---
title: Alerts
tags:
  - intermediate
---
# Alerts

## Parent
- [[Grafana]]

---

## Définition

Grafana Alerting permet de définir des règles d'alerte directement dans Grafana (sans passer par Prometheus Alertmanager) et de les router vers des canaux de notification. Depuis Grafana 8+, il centralise toutes les alertes.

---

## Créer une alerte

```yaml
# Grafana Unified Alerting — configuration as code
apiVersion: 1
groups:
  - orgId: 1
    name: Application Alerts
    folder: MyApp
    interval: 1m
    rules:
      - uid: high-error-rate
        title: High Error Rate
        condition: C
        data:
          - refId: A
            datasourceUid: prometheus
            model:
              expr: sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))
          - refId: C
            datasourceUid: __expr__
            model:
              type: threshold
              conditions:
                - evaluator:
                    params: [0.05]
                    type: gt
        noDataState: NoData
        execErrState: Error
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Error rate > 5%"
```

---

## Contact points (canaux de notification)

```
Grafana → Alerting → Contact points :
  - Slack webhook URL
  - PagerDuty integration key
  - Email SMTP
  - OpsGenie API key
```
