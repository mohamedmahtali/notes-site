---
title: Tracing
tags:
  - advanced
---
# Tracing

## Définition

Le tracing distribué suit le chemin d'une requête à travers plusieurs [[Services]] dans une architecture microservices. Il permet de mesurer la latence de chaque composant et d'identifier où se situe un goulot d'étranglement.

> [!note] Quand les métriques ne suffisent pas
> Les métriques indiquent que la latence est haute ; les logs indiquent qu'il y a des erreurs ; le tracing indique QUEL service, QUELLE opération, et COMBIEN DE TEMPS prend chaque étape d'une requête.

## Anatomie d'une trace

```
Trace ID: abc-123 (identifie la requête end-to-end)
│
├── Span 1 : API Gateway          0ms → 70ms  (70ms total)
│   ├── Span 2 : Auth Service     2ms → 7ms   (5ms)
│   ├── Span 3 : User Service    10ms → 60ms  (50ms) ← goulot !
│   │   └── Span 4 : PostgreSQL  12ms → 52ms  (40ms) ← vraie cause
│   └── Span 5 : Cache lookup    62ms → 65ms  (3ms)
└── Response                          70ms
```

- **Trace** : la requête complète, de bout en bout
- **Span** : une opération unitaire (appel HTTP, requête BDD, cache)
- **Parent span** : span qui a déclenché d'autres spans
- **Trace ID** : identifiant unique propagé dans tous les headers

## OpenTelemetry — standard d'instrumentation

OpenTelemetry (OTel) est le standard CNCF pour instrumenter les applications. Il remplace Jaeger client, Zipkin client, etc.

```python
# Python — instrumentation automatique (FastAPI)
pip install opentelemetry-sdk opentelemetry-instrumentation-fastapi

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Configurer l'exporteur (vers Jaeger, Tempo, etc.)
provider = TracerProvider()
provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint="http://jaeger:4317"))
)
trace.set_tracer_provider(provider)

# Instrumenter
tracer = trace.get_tracer("my-service")

def process_order(order_id: str):
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)
        span.set_attribute("order.source", "web")
        # ... logique métier
```

```go
// Go — span manuel
import "go.opentelemetry.io/otel"

tracer := otel.Tracer("my-service")

func HandleRequest(ctx context.Context) {
    ctx, span := tracer.Start(ctx, "handle_request")
    defer span.End()

    span.SetAttributes(attribute.String("user.id", userID))
    // Passer ctx aux appels downstream pour propager le trace ID
    callDatabase(ctx)
}
```

## Déployer Jaeger (tracing backend)

```yaml
# Jaeger all-in-one (dev/staging)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jaeger
spec:
  replicas: 1
  template:
    spec:
      containers:
        - name: jaeger
          image: jaegertracing/all-in-one:latest
          ports:
            - containerPort: 16686   # UI
            - containerPort: 4317    # OTLP gRPC
            - containerPort: 4318    # OTLP HTTP
          env:
            - name: COLLECTOR_OTLP_ENABLED
              value: "true"
```

```bash
# Port-forward pour accéder à l'UI
kubectl port-forward svc/jaeger 16686:16686
# Ouvrir http://localhost:16686
```

## Propagation du contexte

Le trace ID doit être propagé dans tous les appels entre services via les headers HTTP :

```
Service A → HTTP call → Service B
Headers: {
  traceparent: "00-abc123...-def456...-01"
  # format W3C : version-traceId-parentSpanId-flags
}
```

OpenTelemetry gère la propagation automatiquement si tous les services utilisent le même SDK. En pratique : instrumenter les clients HTTP et les frameworks web.

## Sampling — ne pas tout tracer

En production, tracer 100% des requêtes est trop coûteux. Stratégies :

| Stratégie | Description | Usage |
|-----------|-------------|-------|
| Head sampling | Décision à l'entrée (ex: 10%) | Simple, basse charge |
| Tail sampling | Décision à la fin (garder les erreurs/lents) | Précis, plus complexe |
| Rate limiting | N traces/seconde max | Protège les backends |

```yaml
# Tail sampling dans OpenTelemetry Collector
processors:
  tail_sampling:
    decision_wait: 10s
    policies:
      - name: errors-policy
        type: status_code
        status_code: {status_codes: [ERROR]}
      - name: slow-traces-policy
        type: latency
        latency: {threshold_ms: 1000}
      - name: probabilistic-policy
        type: probabilistic
        probabilistic: {sampling_percentage: 5}
```

## Corrélation logs + traces

L'intérêt maximal du tracing vient de la corrélation avec les logs :

```python
# Injecter le trace_id dans les logs
from opentelemetry import trace

def get_current_trace_id():
    span = trace.get_current_span()
    ctx = span.get_span_context()
    return format(ctx.trace_id, '032x') if ctx.is_valid else "no-trace"

log.info("order processed",
    order_id=order_id,
    trace_id=get_current_trace_id()   # → corrélation dans Grafana/Jaeger
)
```

Dans Grafana, cliquer sur un log avec `trace_id` ouvre directement la trace Jaeger/Tempo correspondante.

## Outils

| Outil | Description | Usage |
|-------|-------------|-------|
| Jaeger | Tracing open-source CNCF | Self-hosted, K8s |
| Grafana Tempo | Tracing scalable, intégré Grafana | Stack Grafana |
| Zipkin | Tracing open-source (Twitter) | Simple, legacy |
| AWS X-Ray | Solution AWS native | Tout sur AWS |
| Datadog APM | Solution commerciale | Enterprise |

## Explorer

- **[[Metrics]]** — métriques quantitatives, complément du tracing
- **[[Logging]]** — logs événements, corrélés via trace_id
- **[[SLO SLA SLI]]** — mesurer la fiabilité à partir des traces
- **[[Grafana]]** — visualisation des traces avec Tempo
