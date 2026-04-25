---
title: ClusterRoles
tags:
  - intermediate
---
# ClusterRoles

---

## Définition

Un ClusterRole définit des [[Permissions]] à l'échelle du [[Cluster]] (non limité à un namespace). Il peut gérer des ressources cluster-scoped ([[Node]], PersistentVolumes, [[Namespaces]]) ou être utilisé dans plusieurs namespaces via un ClusterRoleBinding.

---

## Cas d'usage

> [!note] ClusterRole vs Role
> - **Role** : permissions dans un namespace → pour les applications
> - **ClusterRole** : permissions cluster-wide → pour les opérateurs, [[Monitoring]], [[Ingress]] controllers

---

## ClusterRoles prédéfinis

```bash
kubectl get clusterroles | grep -v system:

# Les 4 roles prédéfinis importants
# cluster-admin → tout faire sur tout
# admin         → tout dans un namespace (hors quota/limitrange)
# edit          → modifier les ressources (hors RBAC)
# view          → lecture seule
```

---

## Manifeste

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-reader
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["persistentvolumes"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["metrics.k8s.io"]
  resources: ["nodes", "pods"]
  verbs: ["get", "list"]
```

---

```bash
kubectl describe clusterrole cluster-admin
kubectl describe clusterrole edit
```
