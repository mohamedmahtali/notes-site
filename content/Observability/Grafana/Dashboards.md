---
title: Dashboards
tags:
  - intermediate
---
# Dashboards

## Parent
- [[Grafana]]

---

## Définition

Un dashboard Grafana est une collection de panels (graphiques, jauges, tableaux) qui visualisent l'état d'un système. Les dashboards sont stockés en JSON et peuvent être versionnés dans Git.

---

## Bonnes pratiques

```
Organisation recommandée :
├── Overview        — état global (SLOs, traffic, errors)
├── Infrastructure  — CPU, mémoire, disque, réseau
├── Application     — latence, throughput, erreurs par service
├── Business        — KPIs business (commandes, revenus)
└── Incidents       — dashboards de diagnostic

Variables de template :
  - $cluster, $namespace, $pod, $service
  → Même dashboard, filtres différents
```

---

## Provisioning (Dashboard as Code)

```yaml
# /etc/grafana/provisioning/dashboards/dashboards.yml
apiVersion: 1
providers:
  - name: 'Default'
    folder: 'Platform'
    type: file
    options:
      path: /var/lib/grafana/dashboards
      foldersFromFilesStructure: true
```

```bash
# Le JSON du dashboard est versionné dans git
git add dashboards/kubernetes-overview.json
git commit -m "chore: update K8s overview dashboard"
# → Grafana recharge automatiquement les dashboards depuis le filesystem
```

---

> [!tip]
> Exporter les dashboards importants en JSON et les committer dans le repo. Utiliser le provisioning Grafana pour les charger automatiquement — évite de perdre les dashboards si le pod Grafana est recréé.
