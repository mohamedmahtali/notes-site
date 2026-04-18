---
title: Dev staging prod
tags: [gitops, intermediate]
---

# Dev / Staging / Production

## Définition

Les trois environnements standard d'une pipeline de déploiement : développement, recette/staging et production. Dans une architecture GitOps, chacun correspond à un path ou une branche dans le repo Git.

> [!note] Parité des environnements
> L'objectif GitOps est d'avoir des environnements aussi similaires que possible. Les différences (replicas, domaines, resources) sont isolées dans des values ou overlays par environnement.

## Structure GitOps par dossier

```
gitops-repo/
├── clusters/
│   ├── dev/
│   │   └── apps/myapp/kustomization.yaml
│   ├── staging/
│   │   └── apps/myapp/kustomization.yaml
│   └── production/
│       └── apps/myapp/kustomization.yaml
└── apps/
    └── myapp/
        ├── base/                  # Config commune
        │   ├── deployment.yaml
        │   └── service.yaml
        └── overlays/
            ├── dev/               # Surcharge dev
            │   └── kustomization.yaml  # replicas: 1
            ├── staging/
            │   └── kustomization.yaml  # replicas: 2
            └── production/
                └── kustomization.yaml  # replicas: 5
```

## Liens

- [[Environments]]
- [[Promotion strategy]]
- [[Multi-cluster]]
