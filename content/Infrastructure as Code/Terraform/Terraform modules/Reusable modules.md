---
title: Reusable modules
tags:
  - intermediate
---
# Reusable modules

## Parent
- [[Terraform modules]]

---

## Définition

Les modules réutilisables sont des modules génériques publiés dans un registry (Terraform Registry, GitHub) pour être partagés entre équipes ou projets. Les modules officiels AWS/GCP/Azure couvrent les patterns les plus courants.

---

## Terraform Registry

```hcl
# Module VPC AWS officiel
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = false    # un NAT par AZ pour la HA

  tags = {
    Environment = "production"
    Terraform   = "true"
  }
}
```

---

## Module privé depuis GitHub

```hcl
module "my-vpc" {
  source = "git::https://github.com/mycompany/terraform-modules.git//vpc?ref=v2.0.0"
  # ...
}
```

---

## Bonnes pratiques de modules

```hcl
# Toujours épingler la version
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "= 20.8.4"    # version exacte pour la reproductibilité
}
```

---

> [!tip]
> Consulter le [Terraform Registry](https://registry.terraform.io) pour les modules communautaires. Les modules `terraform-aws-modules/*` sont les plus fiables pour AWS.
