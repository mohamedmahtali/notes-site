---
title: RoleBindings
tags:
  - intermediate
---
# RoleBindings

## Parent
- [[RBAC]]

---

## Définition

Un RoleBinding attribue un Role ou ClusterRole à un ou plusieurs sujets (User, Group, ServiceAccount) dans un namespace. C'est le lien entre "qui" et "quelles permissions".

---

## Manifeste

```yaml
# Attribuer un Role à un ServiceAccount
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: myapp-pod-reader
  namespace: production
subjects:
- kind: ServiceAccount
  name: myapp
  namespace: production
- kind: User
  name: alice@company.com
  apiGroup: rbac.authorization.k8s.io
- kind: Group
  name: dev-team
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role             # ou ClusterRole
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

---

## ClusterRoleBinding

```yaml
# Attribuer un ClusterRole au niveau cluster
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: prometheus-cluster-reader
subjects:
- kind: ServiceAccount
  name: prometheus
  namespace: monitoring
roleRef:
  kind: ClusterRole
  name: node-reader
  apiGroup: rbac.authorization.k8s.io
```

---

## Commandes rapides

```bash
# Créer un RoleBinding rapidement
kubectl create rolebinding dev-edit   --clusterrole=edit   --user=alice@company.com   --namespace=development

kubectl create clusterrolebinding cluster-admin-binding   --clusterrole=cluster-admin   --serviceaccount=kube-system:default
```
