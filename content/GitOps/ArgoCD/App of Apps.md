---
title: App of Apps
tags:
  - gitops
  - advanced
---

# App of Apps

## Définition

Le pattern "App of Apps" est une stratégie ArgoCD où une Application racine gère un ensemble d'autres Applications. Elle permet de bootstrapper tout un [[Cluster]] à partir d'un seul objet [[Git]].

> [!tip] Pourquoi c'est utile
> Au lieu de créer manuellement des dizaines d'Applications ArgoCD, une seule Application "root" les déploie toutes. Ajouter une nouvelle app = ajouter un fichier dans Git.

## Structure

```
gitops-repo/
├── root-app.yaml          ← Application racine
└── apps/
    ├── monitoring.yaml    ← Application ArgoCD pour le monitoring
    ├── ingress.yaml       ← Application ArgoCD pour l'ingress
    └── myapp.yaml         ← Application ArgoCD pour myapp
```

## Root Application

```yaml
# root-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: root
  namespace: argocd
spec:
  source:
    repoURL: https://github.com/myorg/gitops-repo
    path: apps/           # Dossier contenant les autres Applications
    targetRevision: HEAD
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd     # Les Applications sont créées dans argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

## Liens

- [[ArgoCD]]
- [[Applications]]
- [[Sync policies]]
- [[GitOps]]
