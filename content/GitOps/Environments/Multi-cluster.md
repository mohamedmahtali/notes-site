---
title: Multi-cluster
tags:
  - gitops
  - advanced
---

# Multi-cluster (GitOps)

## Définition

La gestion multi-[[Cluster]] [[GitOps]] permet de déployer et synchroniser plusieurs clusters [[Kubernetes]] (par région, par client, par environnement) depuis un seul repo [[Git]], avec ArgoCD ou Flux.

> [!tip] Pourquoi c'est important
> Les architectures enterprise ont souvent 10-100 clusters. GitOps permet de les gérer centralement avec les mêmes garanties (consistance, audit, [[Rollback]]) que pour un seul cluster.

## ArgoCD — Multi-cluster

```bash
# Enregistrer un cluster distant
argocd cluster add prod-eu-west-1 --name prod-eu

# Lister les clusters
argocd cluster list

# Déployer sur un cluster spécifique
kubectl apply -f - <<EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-eu
  namespace: argocd
spec:
  destination:
    server: https://prod-eu.k8s.example.com  # Cluster distant
    namespace: production
  source:
    repoURL: https://github.com/myorg/gitops
    path: apps/production
EOF
```

## Flux — Multi-cluster (hub-spoke)

```
Hub cluster (ArgoCD/Flux installé)
├── cluster-prod-eu → GitRepository + Kustomization
├── cluster-prod-us → GitRepository + Kustomization
└── cluster-staging → GitRepository + Kustomization
```

## Structure repo multi-cluster

```
gitops-repo/
└── clusters/
    ├── prod-eu-west-1/
    │   ├── infrastructure.yaml
    │   └── apps.yaml
    ├── prod-us-east-1/
    │   ├── infrastructure.yaml
    │   └── apps.yaml
    └── staging/
        ├── infrastructure.yaml
        └── apps.yaml
```

## Liens

- [[Environments]]
- [[Dev staging prod]]
- [[ArgoCD]]
- [[Flux]]
