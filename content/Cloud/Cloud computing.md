---
title: Cloud computing
tags:
  - beginner
---
# Cloud computing

## Définition

Le Cloud computing est la fourniture de ressources informatiques (serveurs, stockage, bases de données, réseau) via internet à la demande, avec facturation à l'usage. Les trois grands providers : [[AWS]], GCP, [[Azure]].

## Modèles de service

| Modèle | Provider gère | Client gère | Exemple |
|---|---|---|---|
| [[IaaS]] | Infra physique, réseau, virtualisation | OS, runtime, apps | [[EC2]], GCE, Azure VMs |
| [[PaaS]] | + OS, runtime, middleware | Code, données | App Engine, Heroku, Azure App Service |
| [[SaaS]] | Tout | Paramétrage, données | Gmail, Salesforce, GitHub |

Plus on monte vers SaaS, moins on gère — mais moins on contrôle.

## 5 caractéristiques essentielles (NIST)

```
1. On-demand self-service    — ressources disponibles sans intervention humaine
2. Broad network access      — accessible depuis n'importe où via internet
3. Resource pooling          — ressources mutualisées entre clients (multi-tenant)
4. Rapid elasticity          — scale up/down en minutes (ou secondes)
5. Measured service          — facturation à l'usage réel
```

## CapEx vs OpEx

```
Avant (On-Premise)              Avec le Cloud
──────────────────────          ──────────────────────
Acheter des serveurs (CapEx)    Louer à l'usage (OpEx)
Provisionner pour le pic        Scaler selon la demande
Capacité fixe                   Capacité élastique
3-6 mois pour déployer          Minutes pour déployer
Amortissement sur 3-5 ans       Coût immédiat, ajustable
```

Le cloud convertit un investissement (CapEx) en coût opérationnel (OpEx). Avantage pour les startups : démarrer petit, payer ce qu'on consomme.

## Modèles de déploiement

| Modèle | Description | Cas d'usage |
|--------|-------------|-------------|
| Public cloud | Infrastructure partagée chez AWS/GCP/Azure | Startups, scale-ups |
| Private cloud | Infrastructure dédiée (on-premise ou hébergée) | Régulations strictes, données sensibles |
| Hybrid cloud | Mix public + private reliés | Migration progressive, burst capacity |
| Multi-cloud | Plusieurs providers publics | Éviter le vendor lock-in, redondance |

## Shared Responsibility Model

```
Provider est responsable de :    Client est responsable de :
─────────────────────────────    ─────────────────────────
Sécurité de l'infrastructure     Sécurité dans le cloud
Hyperviseur, réseau physique     OS, applications, données
Disponibilité des services       IAM, chiffrement, firewall
Conformité de la plateforme      Conformité des données
```

[[AWS]] appelle ça "security OF the cloud vs security IN the cloud".

## CLI des trois providers

```bash
# AWS
aws configure
aws ec2 describe-instances
aws s3 ls s3://my-bucket

# GCP
gcloud config set project my-project
gcloud compute instances list
gcloud container clusters get-credentials my-cluster

# Azure
az login
az vm list --output table
az aks get-credentials --resource-group my-rg --name my-cluster
```

## Explorer

- **[[AWS]]** — leader mondial, EC2, S3, EKS, IAM
- **[[Azure]]** — intégration Microsoft, AKS, Entra ID
- **[[IaaS]]** — infrastructure as a service, contrôle maximal
- **[[PaaS]]** — platform as a service, focus sur le code
- **[[VPC]]** — réseau privé virtuel dans le cloud
