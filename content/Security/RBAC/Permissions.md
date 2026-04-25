---
title: Permissions
tags:
  - security
  - intermediate
---

# Permissions

## Définition

Les permissions définissent les actions autorisées sur des ressources. Dans [[Kubernetes]], elles sont exprimées comme des verbs ([[get]], list, [[create]]...) sur des resources ([[Pods]], [[Deployments]]...) dans des apiGroups.

> [!tip] Principe de moindre privilège
> N'accorder que les permissions strictement nécessaires. "list" et "watch" suffisent souvent là où "create" et "delete" sont inutiles.

## Verbs Kubernetes

| Verb | Action |
|------|--------|
| `get` | Lire une ressource par nom |
| `list` | Lister les ressources |
| `watch` | Observer les changements |
| `create` | Créer une ressource |
| `update` | Mettre à jour |
| `patch` | Modifier partiellement |
| `delete` | Supprimer |
| `deletecollection` | Supprimer en masse |

## Vérifier les permissions

```bash
# Peut-on faire une action ?
kubectl auth can-i create pods
kubectl auth can-i delete deployments -n production

# Vérifier pour un autre utilisateur
kubectl auth can-i list secrets --as=alice

# Lister toutes les permissions d'un service account
kubectl auth can-i --list --as=system:serviceaccount:default:myapp
```

## Exemples de Roles Kubernetes

```yaml
# Role lecture seule sur les pods (namespace-scoped)
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
# ClusterRole — accès en lecture sur tout le cluster
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-reader
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps", "nodes"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments", "replicasets", "daemonsets"]
  verbs: ["get", "list", "watch"]

---
# RoleBinding — associer le Role à un ServiceAccount
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
  namespace: production
subjects:
- kind: ServiceAccount
  name: myapp
  namespace: production
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

## Debug RBAC

```bash
# Vérifier si une action est autorisée
kubectl auth can-i create pods -n production
kubectl auth can-i delete deployments -n production --as=alice

# Lister toutes les permissions d'un ServiceAccount
kubectl auth can-i --list \
  --as=system:serviceaccount:production:myapp \
  -n production

# Voir les RoleBindings qui donnent accès à un namespace
kubectl get rolebindings,clusterrolebindings \
  -n production \
  -o custom-columns='NAME:.metadata.name,ROLE:.roleRef.name,SUBJECTS:.subjects[*].name'

# Audit : qui peut créer des pods dans production ?
kubectl who-can create pods -n production   # nécessite le plugin kubectl-whocan
```

## Liens

- [[RBAC]]
- [[Roles]]
- [[Least privilege]]
