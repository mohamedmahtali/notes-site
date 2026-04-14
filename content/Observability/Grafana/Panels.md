---
title: Panels
tags:
  - beginner
---
# Panels

## Parent
- [[Grafana]]

---

## Définition

Les panels sont les éléments de visualisation dans un dashboard Grafana. Chaque panel affiche des données d'une datasource avec un type de visualisation spécifique : graphique, jauge, tableau, heatmap.

---

## Types de panels

| Type | Usage |
|---|---|
| Time series | Métriques sur le temps (CPU, latence, traffic) |
| Gauge | Valeur instantanée avec seuils (SLO compliance, disk usage) |
| Stat | Valeur unique avec tendance |
| Bar chart | Comparaison entre catégories |
| Table | Données tabulaires (top pods, liste d'alertes) |
| Heatmap | Distribution au fil du temps |
| Logs | Logs depuis Loki/Elasticsearch |
| Alert list | Alertes Grafana actives |

---

## Configuration d'un panel Time Series

```json
{
  "type": "timeseries",
  "title": "HTTP Request Rate",
  "datasource": {"type": "prometheus"},
  "targets": [
    {
      "expr": "sum(rate(http_requests_total[5m])) by (status)",
      "legendFormat": "{{status}}"
    }
  ],
  "fieldConfig": {
    "defaults": {
      "unit": "reqps",
      "thresholds": {
        "steps": [
          {"color": "green", "value": null},
          {"color": "yellow", "value": 100},
          {"color": "red", "value": 500}
        ]
      }
    }
  }
}
```
