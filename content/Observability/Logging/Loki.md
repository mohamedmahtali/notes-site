---
title: Loki
tags:
  - intermediate
---
# Loki

## Parent
- [[Logging]]

---

## Définition

Grafana Loki est un système de stockage de logs horizontalement scalable inspiré de Prometheus. Contrairement à Elasticsearch, il indexe uniquement les labels (pas le contenu des logs), ce qui le rend beaucoup plus économique.

---

## Architecture

```
Pods → Promtail (agent) → Loki (stockage) → Grafana (visualisation)
```

---

## Installation K8s

```bash
helm repo add grafana https://grafana.github.io/helm-charts

# Stack complète Loki + Promtail + Grafana
helm install loki-stack grafana/loki-stack   --namespace monitoring   --set grafana.enabled=true   --set promtail.enabled=true   --set loki.persistence.enabled=true   --set loki.persistence.size=10Gi
```

---

## LogQL — requêtes Loki

```logql
# Logs d'un namespace
{namespace="production"}

# Filtrer par contenu
{app="myapp"} |= "error"
{app="myapp"} != "health"

# Parser JSON et filtrer
{app="myapp"} | json | level="error"

# Métriques depuis les logs (log rate)
sum(rate({namespace="production", level="error"}[5m])) by (app)

# Extraire et filtrer des champs
{app="api"} | json | duration_ms > 1000
```

---

> [!tip]
> Loki est 10x moins cher qu'Elasticsearch pour les logs cloud-native. L'inconvénient : pas de full-text search rapide (il scanne les logs bruts). Pour des recherches complexes sur de gros volumes, Elasticsearch reste plus adapté.
