---
title: Spans
tags:
  - intermediate
---
# Spans

---

## Définition

Un span est l'unité de base du [[Tracing]] distribué. Il représente une opération unique (requête HTTP, requête DB, appel de fonction) avec un début, une fin, des attributs, et des événements.

---

## Structure d'un span

```json
{
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "spanId": "00f067aa0ba902b7",
  "parentSpanId": "b7ad6b7169203331",
  "operationName": "GET /api/users/{id}",
  "startTime": "2024-01-15T10:23:45.123Z",
  "duration": 45,
  "status": "OK",
  "attributes": {
    "http.method": "GET",
    "http.url": "/api/users/123",
    "http.status_code": 200,
    "db.system": "postgresql",
    "db.statement": "SELECT * FROM users WHERE id = $1"
  },
  "events": [
    {"name": "cache miss", "timestamp": "..."},
    {"name": "db query start", "timestamp": "..."}
  ]
}
```

---

## Créer des spans manuels

```python
# OpenTelemetry Python
from opentelemetry import trace

tracer = trace.get_tracer("myapp")

def process_order(order_id):
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)
        span.set_attribute("order.amount", 99.99)

        with tracer.start_as_current_span("validate_payment"):
            result = validate_payment(order_id)
            span.add_event("payment validated")

        return result
```
