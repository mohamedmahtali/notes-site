---
title: Flux
tags:
  - gitops
  - intermediate
---

# Flux

## Définition

Flux est un outil GitOps open-source (CNCF) qui automatise la synchronisation de [[Cluster]] [[Kubernetes]] avec des sources [[Git]], [[Helm]] [[Charts]] ou [[OCI]] [[Artifacts]]. Plus léger qu'[[ArgoCD]], il est entièrement piloté par des [[CRD]] Kubernetes.

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
flux get kustomizations                        # État des Kustomizations
flux get helmreleases                          # État des HelmReleases
flux reconcile source git flux-system          # Forcer sync depuis Git
flux reconcile kustomization myapp             # Forcer sync d'une app
flux logs                                      # Logs des controllers
flux suspend kustomization myapp               # Pause la réconciliation
flux resume kustomization myapp                # Reprendre
```

## Kustomization — déployer depuis Git

```yaml
# Source Git (à créer une fois par repo)
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: gitops-repo
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/myorg/gitops-repo
  ref:
    branch: main
---
# Kustomization — synchroniser un path du repo
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 5m
  path: ./environments/production
  sourceRef:
    kind: GitRepository
    name: gitops-repo
  targetNamespace: production
  prune: true          # Supprimer les ressources absentes de Git
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: myapp
      namespace: production
  timeout: 2m
  retryInterval: 30s
```

## HelmRelease — déployer un chart Helm

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: prometheus
  namespace: monitoring
spec:
  interval: 30m
  chart:
    spec:
      chart: kube-prometheus-stack
      version: ">=45.0.0"
      sourceRef:
        kind: HelmRepository
        name: prometheus-community
  values:
    grafana:
      enabled: true
      adminPassword: "${GRAFANA_PASSWORD}"
    prometheus:
      prometheusSpec:
        retention: 30d
  install:
    createNamespace: true
  upgrade:
    cleanupOnFail: true
    remediation:
      retries: 3
```

## Liens

- [[Kustomizations]]
- [[HelmReleases]]
- [[Image automation]]
- [[GitOps]]
