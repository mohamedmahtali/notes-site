---
title: NAT gateway
tags:
  - intermediate
---
# NAT gateway

## Parent
- [[VPC]]

---

## Définition

Un NAT Gateway permet aux instances dans des subnets privés d'initier des connexions vers internet (mises à jour, téléchargements) sans être accessibles depuis internet. Le trafic entrant non-sollicité est bloqué.

---

## Pourquoi l'utiliser

> [!tip] Les serveurs backend ne doivent pas être exposés
> Les bases de données et serveurs applicatifs dans les subnets privés n'ont pas d'IP publique. Le NAT Gateway leur permet de télécharger des paquets, contacter des APIs externes, tout en restant injoignables depuis internet.

---

```bash
# Créer un NAT Gateway dans le subnet public
EIP_ID=$(aws ec2 allocate-address --domain vpc   --query 'AllocationId' --output text)

NAT_ID=$(aws ec2 create-nat-gateway   --subnet-id subnet-public-abc123   --allocation-id $EIP_ID   --query 'NatGateway.NatGatewayId' --output text)

# Ajouter une route dans la route table des subnets privés
aws ec2 create-route   --route-table-id rtb-private-abc123   --destination-cidr-block 0.0.0.0/0   --nat-gateway-id $NAT_ID
```

---

## Coût

> [!warning] Le NAT Gateway coûte cher
> NAT Gateway : ~$0.045/heure + $0.045/GB de données traitées. Pour réduire les coûts : utiliser des VPC Endpoints pour S3/DynamoDB (gratuits), et minimiser les données qui passent par le NAT.
