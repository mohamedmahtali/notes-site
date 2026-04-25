---
title: Environments
tags:
  - gitops
  - intermediate
---

# Environments (GitOps)

## Définition

Dans une architecture GitOps, les environnements (dev, [[Staging]], production) sont représentés comme des dossiers ou branches dans le repo [[Git]]. La promotion d'une version d'un environnement à l'autre se fait via Git (PR, [[Merge]], tag).

> [!tip] Pourquoi c'est important
> Représenter les environnements dans Git garantit que dev, staging et prod sont identiques en termes de configuration, et que les promotions sont traçables et réversibles.

## Structure de repo — deux approches

### Mono-repo (un repo pour tous les envs)

```
infra-gitops/
├── base/                    # Manifests communs
│   ├── deployment.yaml
│   └── service.yaml
├── environments/
│   ├── dev/
│   │   ├── kustomization.yaml
│   │   └── patches/         # Overrides spécifiques dev
│   ├── staging/
│   │   ├── kustomization.yaml
│   │   └── patches/
│   └── production/
│       ├── kustomization.yaml
│       └── patches/
```

### Multi-repo (un repo par env)

```
infra-dev/       → branche main → cluster dev
infra-staging/   → branche main → cluster staging
infra-prod/      → branche main → cluster production
```

> [!note] Mono-repo vs Multi-repo
> Mono-repo = visibilité globale + diffs cross-[[ENV]] faciles. Multi-repo = [[Permissions]] fines (dev n'a pas accès à prod), blast radius limité. En pratique, le mono-repo avec CODEOWNERS est la solution la plus courante.

## Promotion via Kustomize

```yaml
# base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: myapp
        image: myapp:latest
```

```yaml
# environments/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
patches:
  - patch: |-
      - op: replace
        path: /spec/replicas
        value: 5
      - op: replace
        path: /spec/template/spec/containers/0/image
        value: myapp:1.4.2
    target:
      kind: Deployment
      name: myapp
```

```bash
# Prévisualiser le manifest final d'un env
kubectl kustomize environments/production/

# Appliquer (ou laisser ArgoCD/Flux le faire)
kubectl apply -k environments/production/
```

## Promotion ArgoCD — ApplicationSet

```yaml
# Un ApplicationSet génère une Application par environnement
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: myapp
spec:
  generators:
  - list:
      elements:
      - env: dev
        cluster: https://dev.k8s.local
      - env: staging
        cluster: https://staging.k8s.local
      - env: production
        cluster: https://prod.k8s.local
  template:
    spec:
      project: default
      source:
        repoURL: https://github.com/myorg/infra-gitops
        targetRevision: HEAD
        path: environments/{{env}}
      destination:
        server: '{{cluster}}'
        namespace: myapp
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

## Liens

- [[Dev staging prod]]
- [[Promotion strategy]]
- [[Multi-cluster]]
- [[GitOps]]
