---
title: Cheat sheet Observabilité
tags:
  - observability
  - intermediate
---

# Cheat sheet Observabilité

## PromQL — Requêtes Prometheus

```promql
# Valeur instantanée
up                                          # Targets en vie (1=up, 0=down)
http_requests_total                         # Compteur brut

# Rate (taux par seconde sur 5min)
rate(http_requests_total[5m])

# Error rate
rate(http_requests_total{status=~"5.."}[5m])
  / rate(http_requests_total[5m])

# Latence p99
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# CPU node
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# RAM disponible (%)
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100

# Agrégation
sum(rate(http_requests_total[5m])) by (service)
avg(cpu_usage) by (namespace)
topk(5, http_requests_total)                # Top 5
```

## Alertmanager

```yaml
# Règle d'alerte Prometheus
groups:
  - name: slo
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Error rate > 5%"
```

## Loki — LogQL

```logql
# Filtres de base
{app="nginx"}                               # Logs de nginx
{app="nginx"} |= "ERROR"                   # Contenant "ERROR"
{app="nginx"} != "DEBUG"                   # Sans "DEBUG"
{app="nginx"} |~ "timeout|refused"        # Regex

# Parsing
{app="nginx"} | json                       # Parser JSON
{app="nginx"} | json | status >= 400      # Filtrer après parse
{app="nginx"} | logfmt                     # Parser logfmt

# Métriques depuis logs
rate({app="nginx"} |= "error" [5m])        # Taux d'erreurs
count_over_time({app="nginx"}[1h])         # Compte sur 1h
```

## Grafana CLI

```bash
# Plugins
grafana-cli plugins list-remote
grafana-cli plugins install grafana-piechart-panel

# Import/export dashboard
# Via API
curl -X GET http://admin:pass@grafana:3000/api/dashboards/uid/abc123
curl -X POST http://admin:pass@grafana:3000/api/dashboards/import \
  -H "Content-Type: application/json" \
  -d @dashboard.json
```

## OpenTelemetry (OTel)

```bash
# Variables d'env standard
OTEL_SERVICE_NAME=myapp
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_TRACES_SAMPLER=parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG=0.1  # 10% sampling
```

## Liens

- [[Observability]]
- [[Monitoring]]
- [[Metrics]]
- [[Logging]]
- [[Tracing]]
- [[Grafana]]
