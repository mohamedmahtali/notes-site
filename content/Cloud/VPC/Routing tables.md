---
title: Routing tables
tags:
  - intermediate
---
# Routing tables

---

## Définition

Les route tables définissent comment le trafic réseau est dirigé dans un [[VPC]]. Chaque subnet est associé à une route table. Les règles (routes) spécifient la destination et la cible (IGW, [[NAT]] GW, VPC peering, etc.).

---

## Route tables typiques

```
Route table publique :
  Destination       Target
  10.0.0.0/16       local           ← trafic intra-VPC
  0.0.0.0/0         igw-abc123      ← tout le reste → internet

Route table privée :
  Destination       Target
  10.0.0.0/16       local           ← trafic intra-VPC
  0.0.0.0/0         nat-abc123      ← sortie via NAT Gateway
```

---

```bash
# Créer une route table
RT_ID=$(aws ec2 create-route-table \
  --vpc-id vpc-abc123 \
  --query 'RouteTable.RouteTableId' --output text)

# Associer à un subnet
aws ec2 associate-route-table \
  --route-table-id $RT_ID \
  --subnet-id subnet-abc123

# Ajouter une route vers internet (via IGW)
aws ec2 create-route \
  --route-table-id $RT_ID \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-abc123

# Ajouter une route vers un autre VPC (peering)
aws ec2 create-route \
  --route-table-id $RT_ID \
  --destination-cidr-block 10.1.0.0/16 \
  --vpc-peering-connection-id pcx-abc123

# Lister les routes
aws ec2 describe-route-tables \
  --route-table-ids $RT_ID \
  --query 'RouteTables[*].Routes' --output table
```

## VPC Peering — relier deux VPCs

```
VPC-A (10.0.0.0/16) ←──── Peering ────→ VPC-B (10.1.0.0/16)

Route table VPC-A : 10.1.0.0/16 → pcx-abc123
Route table VPC-B : 10.0.0.0/16 → pcx-abc123
```

> [!warning] Peering non transitif
> Si VPC-A est peeré avec VPC-B, et VPC-B avec VPC-C, VPC-A ne peut **pas** atteindre VPC-C via VPC-B. Utiliser un **Transit [[Gateway]]** pour un hub-and-spoke entre plusieurs VPCs.

## Priorité des routes

[[AWS]] applique la route la plus spécifique (longest prefix match) :

```
Destination        Target
10.0.0.0/16        local           ← priorité si destination dans le VPC
10.0.1.0/24        pcx-abc123      ← plus spécifique, gagne sur la route locale
0.0.0.0/0          nat-abc123      ← tout le reste (défaut)
```
