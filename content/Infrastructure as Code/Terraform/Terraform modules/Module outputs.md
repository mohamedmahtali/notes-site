---
title: Module outputs
tags:
  - beginner
---
# Module outputs

## Parent
- [[Terraform modules]]

---

## Définition

Les outputs d'un module exposent des valeurs calculées (IDs, IPs, ARNs) que d'autres modules ou le module root peuvent utiliser. Ils sont définis dans `outputs.tf` du module.

---

## Définir les outputs

```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  description = "ID du VPC créé"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "IDs des subnets privés"
  value       = aws_subnet.private[*].id
}

output "public_subnet_ids" {
  description = "IDs des subnets publics"
  value       = aws_subnet.public[*].id
}

output "nat_gateway_ip" {
  description = "IP publique du NAT Gateway"
  value       = aws_eip.nat.public_ip
  sensitive   = false
}
```

---

## Utiliser les outputs d'un module

```hcl
# Dans le module root ou un autre module
module "vpc" {
  source = "./modules/vpc"
  # ...
}

module "eks" {
  source = "./modules/eks"

  vpc_id     = module.vpc.vpc_id           # output du module vpc
  subnet_ids = module.vpc.private_subnet_ids
}

output "nat_ip" {
  value = module.vpc.nat_gateway_ip
}
```
