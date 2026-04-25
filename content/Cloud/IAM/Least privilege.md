---
title: Least privilege
tags:
  - intermediate
---
# Least privilege

---

## Définition

Le principe du moindre privilège stipule qu'une identité ne doit avoir accès qu'aux ressources et actions strictement nécessaires à sa fonction. Ni plus, ni moins.

---

## Pourquoi c'est important

> [!warning] Les [[Permissions]] excessives = surface d'attaque
> Si un service compromis a des droits admin, l'attaquant a des droits admin. Si le service a seulement `s3:GetObject` sur un bucket spécifique, l'impact est limité. Le moindre privilège contient le blast radius d'une compromission.

---

## En pratique AWS

```bash
# Mauvais — trop permissif
{
  "Action": "*",
  "Resource": "*",
  "Effect": "Allow"
}

# Bon — permissions précises
{
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::my-specific-bucket/uploads/*",
  "Effect": "Allow"
}
```

---

## Outils d'analyse

```bash
# AWS IAM Access Analyzer — détecte les accès excessifs
aws accessanalyzer create-analyzer   --analyzer-name my-analyzer   --type ACCOUNT

# IAM Access Advisor — voir les derniers accès
aws iam generate-service-last-accessed-details --arn arn:aws:iam::ACCOUNT:role/MyRole
```

---

> [!tip]
> Commencer avec des permissions larges en développement, puis les restreindre en utilisant les logs CloudTrail pour voir ce qui est réellement utilisé. Ne garder que les actions qui apparaissent dans les logs.
