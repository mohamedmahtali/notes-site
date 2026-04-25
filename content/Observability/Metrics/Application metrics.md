---
title: Application metrics
tags:
  - intermediate
---
# Application metrics

---

## Définition

Les métriques applicatives mesurent le comportement de l'application : requêtes/s, latence, taux d'erreur, taille des queues, connexions actives. Elles sont exposées par l'application elle-même via un endpoint `/metrics`.

---

## Exposition avec Prometheus client

```python
# Python — prometheus_client
from prometheus_client import Counter, Histogram, Gauge, start_http_server

REQUEST_COUNT = Counter('http_requests_total', 'Total requests',
                        ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency',
                            ['endpoint'],
                            buckets=[.005, .01, .025, .05, .1, .25, .5, 1, 2.5])
ACTIVE_CONNECTIONS = Gauge('active_connections', 'Active connections')

# Instrumenter les requêtes
@REQUEST_LATENCY.labels(endpoint='/api/users').time()
def get_users():
    REQUEST_COUNT.labels(method='GET', endpoint='/api/users', status='200').inc()
    return ...
```

---

## Métriques business

```go
// Go — métriques métier
ordersTotal := prometheus.NewCounterVec(
    prometheus.CounterOpts{
        Name: "orders_total",
        Help: "Total number of orders",
    },
    []string{"status", "product_type"},
)

revenueGauge := prometheus.NewGaugeVec(
    prometheus.GaugeOpts{
        Name: "revenue_euros_total",
        Help: "Total revenue in euros",
    },
    []string{"region"},
)
```

---

> [!tip]
> Exposer les métriques business (commandes, paiements, utilisateurs actifs) en plus des métriques techniques. Elles sont plus parlantes pour les stakeholders et permettent de corréler les incidents techniques avec l'impact business.
