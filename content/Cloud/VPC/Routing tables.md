---
title: Routing tables
tags:
  - intermediate
---
# Routing tables

## Parent
- [[VPC]]

---

## Définition

Les route tables définissent comment le trafic réseau est dirigé dans un VPC. Chaque subnet est associé à une route table. Les règles (routes) spécifient la destination et la cible (IGW, NAT GW, VPC peering, etc.).

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
aws ec2 create-route-table --vpc-id vpc-abc123

# Associer à un subnet
aws ec2 associate-route-table   --route-table-id rtb-abc123   --subnet-id subnet-abc123

# Ajouter une route
aws ec2 create-route   --route-table-id rtb-abc123   --destination-cidr-block 0.0.0.0/0   --gateway-id igw-abc123

# Lister les routes
aws ec2 describe-route-tables   --route-table-ids rtb-abc123   --query 'RouteTables[*].Routes'
```
