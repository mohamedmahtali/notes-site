---
title: Terraform providers
tags:
  - beginner
---
# Terraform providers

---

## Définition

Les providers sont des plugins [[Terraform]] qui gèrent les interactions avec les APIs de [[Services]] externes ([[AWS]], GCP, [[Azure]], [[Kubernetes]], GitHub, etc.). Chaque ressource appartient à un provider.

---

## Configuration

```hcl
# versions.tf — contraintes de version
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"    # >= 5.0, < 6.0
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

# providers.tf — configuration
provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      ManagedBy   = "terraform"
      Environment = var.environment
    }
  }
}
```

---

```bash
# Télécharger les providers
terraform init

# Voir les providers installés
terraform providers

# Mettre à jour les providers
terraform init -upgrade
```
