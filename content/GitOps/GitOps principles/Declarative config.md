---
title: Declarative config
tags:
  - gitops
  - intermediate
---

# Declarative config

## Définition

La configuration déclarative décrit **ce que l'on veut** (l'état final), non **comment y arriver** (les étapes). [[Kubernetes]] et les outils GitOps utilisent YAML déclaratif : l'orchestrateur détermine comment atteindre l'état décrit.

> [!tip] Avantage clé
> La configuration déclarative est idempotente : appliquer le même YAML 10 fois produit le même résultat. Elle est aussi auto-documentée : le fichier décrit l'état actuel du système.

## Déclaratif vs impératif

```yaml
# ✓ Déclaratif (GitOps)
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 3        # "Je veux 3 replicas"
  template:
    spec:
      containers:
        - image: myapp:1.2.0  # "Je veux cette version"
```

```bash
# ❌ Impératif (pas GitOps)
kubectl scale deployment myapp --replicas=3
kubectl set image deployment/myapp app=myapp:1.2.0
```

## Outils de templating déclaratif

| Outil | Usage |
|-------|-------|
| Kustomize | Patches par environnement, natif [[kubectl]] |
| [[Helm]] | [[Templates]] paramétrables, [[Package]] |
| jsonnet | Templating puissant, plus complexe |

## Liens

- [[GitOps principles]]
- [[Single source of truth]]
- [[GitOps]]
