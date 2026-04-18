---
title: Image automation
tags: [gitops, advanced]
---

# Image automation (Flux)

## Définition

L'image automation Flux surveille un container registry et met à jour automatiquement les manifests Git quand une nouvelle image correspondant à une politique de version est publiée. C'est du vrai CD continu.

> [!warning] À utiliser avec précaution
> L'image automation peut déclencher des déploiements en production automatiquement. Limiter aux environnements de dev/staging, ou exiger une politique de version stricte (ex: semver patch only).

## Flux d'image automation

```
Build → push image → Registry
                         ↑ scan (1min)
                    ImageRepository
                         ↓ si new tag matche la policy
                    ImagePolicy
                         ↓ met à jour le YAML dans Git
                    ImageUpdateAutomation
                         ↓ commit git
                    Flux sync → apply sur le cluster
```

## Configuration

```yaml
# Scanner les images
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: myapp
  namespace: flux-system
spec:
  image: ghcr.io/myorg/myapp
  interval: 1m

---
# Politique de sélection des tags
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImagePolicy
metadata:
  name: myapp
  namespace: flux-system
spec:
  imageRepositoryRef:
    name: myapp
  policy:
    semver:
      range: ">=1.0.0 <2.0.0"   # Patches et mineurs de la v1

---
# Automatisation des commits Git
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageUpdateAutomation
metadata:
  name: flux-system
  namespace: flux-system
spec:
  interval: 30m
  sourceRef:
    kind: GitRepository
    name: flux-system
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        name: Flux
        email: flux@example.com
      messageTemplate: "chore: update image to {{range .Updated.Images}}{{.}}{{end}}"
    push:
      branch: main
```

## Liens

- [[Flux]]
- [[HelmReleases]]
- [[Kustomizations]]
