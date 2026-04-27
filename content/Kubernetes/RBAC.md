---
title: RBAC
tags:
  - intermediate
---
# RBAC

## Définition

RBAC (Role-Based Access Control) est le système d'autorisation de [[Kubernetes]]. Il contrôle quelles actions (verbs) un utilisateur ou une application peut effectuer sur quelles ressources ([[Pods]], [[Services]], [[Secrets]]) dans quels [[Namespaces]].

> [!warning] Principe du moindre privilège
> Par défaut, les [[Service accounts]] ont peu de droits. Toujours accorder le minimum nécessaire. Un pod compromis avec trop de droits RBAC peut lire tous les secrets du cluster, créer des pods privilégiés, ou escalader ses privilèges.

## Modèle : Role → Binding → Subject

```
Role / ClusterRole     → définit les permissions (quoi faire sur quoi)
RoleBinding / ClusterRoleBinding → attribue les permissions (à qui)

Subject (qui) :
  ├── User           — humain authentifié (cert, OIDC)
  ├── Group          — ensemble d'utilisateurs
  └── ServiceAccount — identité pour les pods

Verbs (actions) :
  get, list, watch, create, update, patch, delete, exec

Role       = permissions dans un namespace
ClusterRole = permissions cluster-wide (ou réutilisable dans tous les namespaces)
```

## Role + RoleBinding (namespace-scoped)

```yaml
# Role : lecture seule sur les pods et logs dans "production"
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
---
# RoleBinding : attribue le Role à un ServiceAccount
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: production
subjects:
  - kind: ServiceAccount
    name: monitoring-agent
    namespace: monitoring
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

## ClusterRole + ClusterRoleBinding (cluster-wide)

```yaml
# ClusterRole : accès en lecture à tous les nodes
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-reader
rules:
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["metrics.k8s.io"]
    resources: ["nodes", "pods"]
    verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: metrics-server-binding
subjects:
  - kind: ServiceAccount
    name: metrics-server
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: node-reader
  apiGroup: rbac.authorization.k8s.io
```

## ServiceAccount pour un pod applicatif

```yaml
# 1. Créer le ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: production
---
# 2. Role minimal (lire sa propre ConfigMap)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-config-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get"]
    resourceNames: ["app-config"]   # resource spécifique uniquement
---
# 3. Binding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-reads-config
  namespace: production
subjects:
  - kind: ServiceAccount
    name: app-sa
roleRef:
  kind: Role
  name: app-config-reader
  apiGroup: rbac.authorization.k8s.io
---
# 4. Pod utilisant ce ServiceAccount
apiVersion: v1
kind: Pod
spec:
  serviceAccountName: app-sa
  containers:
    - name: app
      image: myapp:1.0
```

## Vérifier les permissions

```bash
# Est-ce que je peux faire X ?
kubectl auth can-i get pods -n production
kubectl auth can-i create deployments -n production
kubectl auth can-i delete secrets --as system:serviceaccount:production:app-sa

# Lister toutes les permissions d'un subject
kubectl auth can-i --list --as system:serviceaccount:production:app-sa -n production

# Voir les roles et bindings
kubectl get roles,rolebindings -n production
kubectl describe rolebinding read-pods -n production
```

## Roles built-in utiles

| ClusterRole | Droits | Usage |
|-------------|--------|-------|
| `view` | Lecture seule namespace | Monitoring léger |
| `edit` | CRUD sur les workloads | Développeurs |
| `admin` | Tout dans le namespace | Admin namespace |
| `cluster-admin` | Tout le cluster | Super admin (à éviter) |

## Explorer

- **[[Secrets]]** — protection des secrets via RBAC par resourceNames
- **[[Service accounts]]** — identités pour les pods, token de service
- **[[Advanced Kubernetes]]** — Admission Controllers, NetworkPolicies
- **[[IAM]]** — RBAC cloud (AWS/Azure), IRSA pour EKS
