---
title: VPC
tags:
  - intermediate
---
# VPC

## Définition

Un VPC (Virtual Private [[Cloud]]) est un réseau privé virtuel isolé dans le cloud. Il définit la topologie réseau : plages IP, sous-réseaux, routage, et contrôle d'accès. Chaque cloud provider a son équivalent ([[AWS]] VPC, GCP VPC, [[Azure]] VNet).

## Composants clés

```
VPC (10.0.0.0/16 — 65 536 adresses)
├── Subnets          — divisions du VPC par AZ et visibilité
├── Route Tables     — règles de routage par subnet
├── Internet Gateway — connexion internet pour subnets publics
├── NAT Gateway      — sortie internet pour subnets privés (sans entrée)
├── Security Groups  — firewall stateful au niveau instance
└── NACLs            — firewall stateless au niveau subnet
```

## Design typique : 3 couches

Architecture standard pour une app en production sur AWS (multi-AZ) :

```
VPC : 10.0.0.0/16
│
├── Public subnets (10.0.1.0/24, 10.0.2.0/24)
│   → Load balancer, NAT Gateway, Bastion host
│   → Route : 0.0.0.0/0 → Internet Gateway
│
├── Private subnets (10.0.11.0/24, 10.0.12.0/24)
│   → Serveurs applicatifs, pods Kubernetes
│   → Route : 0.0.0.0/0 → NAT Gateway
│
└── Database subnets (10.0.21.0/24, 10.0.22.0/24)
    → RDS, ElastiCache, aucun accès internet
    → Route : local uniquement
```

Pourquoi ce design ? La règle est : **exposer le minimum nécessaire**.
- Le load balancer est en public (doit recevoir le trafic internet)
- L'app est en private (accessible uniquement depuis le LB)
- La BDD est dans un subnet dédié sans route externe

## CIDR — calcul rapide

| CIDR | Adresses disponibles | Cas d'usage |
|------|---------------------|-------------|
| `/16` | 65 534 | VPC entier |
| `/24` | 254 | Subnet moyen |
| `/27` | 30 | Petit subnet (lambdas, NAT GW) |
| `/28` | 14 | Très petit subnet |

Réserver assez d'espace dès le départ — étendre un VPC est pénible.

## Security Groups vs NACLs

| | [[Security groups]] | NACLs |
|---|---|---|
| Niveau | Instance | Subnet |
| Stateful | ✅ (retour auto) | ❌ (règles symétriques requises) |
| Règles deny explicites | ❌ (implicit deny) | ✅ |
| Ordre des règles | N/A | Numérotées (priorité croissante) |
| Usage recommandé | ✅ Principal outil | Couche défense en profondeur |

## VPC Peering et Transit Gateway

```
VPC Peering : relier 2 VPCs directement (même compte ou cross-account)
  Limite : pas de routage transitif (A↔B et B↔C ≠ A↔C)

Transit Gateway : hub central pour relier N VPCs et VPNs
  Use case : architectures multi-VPC, multi-compte, hybride
```

## Explorer

- **[[Subnets]]** — public, private, database subnets
- **[[Internet gateway]]** — accès internet entrant/sortant pour subnets publics
- **[[NAT gateway]]** — sortie internet pour instances privées
- **[[Security groups]]** — règles inbound/outbound par instance
- **[[Routing tables]]** — routage entre subnets et vers internet
