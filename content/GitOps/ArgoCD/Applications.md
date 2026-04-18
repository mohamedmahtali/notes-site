---
title: ArgoCD Applications
tags: [gitops, intermediate]
---

# ArgoCD Applications

## Définition

Une Application ArgoCD est un objet Kubernetes qui définit la source (repo Git + path) et la destination (cluster + namespace) d'une application à déployer. C'est l'unité de base d'ArgoCD.

> [!note] CRD ArgoCD
> `Application` est une Custom Resource Definition (CRD) d'ArgoCD. Elle est stockée dans le namespace `argocd` et réconciliée par les controllers ArgoCD.

## Créer une Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/gitops-repo
    targetRevision: HEAD
    path: apps/production/myapp

  destination:
    server: https://kubernetes.default.svc
    namespace: production

  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

## Via CLI

```bash
argocd app create myapp   --repo https://github.com/myorg/gitops-repo   --path apps/production/myapp   --dest-server https://kubernetes.default.svc   --dest-namespace production   --sync-policy automated
```

## États d'une application

| État | Signification |
|------|--------------|
| `Synced` | Cluster == Git |
| `OutOfSync` | Dérive détectée |
| `Progressing` | Sync en cours |
| `Degraded` | Ressources non saines |
| `Unknown` | Statut indéterminable |

## Liens

- [[ArgoCD]]
- [[Sync policies]]
- [[Health checks]]
- [[App of Apps]]
