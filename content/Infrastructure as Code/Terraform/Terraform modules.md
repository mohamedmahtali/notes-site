---
title: Terraform modules
tags:
  - intermediate
---
# Terraform modules

---

## Définition

Les [[Modules]] [[Terraform]] sont des groupes de ressources réutilisables encapsulées dans un répertoire. Ils permettent de factoriser l'infrastructure commune ([[VPC]], [[EKS]] [[Cluster]], RDS) et de la partager entre projets.

---

## Pourquoi c'est important

> [!tip] DRY pour l'infrastructure
> Sans modules, dupliquer la config VPC pour chaque environnement. Avec modules : définir le VPC une fois, l'instancier plusieurs fois avec des paramètres différents.

---

## Utiliser un module

```hcl
# Module local
module "vpc" {
  source = "./modules/vpc"

  cidr_block   = "10.0.0.0/16"
  environment  = var.environment
  azs          = ["eu-west-1a", "eu-west-1b"]
}

# Module Terraform Registry
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "my-cluster"
  cluster_version = "1.29"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnets
}

# Outputs du module
output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}
```

---

```bash
# Télécharger les modules
terraform init

# Voir les modules utilisés
terraform providers
```
