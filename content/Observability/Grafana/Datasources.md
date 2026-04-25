---
title: Datasources
tags:
  - beginner
---
# Datasources

---

## Définition

Les datasources [[Grafana]] sont les connexions aux systèmes de données externes ([[Prometheus]], [[Loki]], InfluxDB, Elasticsearch, CloudWatch). Chaque dashboard utilise une ou plusieurs datasources.

---

## Configuration via UI

```
Configuration → Data Sources → Add data source

Prometheus :
  URL: http://prometheus:9090
  Scrape interval: 15s

Loki :
  URL: http://loki:3100

Elasticsearch :
  URL: http://elasticsearch:9200
  Index: logs-*
  Time field: @timestamp
```

---

## Configuration as Code (Grafana Provisioning)

```yaml
# /etc/grafana/provisioning/datasources/datasources.yml
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    url: http://prometheus:9090
    isDefault: true
    jsonData:
      timeInterval: "15s"

  - name: Loki
    type: loki
    url: http://loki:3100

  - name: CloudWatch
    type: cloudwatch
    jsonData:
      authType: default
      defaultRegion: eu-west-1
```
