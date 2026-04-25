---
title: Flux Kustomizations
tags:
  - gitops
  - intermediate
---

# Flux Kustomizations

## Définition

Une `Kustomization` Flux est une [[CRD]] qui définit un ensemble de manifests [[Kubernetes]] à appliquer depuis une source [[Git]]. Elle orchestre l'ordre d'application et surveille la santé des ressources.

> [!note] Flux Kustomization ≠ [[kubectl]] Kustomize
> La `Kustomization` Flux (flux.cd/v1) est différente de la `Kustomization` kubectl (kustomize.config.k8s.io). La première pilote Flux, la seconde est le tool de templating.

## Exemple

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 5m          # Réconcilier toutes les 5 minutes
  path: ./apps/production/myapp
  prune: true           # Supprimer les ressources absentes de Git
  sourceRef:
    kind: GitRepository
    name: flux-system
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: myapp
      namespace: production
  timeout: 2m
```

## GitRepository source

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: myapp-repo
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/myorg/myapp
  ref:
    branch: main
```

## Liens

- [[Flux]]
- [[HelmReleases]]
- [[GitOps]]
