---
title: RED method
tags:
  - intermediate
---
# RED method

---

## Définition

La méthode RED (Rate, Errors, Duration) de Tom Wilkie est une framework pour surveiller les [[Services]] et microservices. Elle se concentre sur les métriques orientées utilisateur plutôt que sur les ressources.

---

## Les trois dimensions

| Dimension | Description | Exemples métriques |
|---|---|---|
| **R**ate | Requêtes par seconde | `http_requests_total` |
| **E**rrors | Taux d'erreur | `http_requests_total{status=~"5.."}` |
| **D**uration | Latence des requêtes | `http_request_duration_seconds` |

---

## Métriques RED en PromQL

```promql
# Rate — requêtes/s sur les 5 dernières minutes
rate(http_requests_total[5m])

# Error rate — % d'erreurs 5xx
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m])) * 100

# Duration — latence p99
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

---

## Alertes RED typiques

```yaml
# Alertmanager rules
- alert: HighErrorRate
  expr: |
    sum(rate(http_requests_total{status=~"5.."}[5m]))
    / sum(rate(http_requests_total[5m])) > 0.05
  for: 2m
  annotations:
    summary: "Error rate > 5% for 2 minutes"

- alert: HighLatency
  expr: |
    histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 1
  for: 5m
  annotations:
    summary: "p99 latency > 1s"
```

---

> [!tip]
> Combiner RED (vue service) et USE (vue ressource) pour une observabilité complète. RED pour détecter qu'il y a un problème côté utilisateur, USE pour trouver quelle ressource en est la cause.
