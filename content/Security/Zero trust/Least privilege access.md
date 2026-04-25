---
title: Least privilege access
tags:
  - security
  - intermediate
---

# Least privilege access

## Définition

Dans le contexte Zero Trust, le least privilege access étend le principe de moindre privilège avec le concept de Just-In-Time (JIT) : les accès sont accordés temporairement, à la demande, pour une tâche spécifique.

> [!tip] JIT vs accès permanent
> Plutôt qu'un accès permanent à la production, les ingénieurs demandent un accès temporaire (1h) pour une tâche précise. Cela réduit la fenêtre d'exposition des credentials permanents.

## Accès JIT avec Vault

```bash
# L'ingénieur demande un accès temporaire
vault write aws/creds/prod-readonly ttl=1h

# → Credentials AWS temporaires valides 1h
# → Révoqués automatiquement
# → Tracés dans les audit logs Vault
```

## Accès JIT Kubernetes

```bash
# Créer un RoleBinding temporaire (kubectl)
kubectl create rolebinding temp-access   --clusterrole=view   --user=alice   --namespace=production

# Supprimer après X minutes (script)
sleep 3600 && kubectl delete rolebinding temp-access -n production &
```

## Politique d'accès production

```
1. Pas d'accès permanent à la production
2. Approbation manager requise
3. Durée limitée (1-4h)
4. Logging de toutes les actions
5. Revue post-incident des accès
```

## Liens

- [[Zero trust]]
- [[Assume breach]]
- [[Verify explicitly]]
- [[RBAC]]
- [[Least privilege]]
