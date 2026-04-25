---
title: Internet gateway
tags:
  - intermediate
---
# Internet gateway

---

## Définition

L'Internet [[Gateway]] est la passerelle qui connecte un [[VPC]] à internet. Les instances dans les [[Subnets]] publics avec une route vers l'IGW peuvent recevoir du trafic entrant et sortant depuis internet.

---

```bash
# AWS — créer et attacher une IGW
IGW_ID=$(aws ec2 create-internet-gateway   --query 'InternetGateway.InternetGatewayId' --output text)

aws ec2 attach-internet-gateway   --internet-gateway-id $IGW_ID   --vpc-id vpc-abc123

# Ajouter une route vers l'IGW dans la route table publique
aws ec2 create-route   --route-table-id rtb-abc123   --destination-cidr-block 0.0.0.0/0   --gateway-id $IGW_ID
```

---

## Architecture

```
Internet
    ↕ (toutes directions)
Internet Gateway
    ↕
Public Subnet (avec route 0.0.0.0/0 → IGW)
    ├── Load Balancer (IP publique)
    └── NAT Gateway (pour sortie des subnets privés)
```

---

> [!note]
> Pour qu'une instance reçoive du trafic entrant, elle doit avoir : 1) une IP publique ou Elastic IP, 2) une route vers l'IGW dans sa subnet route table, 3) un [[Security]] group qui autorise le trafic.
