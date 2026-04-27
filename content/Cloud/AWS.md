---
title: AWS
tags:
  - intermediate
---
# AWS

## Définition

Amazon Web Services (AWS) est le leader mondial du [[Cloud]] avec plus de 200 services. Lancé en 2006, il couvre compute, stockage, bases de données, réseau, ML, et IoT. AWS détient ~32% du marché cloud mondial (2024).

## Services fondamentaux

| Catégorie | Service | Description |
|---|---|---|
| Compute | [[EC2]] | Machines virtuelles |
| Compute | Lambda | Fonctions serverless |
| Stockage | S3 | [[Object storage]] |
| Stockage | EBS | Block storage pour EC2 |
| BDD | RDS | PostgreSQL/MySQL/Oracle managés |
| BDD | DynamoDB | NoSQL clé-valeur serverless |
| Réseau | [[VPC]] | Réseau privé virtuel |
| IAM | [[IAM]] | Identité et accès |
| Container | EKS | [[Kubernetes]] managé |
| Container | ECR | Registry Docker privé |
| Monitoring | CloudWatch | Logs, métriques, alertes |

## Régions et Availability Zones

```
Region (ex: eu-west-1 = Irlande)
└── AZ a (eu-west-1a) — data center physique 1
└── AZ b (eu-west-1b) — data center physique 2
└── AZ c (eu-west-1c) — data center physique 3

→ Déployer sur 2+ AZs = haute disponibilité
→ Déployer sur 2+ régions = disaster recovery
```

Régions Europe clés : `eu-west-1` (Irlande), `eu-west-3` (Paris), `eu-central-1` (Frankfurt).

## Modèles de facturation

| Modèle | Usage | Économies |
|--------|-------|-----------|
| On-Demand | Workloads imprévisibles | Référence (0%) |
| Reserved (1 ou 3 ans) | Workloads stables | ~40-60% |
| Spot Instances | Tolérant aux interruptions | ~70-90% |
| Savings Plans | Engagement usage horaire | ~30-50% |

Règle : production stable → Reserved, CI/CD/batch → Spot, tout le reste → On-Demand.

## Configuration CLI

```bash
# Installer
pip install awscli
# ou : brew install awscli / apt install awscli

# Configurer (credentials + région par défaut)
aws configure
# AWS Access Key ID: ...
# AWS Secret Access Key: ...
# Default region name: eu-west-1
# Default output format: json

# Vérifier l'identité
aws sts get-caller-identity

# Profils multiples (dev/prod)
aws configure --profile prod
aws ec2 describe-instances --profile prod
```

## Commandes utiles multi-services

```bash
# Lister les instances EC2 running
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,PublicIpAddress]' \
  --output table

# Lister les buckets S3
aws s3 ls

# Vérifier les coûts du mois en cours
aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-01-31 \
  --granularity MONTHLY \
  --metrics BlendedCost

# Chercher dans les logs CloudWatch
aws logs filter-log-events \
  --log-group-name /app/production \
  --filter-pattern "ERROR"
```

## Bonnes pratiques

| Pratique | Pourquoi |
|----------|----------|
| MFA sur root + comptes IAM | Premier vecteur de compromission |
| Rôles IAM pour les services | Pas de clés statiques sur les instances |
| Activer CloudTrail | Audit de toutes les actions API |
| Budget alerts | Éviter les surprises de facturation |
| Tags sur toutes les ressources | Imputation des coûts, gouvernance |

## Explorer

- **[[EC2]]** — instances, familles, Spot, EBS
- **[[IAM]]** — policies, rôles, IRSA pour EKS
- **[[VPC]]** — subnets, security groups, NAT gateway
- **[[S3]]** — stockage objets, versioning, lifecycle
- **[[EKS]]** — Kubernetes managé sur AWS
