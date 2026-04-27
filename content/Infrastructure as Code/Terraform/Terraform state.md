---
title: Terraform state
tags:
  - intermediate
---
# Terraform state

## Définition

Le state Terraform est un fichier JSON (`terraform.tfstate`) qui mappe les ressources définies dans le code HCL aux ressources réelles dans le [[Cloud]]. C'est la source de vérité de Terraform — il sait ce qu'il gère, leur ID, et leur état actuel.

> [!warning] Le state est critique
> Perte du state = Terraform pense que toutes les ressources n'existent pas encore et veut tout recréer. Toujours stocker le state à distance en production. Ne jamais le modifier manuellement.

## Rôle dans le cycle plan/apply

```
Code HCL          State actuel         Cloud réel
(ce qu'on veut)   (ce que TF sait)     (ce qui existe)
      │                  │                    │
      └──── terraform plan ────────────────────┘
                         │
                  Diff = ce qui va changer
                         │
              terraform apply → exécute le diff
                         │
                  State mis à jour
```

Sans state, `terraform plan` devrait interroger l'API du cloud provider pour chaque ressource — lent et impossible à l'échelle.

## Backend distant (production)

En production, le state doit être distant et versionné. Exemple AWS :

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-tfstate-bucket"
    key            = "prod/terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true

    # DynamoDB pour le locking (évite les apply concurrents)
    dynamodb_table = "terraform-state-lock"
  }
}
```

```bash
# Initialiser avec le nouveau backend
terraform init -migrate-state
```

Équivalents sur GCP et Azure :

```hcl
# GCS
backend "gcs" {
  bucket = "my-tfstate-bucket"
  prefix = "prod"
}

# Azure Blob
backend "azurerm" {
  resource_group_name  = "tfstate-rg"
  storage_account_name = "tfstate"
  container_name       = "tfstate"
  key                  = "prod.tfstate"
}
```

## Commandes state

```bash
# Inspecter
terraform state list                          # toutes les ressources
terraform state show aws_instance.web         # détails d'une ressource

# Modifier (sans détruire la ressource réelle)
terraform state mv aws_instance.web aws_instance.webserver   # renommer
terraform state rm aws_instance.web                          # exclure du state

# Importer une ressource créée manuellement
terraform import aws_instance.existing i-1234567890abcdef0

# Détecter les dérives (cloud vs state)
terraform refresh     # ancienne méthode
terraform plan        # inclut la détection de drift depuis TF 0.15+
```

## Bonnes pratiques

| Pratique | Pourquoi |
|----------|----------|
| Backend distant (S3, GCS) | Partage équipe, survie aux machines locales |
| Locking (DynamoDB) | Évite la corruption par applies concurrents |
| Versioning S3 activé | Rollback en cas de state corrompu |
| `terraform.tfstate` dans `.gitignore` | Le state peut contenir des secrets |
| State par environnement | `prod/terraform.tfstate` ≠ `staging/terraform.tfstate` |

## Explorer

- **[[Remote state]]** — configuration S3/GCS/Azure, partage inter-équipes
- **[[State locking]]** — DynamoDB, prévention des conflits concurrents
- **[[Drift]]** — détecter et corriger les dérives entre state et cloud réel
- **[[Local state]]** — state local en développement uniquement
