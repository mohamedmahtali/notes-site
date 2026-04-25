---
title: NAT gateway
tags:
  - intermediate
---
# NAT gateway

---

## Définition

Un [[NAT]] [[Gateway]] permet aux instances dans des [[Subnets]] privés d'initier des connexions vers internet (mises à jour, téléchargements) sans être accessibles depuis internet. Le trafic entrant non-sollicité est bloqué.

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
> NAT Gateway : ~$0.045/heure + $0.045/GB de données traitées. Pour réduire les coûts : utiliser des [[VPC]] Endpoints pour S3/DynamoDB (gratuits), et minimiser les données qui passent par le NAT.

## VPC Endpoints — alternative sans NAT pour les services AWS

Pour accéder à S3, DynamoDB, SSM, [[Secrets]] Manager depuis un subnet privé, un **VPC Endpoint** est gratuit et plus rapide (trafic reste dans [[AWS]]).

```bash
# Créer un Gateway Endpoint pour S3 (gratuit)
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-abc123 \
  --service-name com.amazonaws.eu-west-1.s3 \
  --route-table-ids rtb-private-abc123

# Créer un Interface Endpoint pour Secrets Manager
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-abc123 \
  --vpc-endpoint-type Interface \
  --service-name com.amazonaws.eu-west-1.secretsmanager \
  --subnet-ids subnet-private-abc123 \
  --security-group-ids sg-abc123
```

| Accès | Via NAT Gateway | Via VPC Endpoint |
|-------|----------------|-----------------|
| S3 | ~$0.045/GB | Gratuit (Gateway) |
| DynamoDB | ~$0.045/GB | Gratuit (Gateway) |
| Secrets Manager | ~$0.045/GB | ~$0.01/heure (Interface) |
| Internet (npm, apt...) | Via NAT (obligatoire) | — |

> [!tip] Audit du trafic NAT
> Utiliser VPC Flow Logs pour identifier les destinations les plus coûteuses et voir lesquelles pourraient être remplacées par des VPC Endpoints.
