---
title: Permissions
tags: [security, intermediate]
---

# Permissions

## Définition

Les permissions définissent les actions autorisées sur des ressources. Dans Kubernetes, elles sont exprimées comme des verbs (get, list, create...) sur des resources (pods, deployments...) dans des apiGroups.

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

## Liens

- [[RBAC]]
- [[Roles]]
- [[Least privilege]]
