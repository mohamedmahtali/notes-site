---
title: Centralized logging
tags:
  - intermediate
---
# Centralized logging

## Parent
- [[Logging]]

---

## Définition

Le logging centralisé collecte les logs de tous les services et serveurs dans un système unique de stockage et de recherche. Sans centralisation, les logs sont dispersés sur des dizaines de pods/serveurs.

---

## Stacks populaires

| Stack | Collecte | Stockage | Visualisation |
|---|---|---|---|
| ELK | Logstash/Filebeat | Elasticsearch | Kibana |
| EFK | Fluentd/Fluent Bit | Elasticsearch | Kibana |
| PLG | Promtail | Loki | Grafana |
| Datadog | Agent | Datadog | Datadog |

---

## Architecture K8s avec Fluent Bit + Loki

```yaml
# Fluent Bit DaemonSet (collecte les logs de tous les pods)
# → Loki (stockage) → Grafana (visualisation)

# Helm
helm repo add fluent https://fluent.github.io/helm-charts
helm install fluent-bit fluent/fluent-bit   --namespace logging   --set config.outputs='[OUTPUT]
    Name loki
    Host loki.monitoring.svc'
```

---

## Requêtes dans Kibana/Grafana

```
# LogQL (Loki)
{namespace="production", app="myapp"} |= "error"
{app="api"} | json | level="error" | duration > 1000ms

# KQL (Kibana)
level: "error" AND service: "order-service"
```
