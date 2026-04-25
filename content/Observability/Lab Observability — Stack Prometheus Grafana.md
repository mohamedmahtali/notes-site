---
title: "Lab Observability — Stack Prometheus Grafana"
tags:
  - observability
  - intermediate
---

# Lab Observability — Stack Prometheus Grafana

## Objectif

Déployer une stack d'observabilité complète avec [[Docker compose]] : [[Prometheus]] (métriques), Grafana ([[Dashboards]]), et une application Python exposant des métriques custom.

> [!note] Prérequis
> - [[Docker]] et Docker Compose installés
> - [[Ports]] 3000, 9090, 8000 disponibles

---

## Étape 1 — Application Python avec métriques

```python
# app.py
from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time, random

app = Flask(__name__)

# Métriques Prometheus
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)
REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration",
    ["endpoint"]
)

@app.route("/")
def index():
    with REQUEST_DURATION.labels("/").time():
        time.sleep(random.uniform(0.01, 0.1))
        REQUEST_COUNT.labels("GET", "/", "200").inc()
        return "Hello Observability!"

@app.route("/error")
def error():
    REQUEST_COUNT.labels("GET", "/error", "500").inc()
    return "Error!", 500

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
```

```text
# requirements.txt
flask==3.0.0
prometheus-client==0.20.0
```

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
```

---

## Étape 2 — Configuration Prometheus

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "myapp"
    static_configs:
      - targets: ["app:8000"]
    metrics_path: /metrics

  - job_name: "node-exporter"
    static_configs:
      - targets: ["node-exporter:9100"]
```

```yaml
# alert-rules.yml
groups:
  - name: app
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status="500"}[5m]) > 0.1
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: "Taux d'erreur > 10%"
```

---

## Étape 3 — Docker Compose complet

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "8000:8000"

  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./alert-rules.yml:/etc/prometheus/alert-rules.yml
      - prometheus-data:/prometheus
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.retention.time=15d"

  node-exporter:
    image: prom/node-exporter:latest
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
    command:
      - "--path.procfs=/host/proc"
      - "--path.sysfs=/host/sys"

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: "admin"
    volumes:
      - grafana-data:/var/lib/grafana

volumes:
  prometheus-data:
  grafana-data:
```

---

## Étape 4 — Démarrer et configurer

```bash
docker compose up -d
docker compose ps

# Tester l'app
curl http://localhost:8000
curl http://localhost:8000/metrics
curl http://localhost:8000/error  # Générer des erreurs
```

**Grafana :**
1. Ouvrir http://localhost:3000 (admin/admin)
2. [[Datasources]] → Add → Prometheus → URL: `http://prometheus:9090`
3. Import dashboard ID **1860** ([[Node]] Exporter Full)
4. Créer un panel avec : `rate(http_requests_total[5m])`

---

## Étape 5 — Requêtes PromQL à tester

```promql
# Taux de requêtes/sec
rate(http_requests_total[1m])

# Taux d'erreur
rate(http_requests_total{status="500"}[5m])

# Latence p50/p95/p99
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# CPU node
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

---

## Vérification finale

- [ ] App répond sur :8000, métriques sur :8000/metrics
- [ ] Prometheus scrape l'app ([[Status]] → Targets : UP)
- [ ] Grafana affiche des données Prometheus
- [ ] Dashboard Node Exporter importé
- [ ] Alerte `HighErrorRate` visible dans Prometheus Rules

## Liens

- [[Observability]]
- [[Monitoring]]
- [[Metrics]]
- [[Grafana]]
- [[PromQL]]
