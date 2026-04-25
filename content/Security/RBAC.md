---
title: RBAC
tags:
  - security
  - intermediate
---

# RBAC (Role-Based Access Control)

## Définition

Le RBAC est un modèle de contrôle d'accès où les permissions sont accordées à des rôles, et les utilisateurs ou [[Services]] sont assignés à ces rôles. C'est le standard pour gérer les accès dans [[Kubernetes]], [[AWS]] [[IAM]], et la plupart des systèmes [[Cloud]].

> [!tip] Pourquoi c'est important
> RBAC est la principale défense contre l'escalade de privilèges. Un système sans RBAC correctement configuré [[EXPOSE]] tous ses utilisateurs avec des permissions trop larges.

## Modèle RBAC

```
Utilisateur/Service → Role Binding → Role → Permissions (verbs sur ressources)
```

## RBAC Kubernetes

```yaml
# Role (namespace-scoped)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
---
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
roleRef:
  kind: Role
  name: pod-reader
subjects:
  - kind: User
    name: alice
```

## Liens

- [[Least privilege]]
- [[Roles]]
- [[Permissions]]
