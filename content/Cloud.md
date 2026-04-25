---
title: Cloud
tags:
  - cloud
  - beginner
---

# Cloud

## Définition

Le cloud computing est la fourniture de ressources informatiques (serveurs, stockage, bases de données, réseau, logiciels) à la demande via Internet, avec facturation à l'usage. Les trois grands providers sont **AWS**, **Google Cloud** et **Azure**.

> [!tip] Pourquoi c'est important
> Le cloud a transformé l'infrastructure IT : plus de serveurs physiques à gérer, des ressources infiniment scalables en quelques secondes, et un modèle pay-as-you-go qui réduit le CAPEX. Aujourd'hui, la quasi-totalité des architectures modernes repose sur le cloud.

## Modèles de service

| Modèle | Tu gères | Le provider gère | Exemples |
|--------|----------|------------------|----------|
| [[IaaS]] | OS, runtime, app | Hardware, réseau | [[EC2]], GCE, Azure VM |
| [[PaaS]] | App, données | OS, runtime, infra | App Engine, Heroku |
| [[SaaS]] | Rien (utilisation) | Tout | Gmail, Slack, Notion |

## Modèles de déploiement

- **Public cloud** — infrastructure partagée, gérée par le provider (AWS, GCP, Azure)
- **Private cloud** — infrastructure dédiée, on-premise ou hébergée
- **Hybrid cloud** — combinaison public + private avec interconnexion

## Composants fondamentaux

- **Compute** — [[Virtual machines]], conteneurs, fonctions serverless
- **Réseau** — [[VPC]], [[Subnets]], [[Load balancers]], [[Security groups]]
- **Stockage** — [[Object storage]], block storage, file storage
- **Identité** — [[IAM]] (gestion des accès et [[Permissions]])
- **Scalabilité** — [[Autoscaling]], [[Load balancing]]

## Providers

- [[AWS]] — Amazon Web [[Services]], leader du marché (EC2, S3, RDS, [[EKS]]...)
- [[Azure]] — Microsoft Azure, fort ancrage enterprise ([[AKS]], Blob, AD...)
- [[Google Cloud]] — GCP, excellence en data/ML ([[GKE]], BigQuery, Cloud Run...)

## Liens

- [[Cloud computing]]
- [[IaaS]]
- [[PaaS]]
- [[SaaS]]
- [[Virtual machines]]
- [[AWS]]
- [[Azure]]
- [[Google Cloud]]
- [[VPC]]
- [[Subnets]]
- [[Security groups]]
- [[Load balancers]]
- [[Object storage]]
- [[IAM]]
- [[Autoscaling]]
