---
title: Grafana
tags:
  - intermediate
---
# Grafana

## Parent
- [[Observability]]

## Enfants
- [[Datasources]]
- [[Dashboards]]
- [[Panels]]
- [[Alerts]]

---

## Définition

Grafana est la plateforme de visualisation open-source standard pour les métriques, logs, et traces. Il se connecte à de nombreuses sources de données (Prometheus, Loki, Elasticsearch, CloudWatch) et permet de créer des dashboards interactifs.

---

## Pourquoi c'est important

> [!tip] Une seule interface pour tout observer
> Grafana unifie la visualisation de métriques (Prometheus), logs (Loki), et traces (Tempo/Jaeger) dans une seule interface. Les dashboards sont versionnés en JSON et partagés comme du code.

---

## Installation

```bash
# Docker
docker run -d   -p 3000:3000   -v grafana-storage:/var/lib/grafana   --name grafana   grafana/grafana:latest

# Helm sur K8s
helm repo add grafana https://grafana.github.io/helm-charts
helm install grafana grafana/grafana   --namespace monitoring   --set persistence.enabled=true   --set adminPassword=admin123
```

---

## Dashboards communautaires

```bash
# Grafana.com/dashboards
# Node Exporter Full      → ID: 1860
# Kubernetes cluster      → ID: 7249
# NGINX                   → ID: 9614
# PostgreSQL              → ID: 9628
```

---

> [!note]
> Voir [[Datasources]] pour configurer les sources de données, [[Dashboards]] pour créer des vues, [[Panels]] pour les visualisations.
