---
title: Scraping
tags:
  - intermediate
---
# Scraping

---

## Définition

Le scraping est le mécanisme par lequel [[Prometheus]] collecte les métriques. Il fait des requêtes HTTP [[get]] vers les endpoints `/metrics` des cibles à intervalles réguliers (scrape_interval). Les cibles exposent leurs métriques au format texte Prometheus.

---

## Format d'exposition

```
# HELP http_requests_total Total number of HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",status="200"} 12847
http_requests_total{method="GET",status="404"} 23
http_requests_total{method="POST",status="200"} 4521

# HELP http_request_duration_seconds Request duration
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.1"} 8421
http_request_duration_seconds_bucket{le="0.5"} 12103
http_request_duration_seconds_bucket{le="+Inf"} 12847
http_request_duration_seconds_sum 1534.2
http_request_duration_seconds_count 12847
```

---

## Service Discovery Kubernetes

```yaml
# Annotation sur un pod pour l'auto-discovery
metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
    prometheus.io/path: "/metrics"
```

---

## Vérifier le scraping

```bash
# Dans Prometheus UI : Status → Targets
# Ou via API
curl http://prometheus:9090/api/v1/targets | jq '.data.activeTargets[] | {job:.job, health:.health}'
```

---

> [!tip]
> Si une cible apparaît en "DOWN" dans Prometheus, vérifier : le pod est-il Running, l'endpoint `/metrics` répond-il, le port est-il correct dans la config scrape ?
