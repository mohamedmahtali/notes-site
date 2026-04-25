---
title: Notification channels
tags:
  - beginner
---
# Notification channels

---

## Définition

Les canaux de notification (receivers) sont les destinations où [[Alertmanager]] envoie les alertes : Slack, PagerDuty, email, webhook, OpsGenie, etc.

---

## Slack

```yaml
receivers:
  - name: slack-critical
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/T.../B.../...'
        channel: '#alerts-critical'
        title: |
          [{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}]
          {{ .GroupLabels.alertname }}
        text: |
          {{ range .Alerts }}
          *Alert:* {{ .Annotations.summary }}
          *Description:* {{ .Annotations.description }}
          *Severity:* {{ .Labels.severity }}
          {{ end }}
        color: '{{ if eq .Status "firing" }}danger{{ else }}good{{ end }}'
        send_resolved: true
```

---

## PagerDuty

```yaml
  - name: pagerduty-critical
    pagerduty_configs:
      - routing_key: '<PAGERDUTY_INTEGRATION_KEY>'
        description: '{{ .GroupLabels.alertname }}: {{ .CommonAnnotations.summary }}'
        severity: '{{ .CommonLabels.severity }}'
        details:
          firing: '{{ .Alerts.Firing | len }} alerts firing'
          resolved: '{{ .Alerts.Resolved | len }} alerts resolved'
```

---

## Webhook (générique)

```yaml
  - name: webhook
    webhook_configs:
      - url: 'https://my-alerting-service.internal/webhook'
        send_resolved: true
        http_config:
          bearer_token: 'my-secret-token'
```
