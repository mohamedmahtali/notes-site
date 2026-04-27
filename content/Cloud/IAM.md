---
title: IAM
tags:
  - intermediate
---
# IAM

## Définition

IAM (Identity and Access Management) est le système de contrôle d'accès du [[Cloud]]. Il définit **qui** peut faire **quoi** sur **quelles ressources**. Commun à [[AWS]], GCP et [[Azure]] sous des formes similaires.

> [!warning] Least privilege
> Le compte root/admin initial doit être sécurisé avec MFA et jamais utilisé au quotidien. Toujours créer des identités dédiées avec le minimum de [[Permissions]] nécessaires.

## Modèle : identité → policy → ressource

```
Identity (qui ?)
  ├── User          — personne physique avec credentials
  ├── Group         — ensemble d'users partageant les mêmes droits
  ├── Role          — identité pour un service ou une application
  └── Federated     — SSO, OIDC, SAML (login via Google, GitHub...)

Policy (quoi ?)
  └── JSON décrivant les actions autorisées ou refusées sur des ressources

Binding
  └── Attacher une policy à une identity
```

## AWS — Exemple de policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-app-bucket/*"
    },
    {
      "Effect": "Deny",
      "Action": "s3:DeleteObject",
      "Resource": "*"
    }
  ]
}
```

Règle : commencer par le **minimum**, puis élargir. Jamais `"Action": "*"` en production.

## Roles pour les services (sans credentials statiques)

```
EC2 → Instance Profile (role attaché à l'instance)
Lambda → Execution Role (role attaché à la fonction)
Kubernetes (EKS) → IRSA — IAM Roles for Service Accounts
  └── Un pod = une identité IAM via annotation sur ServiceAccount

# Exemple IRSA
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789:role/my-app-role
```

Avantage : les services n'ont jamais de clés API statiques dans leur code ou leur config.

## Comparaison AWS / GCP / Azure

| Concept | AWS | GCP | Azure |
|---------|-----|-----|-------|
| Identité service | IAM Role | Service Account | Managed Identity |
| Politique | IAM Policy (JSON) | IAM Policy | Azure Policy + RBAC |
| Gestion utilisateurs | IAM Users | Google Workspace | Azure AD / Entra ID |
| CLI de gestion | `aws iam` | `gcloud iam` | `az role` |

## Bonnes pratiques

| Pratique | Description |
|----------|-------------|
| MFA sur root | Obligatoire, jamais utilisé au quotidien |
| Rôles plutôt que clés | Pas de credentials statiques pour les services |
| Policy conditions | Limiter par IP, heure, région, tag |
| Audit régulier | Supprimer les accès inutilisés (`aws iam get-credential-report`) |
| SCPs (AWS) | Barrières au niveau organisation, pas de bypass possible |

## Explorer

- **[[Permissions]]** — modèle ARN, wildcards, conditions
- **[[RBAC]]** — contrôle d'accès basé sur les rôles (Kubernetes RBAC lié)
- **[[AWS]]** — IAM dans le contexte AWS complet
