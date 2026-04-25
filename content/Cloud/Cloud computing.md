---
title: Cloud computing
tags:
  - beginner
---
# Cloud computing

---

## Définition

Le [[Cloud]] computing est la fourniture de ressources informatiques (serveurs, stockage, bases de données, réseau) via internet à la demande, avec facturation à l'usage. Les grands providers : [[AWS]], GCP, [[Azure]].

---

## Modèles de service

| Modèle | Géré par le provider | Exemple |
|---|---|---|
| [[IaaS]] | Infra physique, réseau, virtualisation | [[EC2]], GCE, Azure VMs |
| [[PaaS]] | + OS, runtime, middleware | App Engine, Heroku |
| [[SaaS]] | Tout | Gmail, Salesforce, GitHub |

---

## Pourquoi c'est important

> [!tip] Payer ce qu'on utilise
> Le cloud élimine l'investissement initial en matériel (CapEx) et le remplace par des coûts opérationnels [[Variables]] (OpEx). Une startup peut démarrer avec un seul serveur et scaler à des milliers en quelques minutes.

---

## Commandes essentielles

```bash
# AWS CLI
aws configure
aws ec2 describe-instances
aws s3 ls s3://my-bucket

# GCP
gcloud config set project my-project
gcloud compute instances list

# Azure
az login
az vm list --output table
```
