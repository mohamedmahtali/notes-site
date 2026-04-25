---
title: Security groups
tags:
  - intermediate
---
# Security groups

---

## Définition

Les [[Security]] [[Groups]] sont des [[Firewall]] virtuels au niveau des instances dans le [[Cloud]]. Ils filtrent le trafic entrant (inbound) et sortant (outbound) basé sur les protocoles, [[Ports]], et sources/destinations. Ils sont stateful : si le trafic entrant est autorisé, la réponse est automatiquement autorisée.

---

## Règles par défaut

```
Nouveau Security Group :
  Inbound  : ❌ Tout bloqué (deny all)
  Outbound : ✅ Tout autorisé (allow all)
```

---

## Commandes AWS

```bash
# Créer un SG
aws ec2 create-security-group   --group-name web-sg   --description "Security group for web servers"   --vpc-id vpc-abc123

# Autoriser HTTP/HTTPS depuis internet
aws ec2 authorize-security-group-ingress   --group-id sg-abc123   --protocol tcp   --port 443   --cidr 0.0.0.0/0

# Autoriser SSH depuis une IP spécifique
aws ec2 authorize-security-group-ingress   --group-id sg-abc123   --protocol tcp   --port 22   --cidr 10.0.0.5/32

# Référencer un autre SG (plutôt qu'une IP)
aws ec2 authorize-security-group-ingress   --group-id sg-backend   --protocol tcp   --port 5432   --source-group sg-app
```
