---
title: ArgoCD
tags: [gitops, intermediate]
---

# ArgoCD

## Définition

ArgoCD est un outil GitOps déclaratif pour Kubernetes. Il surveille des repos Git et synchronise automatiquement l'état des applications Kubernetes avec la configuration déclarée dans Git.

> [!tip] Pourquoi ArgoCD ?
> ArgoCD offre une UI web complète, la gestion des Applications Kubernetes, des health checks automatiques, et un historique complet des déploiements avec possibilité de rollback en un clic.

## Installation

```bash
kubectl create namespace argocd
kubectl apply -n argocd   -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Accéder à l'UI
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Mot de passe admin initial
kubectl -n argocd get secret argocd-initial-admin-secret   -o jsonpath="{.data.password}" | base64 -d
```

## ArgoCD CLI

```bash
argocd login localhost:8080
argocd app list
argocd app get myapp
argocd app sync myapp
argocd app rollback myapp 3    # Rollback à la révision 3
argocd app diff myapp          # Diff Git vs cluster
argocd app delete myapp
```

## Liens

- [[Applications]]
- [[App of Apps]]
- [[Sync policies]]
- [[Health checks]]
- [[GitOps]]
