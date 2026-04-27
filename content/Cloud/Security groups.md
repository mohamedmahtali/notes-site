---
title: Security groups
tags:
  - intermediate
---
# Security groups

## Définition

Les Security Groups sont des firewalls virtuels au niveau des instances dans le [[Cloud]]. Ils filtrent le trafic entrant (inbound) et sortant (outbound) basé sur les protocoles, ports, et sources/destinations. Ils sont **stateful** : si le trafic entrant est autorisé, la réponse est automatiquement autorisée (pas besoin de règle outbound symétrique).

## Comportement par défaut

```
Nouveau Security Group :
  Inbound  : ❌ Tout bloqué (implicit deny)
  Outbound : ✅ Tout autorisé (allow all)

→ Ajouter des règles inbound pour ouvrir ce dont vous avez besoin
→ Restreindre l'outbound pour les workloads sensibles
```

## Anatomie d'une règle

| Champ | Description | Exemple |
|-------|-------------|---------|
| Type | Protocole prédéfini ou custom | HTTP, HTTPS, SSH, Custom TCP |
| Protocol | TCP, UDP, ICMP | tcp |
| Port range | Port ou plage de ports | 443 ou 8080-8090 |
| Source/Dest | CIDR, autre SG, ou préfixe | 10.0.0.0/8, sg-abc123 |
| Description | Label lisible | "Allow HTTPS from internet" |

## Patterns courants

### Architecture 3 couches

```
Internet → SG-ALB (443 depuis 0.0.0.0/0)
         → SG-App (8080 depuis SG-ALB seulement)
           → SG-DB  (5432 depuis SG-App seulement)
```

Référencer un SG comme source (plutôt qu'un CIDR) est plus robuste : les règles restent valides même si les IPs changent.

### Commandes AWS CLI

```bash
# Créer un SG
aws ec2 create-security-group \
  --group-name web-sg \
  --description "Security group for web servers" \
  --vpc-id vpc-abc123

# Autoriser HTTPS depuis internet
aws ec2 authorize-security-group-ingress \
  --group-id sg-web \
  --protocol tcp --port 443 --cidr 0.0.0.0/0

# Autoriser SSH depuis une IP spécifique uniquement
aws ec2 authorize-security-group-ingress \
  --group-id sg-web \
  --protocol tcp --port 22 --cidr 10.0.0.5/32

# Référencer un autre SG (backend accessible depuis app uniquement)
aws ec2 authorize-security-group-ingress \
  --group-id sg-backend \
  --protocol tcp --port 5432 \
  --source-group sg-app

# Lister les règles d'un SG
aws ec2 describe-security-groups --group-ids sg-abc123
```

## Security Groups vs NACLs

| | Security Groups | NACLs |
|---|---|---|
| Niveau | Instance | Subnet |
| Stateful | ✅ (retour auto) | ❌ (règles symétriques requises) |
| Règles Deny explicites | ❌ (implicit deny) | ✅ |
| Ordre des règles | N/A (toutes évaluées) | Numérotées (priorité croissante) |
| Application | À la création de l'ENI | À chaque paquet |
| Usage recommandé | ✅ Principal outil | Défense en profondeur |

La bonne pratique : utiliser les Security Groups pour l'essentiel du contrôle d'accès, les NACLs comme barrière supplémentaire au niveau subnet.

## Bonnes pratiques

| Pratique | Pourquoi |
|----------|----------|
| Jamais `0.0.0.0/0` sur SSH/RDP | Expose à internet, remplacer par Bastion + SG source |
| Référencer des SGs plutôt que des CIDRs | Indépendant des changements d'IP |
| Une description par règle | Audit et maintenance facilités |
| Supprimer les règles inutilisées | Réduire la surface d'attaque |
| SG dédié par couche applicative | ALB, app, BDD, bastion = 4 SGs séparés |

## Explorer

- **[[VPC]]** — contexte réseau dans lequel les SGs s'appliquent
- **[[Subnets]]** — découpage réseau, NACLs au niveau subnet
- **[[IAM]]** — contrôle d'accès aux ressources (différent du contrôle réseau)
