---
title: PromQL
tags:
  - advanced
---
# PromQL

---

## Définition

PromQL ([[Prometheus]] Query Language) est le langage de requête fonctionnel pour interroger les métriques stockées dans Prometheus. Il permet de calculer des taux, des agrégations, et des fonctions temporelles.

---

## Sélecteurs

```promql
# Métrique simple
http_requests_total

# Avec labels
http_requests_total{job="myapp", status="200"}

# Regex
http_requests_total{status=~"2.."}      # 2xx
http_requests_total{status!~"2.."}      # non-2xx

# Range vector (fenêtre temporelle)
http_requests_total[5m]                 # les 5 dernières minutes
```

---

## Fonctions essentielles

```promql
# Rate — taux d'augmentation par seconde (pour counters)
rate(http_requests_total[5m])

# Increase — augmentation totale sur la période
increase(http_requests_total[1h])

# Irate — rate instantané (plus réactif, moins stable)
irate(http_requests_total[5m])

# Percentiles depuis histogram
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# Agrégations
sum(rate(http_requests_total[5m])) by (job)
avg(node_memory_MemAvailable_bytes) by (instance)
max(container_cpu_usage_seconds_total) by (pod)
topk(5, rate(http_requests_total[5m]))
```

---

## Exemples pratiques

```promql
# Error rate %
sum(rate(http_requests_total{status=~"5.."}[5m]))
/ sum(rate(http_requests_total[5m])) * 100

# CPU par pod Kubernetes
sum(rate(container_cpu_usage_seconds_total{container!=""}[5m])) by (pod)

# Mémoire dispo %
(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

# Requêtes/s par endpoint
topk(10, sum(rate(http_requests_total[5m])) by (handler))
```
