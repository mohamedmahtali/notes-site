---
title: Reliability indicators
tags:
  - intermediate
---
# Reliability indicators

## Parent
- [[SLO SLA SLI]]

---

## Définition

Les SLIs (Service Level Indicators) sont les métriques concrètes qui mesurent la qualité d'un service du point de vue de l'utilisateur. Ils sont la base des SLOs.

---

## SLIs par type de service

### API REST
```promql
# Availability : % requêtes sans erreur 5xx
sum(rate(http_requests_total{status!~"5.."}[5m]))
/ sum(rate(http_requests_total[5m]))

# Latency : % requêtes < 500ms
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[5m]))
/ sum(rate(http_request_duration_seconds_count[5m]))
```

### Pipeline de données
```promql
# Freshness : données < 5 min
time() - max(data_last_updated_timestamp) < 300

# Throughput : messages traités/s
rate(messages_processed_total[5m]) > 100
```

### Stockage
```promql
# Durability : % opérations d'écriture réussies
rate(write_operations_total{status="success"}[5m])
/ rate(write_operations_total[5m])
```

---

> [!tip]
> Un SLI doit mesurer ce que l'utilisateur perçoit, pas ce que le système fait en interne. Préférer "% requêtes sans erreur" à "CPU < 80%" — l'utilisateur se fiche du CPU.
