---
title: Reconciliation loop
tags:
  - gitops
  - advanced
---

# Reconciliation loop

## Définition

La boucle de réconciliation est le mécanisme central des agents [[GitOps]] (ArgoCD, Flux). En continu, l'agent compare l'état désiré ([[Git]]) avec l'état réel ([[Cluster]]) et corrige les dérives automatiquement.

> [!note] [[Kubernetes]] natif
> Kubernetes lui-même fonctionne sur ce principe : le controller-manager réconcilie en permanence l'état réel vers l'état désiré décrit dans l'[[API server]].

## Flux de réconciliation

```
Git repo (état désiré)
       ↓  poll/webhook (toutes les X minutes)
Agent GitOps (ArgoCD/Flux)
       ↓  compare
Cluster K8s (état réel)
       ↓  si diff détecté
kubectl apply (réconciliation)
       ↓
Cluster K8s (état == désiré)
```

## Gestion des dérives

```yaml
# ArgoCD — politique de sync automatique
spec:
  syncPolicy:
    automated:
      prune: true      # Supprimer les ressources non dans Git
      selfHeal: true   # Corriger les modifs manuelles
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
```

## Liens

- [[GitOps principles]]
- [[Pull vs Push]]
- [[ArgoCD]]
- [[Flux]]
