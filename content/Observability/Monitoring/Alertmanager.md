---
title: Alertmanager
tags:
  - intermediate
---
# Alertmanager

## Parent
- [[Monitoring]]

## Enfants
- [[Alert routing]]
- [[Notification channels]]
- [[Silences]]

---

## Définition

Alertmanager reçoit les alertes de Prometheus et les achemine vers les bons canaux de notification (Slack, PagerDuty, email) en gérant le groupement, le throttling, et la déduplication.

---

## Configuration

```yaml
# alertmanager.yml
global:
  slack_api_url: 'https://hooks.slack.com/services/...'
  pagerduty_url: 'https://events.pagerduty.com/v2/enqueue'

route:
  receiver: 'default'
  group_by: ['alertname', 'cluster', 'service']
  group_wait: 30s        # attendre avant d'envoyer (groupement)
  group_interval: 5m     # intervalle entre les groupes
  repeat_interval: 4h    # répéter si non résolu

  routes:
    - match:
        severity: critical
      receiver: 'pagerduty'
      continue: true    # aussi envoyer au default receiver

    - match:
        severity: warning
      receiver: 'slack-warnings'

receivers:
  - name: 'default'
    slack_configs:
      - channel: '#alerts'
        title: '[{{ .Status | toUpper }}] {{ .GroupLabels.alertname }}'

  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: '<PAGERDUTY_KEY>'

inhibit_rules:
  # Si critical firing, supprimer les warnings du même service
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'service']
```

---

> [!note]
> Voir [[Alert routing]], [[Notification channels]], [[Silences]] pour les détails de configuration.
