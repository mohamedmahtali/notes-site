---
title: Roles
tags:
  - intermediate
---
# Roles

---

## Définition

Un Role définit un ensemble de [[Permissions]] dans un namespace spécifique. Il spécifie les ressources sur lesquelles les actions sont autorisées et les verbs ([[get]], [[create]], delete...) permis. Contrairement au ClusterRole, un Role est limité à un namespace.

---

## Manifeste

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: production
rules:
- apiGroups: [""]             # "" = core API group (pods, services, etc.)
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch"]

- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "update", "patch"]

- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get"]
  resourceNames: ["db-secret"] # limiter à des ressources spécifiques
```

---

## Verbs disponibles

```
get      → lire une ressource
list     → lister les ressources
watch    → surveiller les changements
create   → créer
update   → remplacer entièrement
patch    → modification partielle
delete   → supprimer
deletecollection → supprimer en masse
exec     → kubectl exec
portforward → kubectl port-forward
```

---

```bash
kubectl get roles -n production
kubectl describe role pod-reader -n production
```
