---
title: Inbound rules
tags:
  - beginner
---
# Inbound rules

---

## Définition

Les règles inbound contrôlent le trafic entrant vers une instance. Par défaut, tout le trafic entrant est bloqué — il faut explicitement autoriser chaque port/protocole nécessaire.

---

## Règles typiques par type de serveur

```
Web server (public) :
  TCP 80  → 0.0.0.0/0 (HTTP)
  TCP 443 → 0.0.0.0/0 (HTTPS)
  TCP 22  → 10.0.0.0/8 (SSH depuis le réseau interne)

App server (privé) :
  TCP 8080 → sg-loadbalancer (depuis le LB uniquement)
  TCP 22   → sg-bastion (depuis le bastion uniquement)

Database (privé) :
  TCP 5432 → sg-appserver (PostgreSQL depuis l'app uniquement)
```

---

## Créer des règles via AWS CLI

```bash
# Créer un security group
SG_ID=$(aws ec2 create-security-group \
  --group-name web-sg \
  --description "Web server security group" \
  --vpc-id vpc-abc123 \
  --query 'GroupId' --output text)

# Autoriser HTTPS depuis internet
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp --port 443 --cidr 0.0.0.0/0

# Autoriser HTTP depuis internet (pour redirect → HTTPS)
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp --port 80 --cidr 0.0.0.0/0

# Autoriser SSH uniquement depuis un autre Security Group (bastion)
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp --port 22 \
  --source-group sg-bastion-id

# Supprimer une règle
aws ec2 revoke-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp --port 80 --cidr 0.0.0.0/0
```

## Architecture typique en 3 couches

```
Internet
   │
   ▼
sg-alb          : TCP 80, 443 ← 0.0.0.0/0
   │
   ▼
sg-app          : TCP 8080 ← sg-alb seulement
                  TCP 22   ← sg-bastion seulement
   │
   ▼
sg-db           : TCP 5432 (PG) ← sg-app seulement
                  TCP 3306 (MySQL) ← sg-app seulement
```

## Principe du moindre privilège

> [!warning] Ne jamais exposer les [[Ports]] admin
> - Jamais `0.0.0.0/0` sur le port 22 ([[SSH]]), 3306 (MySQL), 5432 (PostgreSQL)
> - Référencer des [[Security [[Groups]]]] plutôt que des [[CIDR]] quand possible — les IPs changent, les SGs non
> - Utiliser [[AWS]] Systems Manager Session Manager pour SSH sans port 22 exposé
