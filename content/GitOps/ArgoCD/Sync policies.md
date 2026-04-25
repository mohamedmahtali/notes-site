---
title: Sync policies
tags:
  - gitops
  - intermediate
---

# Sync policies (ArgoCD)

## Définition

Les sync [[Policies]] définissent comment et quand ArgoCD synchronise un [[Cluster]] avec [[Git]]. On peut choisir entre sync manuel (approbation humaine) ou sync automatique (réconciliation continue).

> [!warning] Sync automatique en production
> Le sync auto avec `prune: true` supprime automatiquement les ressources absentes de Git. À utiliser avec prudence en production — s'assurer que les manifests sont complets et corrects.

## Configuration

```yaml
spec:
  syncPolicy:
    automated:
      prune: true       # Supprimer ressources hors Git
      selfHeal: true    # Corriger les modifs manuelles
      allowEmpty: false # Refuser si Git retourne 0 ressource

    syncOptions:
      - CreateNamespace=true    # Créer le namespace si absent
      - PrunePropagationPolicy=foreground
      - ApplyOutOfSyncOnly=true # N'appliquer que ce qui a changé

    retry:
      limit: 5          # Réessayer 5 fois si échec
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

## Sync manuel

```bash
# Synchroniser manuellement
argocd app sync myapp

# Sync avec dry-run
argocd app sync myapp --dry-run

# Sync d'une ressource spécifique
argocd app sync myapp --resource apps:Deployment:myapp
```

## Liens

- [[ArgoCD]]
- [[Applications]]
- [[Reconciliation loop]]
