---
title: Subnets
tags:
  - intermediate
---
# Subnets

---

## Définition

Les subnets (sous-réseaux) sont des subdivisions d'un [[VPC]]. Chaque subnet est dans une seule Availability Zone. Les subnets publics ont accès à internet via un [[Internet [[Gateway]]]] ; les subnets privés n'ont pas d'IP publique.

---

## Public vs Private

| | [[Public subnet]] | [[Private subnet]] |
|---|---|---|
| Accès internet entrant | ✅ Via IGW | ❌ |
| Accès internet sortant | ✅ Via IGW | ✅ Via [[NAT]] GW |
| Ressources typiques | LB, Bastion, NAT GW | [[EC2]], RDS, [[EKS]] [[Node]] |
| IP publique | Possible | ❌ Non |

---

```bash
# Créer un subnet public
aws ec2 create-subnet   --vpc-id vpc-abc123   --cidr-block 10.0.1.0/24   --availability-zone eu-west-1a

# Activer l'auto-assign d'IP publique (pour subnet public)
aws ec2 modify-subnet-attribute   --subnet-id subnet-abc123   --map-public-ip-on-launch
```

---

## Architecture recommandée (2 AZ)

```
VPC : 10.0.0.0/16
├── subnet-public-a   10.0.1.0/24   AZ: eu-west-1a   → Internet GW
├── subnet-public-b   10.0.2.0/24   AZ: eu-west-1b   → Internet GW
├── subnet-private-a  10.0.10.0/24  AZ: eu-west-1a   → NAT GW (subnet-public-a)
└── subnet-private-b  10.0.20.0/24  AZ: eu-west-1b   → NAT GW (subnet-public-b)

Ressources :
  subnet-public   → ALB, Bastion, NAT Gateway
  subnet-private  → EC2 app servers, EKS nodes, RDS
```

```bash
# Créer le VPC
VPC_ID=$(aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --query 'Vpc.VpcId' --output text)

# Créer les subnets
aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.1.0/24 \
  --availability-zone eu-west-1a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=public-a}]'

aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.10.0/24 \
  --availability-zone eu-west-1a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=private-a}]'
```

## Planifier ses CIDRs

| Taille [[CIDR]] | Nb d'IPs utilisables | Usage |
|-------------|---------------------|-------|
| /28 | 11 | Petit subnet isolé (bastion) |
| /24 | 251 | Subnet standard |
| /22 | 1019 | Subnet large (EKS nodes) |
| /16 | 65 531 | VPC entier |

> [!tip]
> Concevoir avec au minimum 2 AZ pour la HA. Laisser de l'espace dans le CIDR du VPC pour ajouter des subnets plus tard — impossible d'agrandir un subnet existant.
