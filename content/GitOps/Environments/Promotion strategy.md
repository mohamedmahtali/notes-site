---
title: Promotion strategy
tags:
  - gitops
  - intermediate
---

# Promotion strategy

## Définition

La stratégie de promotion définit comment une version d'application progresse de dev vers [[Staging]] puis production dans une [[Pipeline]] [[GitOps]]. Chaque promotion est un événement [[Git]] (PR, [[Merge]], tag).

> [!tip] Pourquoi Git pour les promotions
> La promotion via PR permet une revue humaine, un audit trail complet et un [[Rollback]] immédiat. C'est le cœur de la valeur GitOps pour les équipes en production.

## Stratégies courantes

### 1. Promotion par mise à jour d'image tag

```bash
# Étape 1 : CI build + push image
docker push ghcr.io/myorg/myapp:v1.2.3

# Étape 2 : Ouvrir une PR pour mettre à jour staging
# Modifier apps/overlays/staging/kustomization.yaml
# images:
#   - name: myapp
#     newTag: v1.2.3

# Étape 3 : Après validation staging, PR pour production
# images:
#   - name: myapp
#     newTag: v1.2.3
```

### 2. Promotion par branche Git

```
feature/* → dev branch → staging branch → main (production)
             ArgoCD dev    ArgoCD staging   ArgoCD prod
```

### 3. Flux image automation (automatique)

```yaml
# Staging : auto-update sur toute nouvelle image
policy:
  semver:
    range: ">=0.0.0"

# Production : seulement les releases stables
policy:
  semver:
    range: ">=1.0.0 <2.0.0"
```

## Liens

- [[Environments]]
- [[Dev staging prod]]
- [[Image automation]]
