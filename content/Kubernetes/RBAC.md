---
title: RBAC
tags:
  - intermediate
---
# RBAC

---

## Définition

RBAC (Role-Based Access Control) est le système d'autorisation de [[Kubernetes]]. Il contrôle quelles actions (verbs) un utilisateur ou une application peut effectuer sur quelles ressources ([[Pods]], [[Services]], [[Secrets]]) dans quels [[Namespaces]].

---

## Pourquoi c'est important

> [!warning] Principe du moindre privilège
> Par défaut, les [[Service accounts]] ont peu de droits. Toujours accorder le minimum nécessaire. Un pod compromis avec trop de droits RBAC peut lire tous les secrets du [[Cluster]], créer des pods privilégiés, ou escalader ses privilèges.

---

## Concepts clés

```
Role/ClusterRole  → définit les permissions (quoi faire)
RoleBinding/ClusterRoleBinding → attribue les permissions (à qui)

Subject (qui) :
  - User (authentifié via cert, OIDC, etc.)
  - Group
  - ServiceAccount (pour les pods)

Resources (sur quoi) :
  - pods, services, deployments, secrets, configmaps...

Verbs (quoi faire) :
  - get, list, watch, create, update, patch, delete
```

---

## Vérifier les permissions

```bash
# Est-ce que je peux faire X ?
kubectl auth can-i get pods
kubectl auth can-i create deployments --namespace production
kubectl auth can-i delete secrets --as system:serviceaccount:default:myapp

# Lister les permissions d'un subject
kubectl auth can-i --list --as system:serviceaccount:default:myapp
```

---

> [!note]
> Voir [[Roles]] et [[ClusterRoles]] pour les objets de [[Permissions]], [[RoleBindings]] pour les attributions.
