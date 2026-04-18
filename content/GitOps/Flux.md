---
title: Flux
tags: [gitops, intermediate]
---

# Flux

## Définition

Flux est un outil GitOps open-source (CNCF) qui automatise la synchronisation de clusters Kubernetes avec des sources Git, Helm charts ou OCI artifacts. Plus léger qu'ArgoCD, il est entièrement piloté par des CRDs Kubernetes.

> [!note] Flux vs ArgoCD
> Flux est plus "natif Kubernetes" (tout via CRDs, pas d'UI propre). ArgoCD a une UI riche et est plus adapté aux équipes qui veulent de la visibilité. Les deux sont excellents — choix selon les préférences d'équipe.

## Installation (Flux CLI)

```bash
# Installer la CLI
curl -s https://fluxcd.io/install.sh | sudo bash

# Bootstrapper le cluster (GitHub)
flux bootstrap github   --owner=myorg   --repository=gitops-repo   --branch=main   --path=clusters/production   --personal

# Vérifier l'installation
flux check
flux get all
```

## Commandes CLI

```bash
flux get kustomizations         # État des Kustomizations
flux get helmreleases           # État des HelmReleases
flux reconcile source git flux-system  # Forcer sync depuis Git
flux reconcile kustomization myapp     # Forcer sync d'une app
flux logs                       # Logs des controllers Flux
flux suspend kustomization myapp    # Pause la réconciliation
flux resume kustomization myapp     # Reprendre
```

## Liens

- [[Kustomizations]]
- [[HelmReleases]]
- [[Image automation]]
- [[GitOps]]
