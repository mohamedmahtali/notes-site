---
title: Module inputs
tags:
  - beginner
---
# Module inputs

## Parent
- [[Terraform modules]]

---

## Définition

Les inputs d'un module sont les variables définies dans `variables.tf` du module. Ils permettent à l'appelant de personnaliser le comportement du module.

---

## Définir les inputs

```hcl
# modules/vpc/variables.tf
variable "vpc_name" {
  description = "Nom du VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block du VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "private_subnets" {
  description = "CIDR blocks des subnets privés"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "enable_nat_gateway" {
  description = "Activer le NAT Gateway"
  type        = bool
  default     = true
}
```

---

## Passer les inputs

```hcl
# main.tf (root module)
module "vpc" {
  source = "./modules/vpc"

  vpc_name           = "production-vpc"
  cidr_block         = "10.10.0.0/16"
  private_subnets    = ["10.10.1.0/24", "10.10.2.0/24", "10.10.3.0/24"]
  enable_nat_gateway = true   # override du défaut
}
```
