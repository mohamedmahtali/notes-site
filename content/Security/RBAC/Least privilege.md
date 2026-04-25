---
title: Least privilege
tags:
  - security
  - intermediate
---

# Least privilege (Moindre privilège)

## Définition

Le principe de moindre privilège stipule qu'un utilisateur, processus ou service ne doit avoir que les permissions minimales nécessaires pour accomplir sa tâche, rien de plus.

> [!tip] Pourquoi c'est important
> Le moindre privilège limite le blast radius en cas de compromission. Un service compromis avec des droits minimaux fait moins de dégâts qu'un service avec des droits admin.

## Anti-patterns à éviter

```yaml
# ❌ Trop permissif
rules:
  - apiGroups: ["*"]
    resources: ["*"]
    verbs: ["*"]

# ✓ Minimal et précis
rules:
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list"]
    resourceNames: ["myapp"]  # Limiter à une ressource spécifique
```

## Audit des permissions excessives

```bash
# Qui a des droits cluster-admin ?
kubectl get clusterrolebindings -o json   | jq '.items[] | select(.roleRef.name == "cluster-admin") | .subjects'

# Raku (outil d'audit RBAC)
raku --k8s

# rbac-tool
kubectl rbac-tool who-can create pods
```

## AWS : politique de moindre privilège

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject"],
  "Resource": "arn:aws:s3:::my-bucket/my-prefix/*"
}
```

## Liens

- [[RBAC]]
- [[Roles]]
- [[Permissions]]
- [[Zero trust]]
