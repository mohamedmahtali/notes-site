---
title: Azure
tags:
  - intermediate
---
# Azure

## Définition

Microsoft Azure est le deuxième [[Cloud]] provider mondial, particulièrement présent dans les entreprises grâce à son intégration avec les produits Microsoft (Active Directory, Office 365, Windows Server). Il couvre compute, réseau, stockage, identité, et services managés (Kubernetes, BDD, ML).

## Services fondamentaux

| Catégorie | AWS équivalent | Azure | Description |
|---|---|---|---|
| VM | [[EC2]] | [[Virtual Machines]] | Machines virtuelles |
| Kubernetes | [[EKS]] | AKS | Kubernetes managé |
| Serverless | Lambda | Azure Functions | Fonctions event-driven |
| Object storage | S3 | Blob Storage | Stockage objets |
| IAM | [[IAM]] | Azure AD / Entra ID | Identité et accès |
| BDD relationnelle | RDS | Azure SQL Database | PostgreSQL/MySQL/SQL Server managés |
| Réseau | [[VPC]] | VNet | Réseau virtuel privé |
| DNS | Route 53 | Azure DNS | Gestion DNS |
| CDN | CloudFront | Azure CDN | Distribution de contenu |

## Organisation des ressources

Azure structure les ressources en 4 niveaux :

```
Tenant (Azure AD)
└── Management Group (optionnel, gouvernance multi-subs)
    └── Subscription (unité de facturation et périmètre)
        └── Resource Group (conteneur logique de ressources)
            └── Ressources (VMs, BDD, réseaux...)
```

Toute ressource appartient à exactement un Resource Group. Le RG est aussi l'unité de déploiement (ARM templates, Bicep) et de contrôle d'accès (RBAC).

## Identité et accès (Azure AD / Entra ID)

Azure utilise le RBAC pour contrôler l'accès aux ressources :

```
Principal (qui ?)
  ├── User         — compte humain
  ├── Group        — ensemble d'users
  ├── Service Principal — identité applicative (équivalent IAM Role)
  └── Managed Identity  — identité sans credentials pour les services Azure

Role Assignment = Principal + Role + Scope
  Scope : Management Group > Subscription > Resource Group > Resource
```

```bash
# Assigner un rôle à un Service Principal
az role assignment create \
  --assignee <sp-client-id> \
  --role "Contributor" \
  --scope /subscriptions/<sub-id>/resourceGroups/my-rg
```

Roles built-in clés : Owner, Contributor, Reader, User Access Administrator.

## AKS — Kubernetes managé

```bash
# Créer un cluster AKS
az aks create \
  --resource-group my-rg \
  --name my-cluster \
  --node-count 3 \
  --node-vm-size Standard_D2s_v3 \
  --enable-managed-identity \
  --enable-addons monitoring

# Récupérer le kubeconfig
az aks get-credentials --resource-group my-rg --name my-cluster

# Scaler le node pool
az aks scale --resource-group my-rg --name my-cluster --node-count 5
```

## Configuration CLI

```bash
# Installer az CLI (Debian/Ubuntu)
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Connexion interactive
az login
az account set --subscription "My Subscription"

# Vérifier le contexte actif
az account show
az group list --output table

# Créer un Resource Group
az group create --name my-rg --location westeurope
```

## Régions et disponibilité

```
Region (ex: West Europe = Amsterdam)
└── Availability Zones (AZ1, AZ2, AZ3)
    └── Data centers physiques distincts

→ Déployer multi-AZ pour la haute disponibilité
→ Utiliser des Availability Sets pour les VMs sans AZ
```

Régions clés Europe : West Europe (Amsterdam), North Europe (Dublin), France Central (Paris).

## Explorer

- **[[Virtual Machines]]** — VMs Azure, tailles, disques managés
- **[[IAM]]** — RBAC Azure, Managed Identities, Azure AD
- **[[VPC]]** — VNet Azure, subnets, NSGs
- **[[AWS]]** — comparaison avec le leader du marché
