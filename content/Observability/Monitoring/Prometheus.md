---
title: Prometheus
tags:
  - intermediate
---
# Prometheus

---

## Définition

Prometheus est la base de données de séries temporelles (TSDB) open-source standard pour le [[Monitoring]] [[Cloud]]-native. Il collecte les métriques en [[Scraping]] des endpoints HTTP `/metrics` à intervalle régulier.

---

## Architecture

```
Targets (apps, nodes, K8s)
    ↑ scrape HTTP /metrics
Prometheus Server
    ├── TSDB (stockage local)
    ├── Rule engine (alertes)
    └── HTTP API (PromQL)
         ↓
    Grafana / AlertManager
```

---

## Configuration

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

rule_files:
  - "alert_rules.yml"

scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: 'true'

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

---

## Déploiement K8s

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack   --namespace monitoring --create-namespace
```

---

> [!note]
> Voir [[PromQL]] pour interroger les métriques, [[Exporters]] pour les agents de collecte, [[Recording rules]] pour les agrégations.
