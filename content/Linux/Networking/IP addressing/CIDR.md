---
title: CIDR
tags:
  - beginner
---

# CIDR

---

## Définition

CIDR (Classless Inter-Domain [[Routing]]) est une notation qui spécifie une adresse IP et le masque de sous-réseau en une seule expression : `192.168.1.0/24`. Le chiffre après `/` indique le nombre de bits du masque réseau.

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
# Détails d'un réseau
ipcalc 192.168.1.0/24
# Address: 192.168.1.0
# Netmask: 255.255.255.0 = 24
# Broadcast: 192.168.1.255
# HostMin: 192.168.1.1
# HostMax: 192.168.1.254
# Hosts/Net: 254

# Découper un /24 en sous-réseaux /26 (4 sous-réseaux de 62 hôtes)
ipcalc 192.168.1.0/24 --split 62 62 62 62

# Vérifier si une IP est dans un sous-réseau
python3 -c "import ipaddress; print('10.0.1.50' in ipaddress.ip_network('10.0.0.0/16'))"
```

## Subnetting pratique

Diviser `10.0.0.0/16` pour un [[VPC]] [[AWS]] (4 AZ × 2 [[Types]]) :

```
10.0.0.0/16  (65 534 hôtes)
├── Public subnets
│   ├── 10.0.1.0/24   AZ-a  (254 hôtes)
│   └── 10.0.2.0/24   AZ-b
├── Private subnets
│   ├── 10.0.10.0/24  AZ-a
│   └── 10.0.20.0/24  AZ-b
└── Réservé pour expansion future
    └── 10.0.100.0/22  (1 022 hôtes — EKS nodes)
```

> [!tip] Réserver de l'espace
> Toujours planifier plus large que nécessaire. Un sous-réseau trop petit ne peut pas être agrandi sans recréer l'infrastructure. En AWS, /22 (1022 hôtes) est recommandé pour les [[Node]] pools K8s.

## RFC 1918 — adresses privées

| Bloc | Plage | Taille |
|------|-------|--------|
| `10.0.0.0/8` | 10.0.0.0 – 10.255.255.255 | 16M adresses |
| `172.16.0.0/12` | 172.16.0.0 – 172.31.255.255 | 1M adresses |
| `192.168.0.0/16` | 192.168.0.0 – 192.168.255.255 | 65K adresses |
