---
title: OSI model
tags:
  - networking
  - beginner
---

# Modèle OSI

## Définition

Le modèle OSI (Open Systems Interconnection) est un cadre conceptuel qui standardise les fonctions d'un réseau de télécommunication en 7 couches. Chaque couche a une responsabilité précise et s'appuie sur la couche inférieure.

> [!note] OSI vs TCP/IP
> En pratique, on utilise le modèle TCP/IP (4 couches). Le modèle OSI à 7 couches est principalement utilisé pour comprendre et diagnostiquer les problèmes réseau.

## Les 7 couches

| # | Couche | Protocoles | Équipements |
|---|--------|-----------|-------------|
| 7 | Application | HTTP, DNS, SMTP, FTP | — |
| 6 | Présentation | [[TLS]]/SSL, JPEG, UTF-8 | — |
| 5 | Session | NetBIOS, RPC | — |
| 4 | Transport | TCP, UDP | [[Firewall]] stateful |
| 3 | Réseau | IP, ICMP, BGP | Routeur |
| 2 | Liaison | Ethernet, Wi-Fi, ARP | Switch |
| 1 | Physique | Câbles, fibre, Wi-Fi | Hub, câble |

## Mnémotechnique

```
All People Seem To Need Data Processing
A  P       S    T  N     D    P
7  6       5    4  3     2    1  (de haut en bas)
```

## Où se situent les outils DevOps

```
L7 — Application  : HTTP (nginx, haproxy L7), DNS, API REST
L4 — Transport    : TCP (haproxy L4, iptables), ports
L3 — Réseau       : IP routing, VPC, security groups
L2 — Liaison      : VLANs, MAC addresses
```

## Liens

- [[TCP IP]]
- [[DNS]]
- [[Networking]]
