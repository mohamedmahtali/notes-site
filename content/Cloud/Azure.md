---
title: Azure
tags:
  - intermediate
---
# Azure

---

## Définition

Microsoft Azure est le deuxième [[Cloud]] provider mondial, particulièrement présent dans les entreprises grâce à son intégration avec les produits Microsoft (Active Directory, Office 365, Windows Server).

---

## Services fondamentaux

| Catégorie | [[AWS]] équivalent | Azure |
|---|---|---|
| VM | [[EC2]] | [[Virtual Machines]] |
| K8s | [[EKS]] | [[AKS]] |
| Serverless | Lambda | Azure [[Functions]] |
| [[Object storage]] | S3 | [[Blob Storage]] |
| [[IAM]] | IAM | Azure Active Directory |
| BDD | RDS | Azure SQL Database |

---

## Configuration CLI

```bash
# Installer az CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Connexion
az login
az account set --subscription "My Subscription"

# Vérifier
az account show
az group list --output table
```
