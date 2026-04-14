---
title: CIDR
tags:
  - beginner
---

# CIDR

## Parent
- [[IP addressing]]

---

## Définition

CIDR (Classless Inter-Domain Routing) est une notation qui spécifie une adresse IP et le masque de sous-réseau en une seule expression : `192.168.1.0/24`. Le chiffre après `/` indique le nombre de bits du masque réseau.

---

## Notation et masques

| CIDR | Masque | Hôtes | Usage |
|---|---|---|---|
| /8 | 255.0.0.0 | 16 777 214 | Classe A |
| /16 | 255.255.0.0 | 65 534 | Classe B |
| /24 | 255.255.255.0 | 254 | Classe C, réseau standard |
| /25 | 255.255.255.128 | 126 | Sous-réseau divisé |
| /28 | 255.255.255.240 | 14 | Petit sous-réseau |
| /30 | 255.255.255.252 | 2 | Point à point |
| /32 | 255.255.255.255 | 1 | Hôte unique |

---

## Calculer

```bash
# Calculer les détails d'un réseau
ipcalc 192.168.1.0/24
# Address: 192.168.1.0
# Netmask: 255.255.255.0 = 24
# Network: 192.168.1.0/24
# Broadcast: 192.168.1.255
# HostMin: 192.168.1.1
# HostMax: 192.168.1.254
# Hosts/Net: 254
```
