---
title: VPC
tags:
  - intermediate
---
# VPC

---

## Définition

Un [[AWS]] VPC (Virtual Private [[Cloud]]) est un réseau virtuel isolé dans AWS. Il permet de contrôler complètement l'environnement réseau : plage IP, sous-réseaux, tables de routage, passerelles.

---

## Architecture typique

```
VPC: 10.0.0.0/16
├── Public Subnet (10.0.1.0/24) — AZ-a
│   └── Load Balancer, NAT Gateway
├── Public Subnet (10.0.2.0/24) — AZ-b
│   └── Load Balancer (HA)
├── Private Subnet (10.0.3.0/24) — AZ-a
│   └── EC2 instances, EKS nodes
└── Private Subnet (10.0.4.0/24) — AZ-b
    └── EC2 instances, RDS replica
```

---

## Commandes

```bash
# Créer un VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16

# Créer des subnets
aws ec2 create-subnet   --vpc-id vpc-abc123   --cidr-block 10.0.1.0/24   --availability-zone eu-west-1a

# Internet Gateway (pour les subnets publics)
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway   --internet-gateway-id igw-abc123   --vpc-id vpc-abc123
```

---

> [!tip]
> Toujours déployer dans au moins 2 AZ pour la haute disponibilité. Les instances dans les [[Subnets]] privés accèdent à internet via un [[NAT [[Gateway]]]] dans le subnet public.
