---
title: Users
tags:
  - beginner
---
# Users

## Parent
- [[IAM]]

---

## Définition

Les IAM users sont des identités permanentes associées à des personnes (ou des applications qui ont besoin d'accès long-terme). Ils ont des credentials (mot de passe, access keys) et des permissions via des politiques attachées.

---

## AWS — gestion des users

```bash
# Créer un user
aws iam create-user --user-name alice

# Créer des access keys (pour CLI/API)
aws iam create-access-key --user-name alice

# Attacher une politique
aws iam attach-user-policy   --user-name alice   --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

# Ajouter à un groupe
aws iam add-user-to-group --user-name alice --group-name developers

# Voir les permissions effectives
aws iam simulate-principal-policy   --policy-source-arn arn:aws:iam::ACCOUNT:user/alice   --action-names s3:PutObject   --resource-arns arn:aws:s3:::my-bucket/*
```

---

> [!warning]
> En production, préférer les **rôles IAM** aux users IAM pour les services et applications. Les rôles utilisent des credentials temporaires (STS) — plus sécurisés que les access keys longue durée qui peuvent être leakées.
