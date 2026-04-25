---
title: Metrics
tags:
  - intermediate
---
# Metrics

---

## Définition

Les métriques sont des mesures numériques collectées périodiquement : CPU, mémoire, requêtes par seconde, taux d'erreur, latence. Elles donnent une vue quantitative de l'état du système au fil du temps.

---

## Types de métriques

| Type | Description | Exemple |
|---|---|---|
| Counter | Toujours croissant | Nombre de requêtes total |
| Gauge | Valeur instantanée | CPU actuel, connexions ouvertes |
| Histogram | Distribution de valeurs | Latences p50/p95/p99 |
| Summary | Quantiles calculés côté client | Identique histogram, moins flexible |

---

## Pourquoi c'est important

> [!tip] Les métriques répondent à "combien"
> Les métriques permettent de détecter les anomalies (spike de latence), de planifier la capacité, et de mesurer l'impact des déploiements. Les logs répondent à "pourquoi", les métriques à "combien" et "depuis quand".

---

## Exposer des métriques avec Prometheus

```python
# Python — exposer des métriques custom
from prometheus_client import Counter, Histogram, start_http_server

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency',
                            buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0])

@REQUEST_LATENCY.time()
def handle_request(method):
    # ... logique métier
    REQUEST_COUNT.labels(method=method, status='200').inc()

start_http_server(8000)  # Expose /metrics sur le port 8000
```

```yaml
# Kubernetes — annoter un Pod pour la découverte Prometheus
metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8000"
    prometheus.io/path: "/metrics"
```

## Requêtes PromQL essentielles

```promql
# Taux de requêtes par seconde (sur 5 min)
rate(http_requests_total[5m])

# Taux d'erreurs (5xx)
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])

# Latence p99
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# CPU utilisé par pod
rate(container_cpu_usage_seconds_total{namespace="production"}[5m])

# Mémoire utilisée vs limite
container_memory_working_set_bytes / container_spec_memory_limit_bytes
```

## Seuils d'alerte courants

| Métrique | Seuil d'alerte | Seuil critique |
|----------|---------------|----------------|
| CPU | > 80% pendant 5 min | > 95% pendant 2 min |
| Mémoire | > 85% | > 95% |
| Taux d'erreur | > 1% | > 5% |
| Latence p99 | > 500ms | > 2s |
| Disk | > 80% | > 90% |

> [!note]
> Voir [[USE method]] pour les métriques d'infra, [[RED method]] pour les métriques applicatives, [[Monitoring/Prometheus]] pour la collecte.
