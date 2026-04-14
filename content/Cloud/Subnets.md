---
title: Subnets
tags:
  - intermediate
---
# Subnets

## Parent
- [[Cloud]]

## Enfants
- [[Public subnet]]
- [[Private subnet]]

---

## Définition

Les subnets (sous-réseaux) sont des subdivisions d'un VPC. Chaque subnet est dans une seule Availability Zone. Les subnets publics ont accès à internet via un Internet Gateway ; les subnets privés n'ont pas d'IP publique.

---

## Public vs Private

| | Public Subnet | Private Subnet |
|---|---|---|
| Accès internet entrant | ✅ Via IGW | ❌ |
| Accès internet sortant | ✅ Via IGW | ✅ Via NAT GW |
| Ressources typiques | LB, Bastion, NAT GW | EC2, RDS, EKS nodes |
| IP publique | Possible | ❌ Non |

---

```bash
# Créer un subnet public
aws ec2 create-subnet   --vpc-id vpc-abc123   --cidr-block 10.0.1.0/24   --availability-zone eu-west-1a

# Activer l'auto-assign d'IP publique (pour subnet public)
aws ec2 modify-subnet-attribute   --subnet-id subnet-abc123   --map-public-ip-on-launch
```

---

> [!tip]
> Concevoir avec au minimum 2 AZ pour la HA. Architecture recommandée : 2 subnets publics + 2 subnets privés, un de chaque par AZ.
