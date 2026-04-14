---
title: Roles
tags: [security, intermediate]
---

# Roles

## Définition

Un rôle est un ensemble nommé de permissions. Dans Kubernetes, il en existe deux types : `Role` (namespace-scoped) et `ClusterRole` (cluster-wide). Dans AWS IAM, les rôles peuvent être assumés par des services ou utilisateurs.

> [!note] Role vs ClusterRole
> Un `Role` ne s'applique qu'à un namespace. Un `ClusterRole` s'applique à tout le cluster (ou peut être bindé à un namespace via RoleBinding).

## Kubernetes : ClusterRole

```yaml
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
```

## Roles prédéfinis Kubernetes

```bash
# Lister les ClusterRoles prédéfinis
kubectl get clusterroles | grep -v system:

# Rôles courants
cluster-admin    # Admin total (à éviter)
admin            # Admin namespace
edit             # Lecture/écriture namespace
view             # Lecture seule namespace
```

## AWS IAM Role

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "ec2.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}
```

## Liens

- [[RBAC]]
- [[Permissions]]
- [[Least privilege]]
