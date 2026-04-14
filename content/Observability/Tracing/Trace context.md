---
title: Trace context
tags:
  - intermediate
---
# Trace context

## Parent
- [[Tracing]]

---

## Définition

Le trace context est l'ensemble des informations propagées de service en service pour relier les spans d'une même requête distribuée. Il contient le trace ID (unique par requête) et le span ID (unique par opération).

---

## Standards de propagation

| Standard | Header | Usage |
|---|---|---|
| W3C TraceContext | `traceparent`, `tracestate` | Standard moderne (recommandé) |
| B3 Propagation | `X-B3-TraceId`, `X-B3-SpanId` | Zipkin, Istio |
| Jaeger | `uber-trace-id` | Jaeger natif |

---

## Propagation W3C

```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
             │  │                                 │                 │
             v  version                           │                 sampled flag
                trace-id (128 bits)               parent-span-id (64 bits)
```

---

## Propagation inter-services

```python
# FastAPI — avec OpenTelemetry auto-instrumentation
# Les headers sont injectés/extraits automatiquement

# Manuellement si nécessaire
from opentelemetry.propagate import inject, extract

# Côté client — injecter le contexte dans les headers
headers = {}
inject(headers)    # ajoute traceparent, tracestate
requests.get("http://service-b/api", headers=headers)

# Côté serveur — extraire le contexte des headers
context = extract(request.headers)
```
