---
title: Rollbacks
tags:
  - intermediate
---
# Rollbacks

## Parent
- [[Deployments]]

---

## Définition

Un rollback Kubernetes revient à une version précédente d'un Deployment en restaurant un ancien ReplicaSet. C'est instantané — les pods de l'ancienne version sont disponibles sans rebuild.

---

## Pourquoi c'est rapide

Les anciens ReplicaSets sont conservés (à 0 réplicas) après chaque update. Un rollback consiste simplement à remettre l'ancien RS à 3 réplicas et descendre le nouveau à 0 — aucun pull d'image nécessaire si elle est déjà sur les nodes.

---

## Commandes

```bash
# Rollback vers la revision précédente
kubectl rollout undo deployment/myapp

# Rollback vers une revision spécifique
kubectl rollout history deployment/myapp   # voir les revisions
kubectl rollout undo deployment/myapp --to-revision=3

# Vérifier après rollback
kubectl rollout status deployment/myapp
kubectl get pods -l app=myapp

# Voir quelle image tourne
kubectl get deployment myapp -o jsonpath='{.spec.template.spec.containers[0].image}'
```

---

## Annoter pour l'historique

```bash
# Ajouter une annotation CHANGE-CAUSE lisible dans l'historique
kubectl set image deployment/myapp app=myapp:2.0
kubectl annotate deployment/myapp kubernetes.io/change-cause="Upgrade to v2.0: add auth feature"

kubectl rollout history deployment/myapp
# REVISION  CHANGE-CAUSE
# 1         Initial deployment v1.0
# 2         Upgrade to v2.0: add auth feature
```

---

> [!warning]
> `.spec.revisionHistoryLimit` (défaut: 10) contrôle combien de ReplicaSets sont gardés. Réduire à 3-5 en production pour limiter les ressources, mais garder au moins 2 pour pouvoir rollback.
