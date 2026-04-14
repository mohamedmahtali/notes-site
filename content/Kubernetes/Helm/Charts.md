---
title: Charts
tags:
  - intermediate
---
# Charts

## Parent
- [[Helm]]

---

## Définition

Un chart Helm est un répertoire contenant les templates YAML et la configuration nécessaires pour déployer une application Kubernetes. Il peut être publié dans un registry (Artifact Hub) et partagé entre équipes.

---

## Structure d'un chart

```
mychart/
├── Chart.yaml           # métadonnées (nom, version, description)
├── values.yaml          # valeurs par défaut
├── charts/              # charts dépendants (sub-charts)
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── _helpers.tpl     # templates partiels réutilisables
│   └── NOTES.txt        # instructions post-installation
└── .helmignore
```

---

## Chart.yaml

```yaml
apiVersion: v2
name: myapp
description: My application Helm chart
type: application
version: 1.2.3           # version du chart
appVersion: "2.0.0"      # version de l'application
dependencies:
- name: postgresql
  version: "13.2.0"
  repository: https://charts.bitnami.com/bitnami
  condition: postgresql.enabled
```

---

## Commandes

```bash
# Créer un chart vide
helm create myapp

# Valider le chart
helm lint ./myapp

# Voir les templates rendus
helm template myapp ./myapp --values prod-values.yaml

# Installer les dépendances
helm dependency update ./myapp
```
