---
title: VPC
tags:
  - intermediate
---
# VPC

---

## Définition

Un VPC (Virtual Private [[Cloud]]) est un réseau privé virtuel isolé dans le cloud. Il permet de définir sa propre topologie réseau : plages IP, sous-réseaux, règles de routage, et contrôle d'accès. Chaque cloud provider a son équivalent ([[AWS]] VPC, GCP VPC, [[Azure]] VNet).

---

## Composants clés

```
VPC (10.0.0.0/16)
├── Subnets — divisions du VPC par zone de dispo
├── Route Tables — règles de routage
├── Internet Gateway — accès internet pour subnets publics
├── NAT Gateway — accès internet sortant pour subnets privés
├── Security Groups — firewall par instance
└── NACLs — firewall par subnet (stateless)
```

---

## Security Groups vs NACLs

| | [[Security [[Groups]]]] | NACLs |
|---|---|---|
| Niveau | Instance | Subnet |
| Statefull | ✅ Oui | ❌ Non |
| Règles deny | ❌ (implicit deny) | ✅ Explicites |
| Ordre des règles | N/A | Numérotées |

---

> [!note]
> Voir [[Internet gateway]], [[NAT gateway]], [[Routing tables]] pour les composants réseau détaillés.
