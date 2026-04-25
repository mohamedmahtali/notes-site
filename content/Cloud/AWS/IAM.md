---
title: IAM
tags:
  - intermediate
---
# IAM

---

## Définition

[[AWS]] IAM (Identity and Access Management) contrôle qui peut faire quoi sur quelles ressources AWS. Il gère les utilisateurs, groupes, rôles, et les politiques de [[Permissions]] JSON.

---

## Concepts clés

```
User   → identité permanente d'un humain
Group  → collection d'utilisateurs avec les mêmes permissions
Role   → identité assumable par des services/EC2/Lambda
Policy → document JSON définissant les permissions
```

---

## Commandes

```bash
# Créer un utilisateur
aws iam create-user --user-name alice

# Attacher une politique
aws iam attach-user-policy   --user-name alice   --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

# Créer un rôle pour EC2
aws iam create-role   --role-name EC2-S3-ReadOnly   --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}'

# Lister les utilisateurs
aws iam list-users --output table
```

---

## Politique JSON

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-bucket/*"
    },
    {
      "Effect": "Deny",
      "Action": "s3:DeleteObject",
      "Resource": "*"
    }
  ]
}
```

---

> [!warning]
> Ne jamais utiliser le compte root AWS pour les opérations quotidiennes. Créer des [[Users]] IAM avec le principe du moindre privilège. Activer MFA sur tous les comptes.
