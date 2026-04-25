---
title: Single source of truth
tags:
  - gitops
  - intermediate
---

# Single source of truth

## Définition

Dans GitOps, [[Git]] est la seule source de vérité pour l'état désiré du système. Aucun changement ne doit être appliqué directement sur le [[Cluster]] (pas de `kubectl apply` manuel en prod) — tout doit passer par un [[Commit]].

> [!warning] Anti-pattern à éviter
> Modifier directement un objet [[Kubernetes]] via `kubectl edit` en production contourne Git. L'agent GitOps détectera la dérive et la corrigera automatiquement (ou alertera selon la politique).

## Implications pratiques

```bash
# ❌ Anti-pattern GitOps
kubectl scale deployment myapp --replicas=5  # Modif directe

# ✓ GitOps correct
# 1. Modifier le YAML dans git
# values.yaml: replicaCount: 5
# 2. Commit + push
# 3. PR approuvée → merge
# 4. ArgoCD/Flux détecte et applique
```

## Organisation du repo Git

```
gitops-repo/
├── apps/
│   ├── production/
│   │   ├── myapp/
│   │   │   ├── deployment.yaml
│   │   │   └── values.yaml
│   └── staging/
├── infrastructure/
│   ├── monitoring/
│   └── ingress/
└── clusters/
    ├── production/
    └── staging/
```

## Liens

- [[GitOps principles]]
- [[Declarative config]]
- [[GitOps]]
