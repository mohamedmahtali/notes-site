---
title: Recording rules
tags:
  - intermediate
---
# Recording rules

---

## Définition

Les recording rules pré-calculent des expressions [[PromQL]] complexes et stockent le résultat comme une nouvelle métrique. Elles accélèrent les [[Dashboards]] [[Grafana]] et permettent de réutiliser des calculs coûteux.

---

## Configuration

```yaml
# recording_rules.yml
groups:
  - name: http_metrics
    interval: 30s
    rules:
      # Pré-calculer le taux de requêtes par job
      - record: job:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)

      # Pré-calculer le taux d'erreurs
      - record: job:http_error_rate:rate5m
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) by (job)
          /
          sum(rate(http_requests_total[5m])) by (job)

      # Latence p99 pré-calculée
      - record: job:http_request_duration_seconds:p99
        expr: |
          histogram_quantile(0.99,
            sum(rate(http_request_duration_seconds_bucket[5m])) by (job, le)
          )
```

---

## Utilisation dans Grafana

```promql
# Au lieu de la requête lente :
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# Utiliser la recording rule pré-calculée :
job:http_request_duration_seconds:p99
```

---

> [!tip]
> Nommer les recording rules avec la convention `level:metric:operations` (ex: `job:http_requests:rate5m`). Cela les rend facilement identifiables dans les dashboards.
