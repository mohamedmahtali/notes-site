---
title: Users
tags:
  - beginner
---
# Users

---

## Définition

Les [[IAM]] users sont des identités permanentes associées à des personnes (ou des applications qui ont besoin d'accès long-terme). Ils ont des credentials (mot de passe, access keys) et des [[Permissions]] via des politiques attachées.

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
> En production, préférer les **rôles IAM** aux users IAM pour les [[Services]] et applications. Les rôles utilisent des credentials temporaires (STS) — plus sécurisés que les access keys longue durée qui peuvent être leakées.

## Bonnes pratiques

```bash
# Activer MFA sur un user
aws iam enable-mfa-device \
  --user-name alice \
  --serial-number arn:aws:iam::ACCOUNT:mfa/alice \
  --authentication-code1 123456 \
  --authentication-code2 789012

# Auditer les access keys (trouver les clés non utilisées)
aws iam generate-credential-report
aws iam get-credential-report --query 'Content' --output text | base64 -d

# Désactiver une clé compromise immédiatement
aws iam update-access-key \
  --user-name alice \
  --access-key-id AKIAIOSFODNN7EXAMPLE \
  --status Inactive

# Supprimer une clé
aws iam delete-access-key \
  --user-name alice \
  --access-key-id AKIAIOSFODNN7EXAMPLE
```

## Règles d'or

| Règle | Pourquoi |
|-------|---------|
| Pas d'access keys sur le compte root | La clé root a des droits illimités |
| MFA obligatoire pour la console | Protège contre le vol de mot de passe |
| Rotation des access keys tous les 90j | Limite la fenêtre d'exploitation |
| Pas d'access keys pour les services [[AWS]] | Utiliser les rôles IAM + instance profile |
| Principe du moindre privilège | Une clé compromise = dommages limités |
