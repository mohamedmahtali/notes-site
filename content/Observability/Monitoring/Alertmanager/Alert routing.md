---
title: Alert routing
tags:
  - intermediate
---
# Alert routing

## Parent
- [[Alertmanager]]

---

## Définition

Le routing des alertes définit comment chaque alerte est acheminée vers le bon receiver basé sur les labels (severity, team, service). Il utilise un arbre de routes avec des matchers.

---

## Configuration de routing

```yaml
route:
  receiver: 'default-receiver'
  group_by: ['alertname']

  routes:
    # Alertes critiques → PagerDuty (on-call)
    - matchers:
        - severity = critical
      receiver: pagerduty
      group_wait: 0s    # immédiat pour critical

    # Alertes de l'équipe DB → canal Slack DB
    - matchers:
        - team = database
      receiver: slack-database
      routes:
        # Sous-route : critical DB → aussi PagerDuty
        - matchers:
            - severity = critical
          receiver: pagerduty

    # Alertes business → équipe produit
    - matchers:
        - category = business
      receiver: slack-product
      repeat_interval: 1h
```

---

## Règles d'alert dans Prometheus

```yaml
# alert_rules.yml
groups:
  - name: app-alerts
    rules:
      - alert: HighErrorRate
        expr: job:http_error_rate:rate5m > 0.05
        for: 2m
        labels:
          severity: critical    # utilisé pour le routing
          team: backend
        annotations:
          summary: "High error rate on {{ $labels.job }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```
