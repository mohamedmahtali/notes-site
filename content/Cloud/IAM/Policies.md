---
title: Policies
tags:
  - intermediate
---
# Policies

---

## Définition

Les politiques [[IAM]] sont des documents JSON qui définissent les [[Permissions]]. Elles spécifient quelles actions (Effect: Allow/Deny), sur quelles ressources (Resource), sous quelles [[Conditions]] (Condition).

---

## Structure d'une politique AWS

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadWrite",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ]
    },
    {
      "Sid": "DenyDeleteOnProd",
      "Effect": "Deny",
      "Action": "s3:DeleteObject",
      "Resource": "arn:aws:s3:::production-bucket/*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalTag/Environment": "admin"
        }
      }
    }
  ]
}
```

---

## Types de politiques

| Type | Description |
|---|---|
| [[AWS]] managed | Politiques prédéfinies AWS (ReadOnlyAccess, etc.) |
| Customer managed | Politiques personnalisées |
| Inline | Attachées directement à une identité |
| Resource-based | Attachées à la ressource (S3 bucket policy) |

---

> [!tip]
> Utiliser l'AWS Policy Simulator pour tester les politiques avant de les déployer. `aws iam simulate-principal-policy` permet de vérifier ce qu'une identité peut faire.
