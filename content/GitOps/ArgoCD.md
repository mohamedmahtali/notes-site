---
title: ArgoCD
tags:
  - gitops
  - intermediate
---

# ArgoCD

## Définition

ArgoCD est un outil GitOps déclaratif pour [[Kubernetes]]. Il surveille des repos [[Git]] et synchronise automatiquement l'état des applications Kubernetes avec la configuration déclarée dans Git.

> [!tip] Pourquoi ArgoCD ?
> ArgoCD offre une UI web complète, la gestion des Applications Kubernetes, des health checks automatiques, et un historique complet des déploiements avec possibilité de [[Rollback]] en un clic.

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

## Créer une Application

```yaml
# Application ArgoCD — déployer depuis Git
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
    path: environments/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true       # Supprimer les ressources absentes de Git
      selfHeal: true    # Corriger les dérives manuelles
    syncOptions:
      - CreateNamespace=true
      - ApplyOutOfSyncOnly=true   # N'applique que ce qui a changé
    retry:
      limit: 3
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

```bash
# Créer l'app via CLI
argocd app create myapp \
  --repo https://github.com/myorg/gitops-repo \
  --path environments/production \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace production \
  --sync-policy automated \
  --auto-prune \
  --self-heal
```

## Sync manuel avec preview

```bash
# Voir le diff avant d'appliquer
argocd app diff myapp --local ./environments/production

# Sync avec dry-run (ne rien appliquer)
argocd app sync myapp --dry-run

# Sync en forçant même si OutOfSync
argocd app sync myapp --force

# Sync d'une seule ressource
argocd app sync myapp --resource apps:Deployment:myapp
```

## Liens

- [[Applications]]
- [[App of Apps]]
- [[Sync policies]]
- [[Health checks]]
- [[GitOps]]
