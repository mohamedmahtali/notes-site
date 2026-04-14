---
title: Subnetting
tags:
  - intermediate
---

# Subnetting

## Parent
- [[IP addressing]]

---

## Définition

Le subnetting (sous-réseau) divise un réseau IP en segments plus petits et isolés. Cela améliore la sécurité, réduit les collisions broadcast, et optimise le routage.

---

## Exemple de découpage

```
Réseau principal : 10.0.0.0/16 (65 534 hôtes)

Découpage en /24 (254 hôtes chacun) :
  10.0.1.0/24  → Réseau de production
  10.0.2.0/24  → Réseau de staging
  10.0.3.0/24  → Réseau de développement
  10.0.4.0/24  → Réseau d'administration
```

---

## Adresses importantes d'un sous-réseau

```
10.0.1.0/24 :
  10.0.1.0     → Adresse réseau (non utilisable)
  10.0.1.1     → Généralement la gateway
  10.0.1.2 à 10.0.1.254 → Hôtes disponibles
  10.0.1.255   → Broadcast (non utilisable)
```

---

## En pratique (AWS, GCP, Azure)

```
VPC 10.0.0.0/16 → réseau principal du cloud
  Subnet public  : 10.0.1.0/24 → load balancers
  Subnet privé   : 10.0.2.0/24 → applications
  Subnet DB      : 10.0.3.0/24 → bases de données
```
