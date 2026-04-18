---
title: Flux HelmReleases
tags: [gitops, intermediate]
---

# Flux HelmReleases

## Définition

Une `HelmRelease` Flux est une CRD qui pilote le déploiement et la mise à jour d'un Helm chart de façon GitOps. Flux télécharge le chart et applique les values définies dans Git.

> [!tip] Pourquoi c'est utile
> Plutôt que de faire `helm upgrade` manuellement, définir une HelmRelease dans Git garantit que le chart est toujours à la bonne version avec les bonnes values — et se réconcilie automatiquement.

## Exemple

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: nginx-ingress
  namespace: flux-system
spec:
  interval: 10m
  chart:
    spec:
      chart: ingress-nginx
      version: "4.9.x"           # Contrainte de version
      sourceRef:
        kind: HelmRepository
        name: ingress-nginx
      interval: 10m
  targetNamespace: ingress-nginx
  values:
    controller:
      replicaCount: 2
      metrics:
        enabled: true
  valuesFrom:
    - kind: ConfigMap
      name: nginx-values          # Values depuis une ConfigMap
```

## HelmRepository source

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  name: ingress-nginx
  namespace: flux-system
spec:
  interval: 1h
  url: https://kubernetes.github.io/ingress-nginx
```

## Liens

- [[Flux]]
- [[Kustomizations]]
- [[Helm]]
