---
title: IP addressing
tags:
  - beginner
---

# IP addressing

## Parent
- [[Networking]]

## Enfants
- [[IPv4]]
- [[IPv6]]
- [[CIDR]]
- [[Subnetting]]

---

## Définition

L'adressage IP est le système d'identification des machines sur un réseau. IPv4 utilise des adresses 32 bits (ex: 192.168.1.1), IPv6 des adresses 128 bits (ex: 2001:db8::1). Le CIDR définit les sous-réseaux.

---

## Classes d'adresses privées

| Plage | CIDR | Usage |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | Réseaux d'entreprise |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | Docker, VPN |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | Réseaux domestiques/LAN |

---

## Adresses spéciales

```
127.0.0.0/8    → loopback (lo, 127.0.0.1)
0.0.0.0        → toutes les interfaces (LISTEN)
255.255.255.255 → broadcast
```

---

## Commandes

```bash
# Voir les IPs
ip addr show
hostname -I     # IPs de la machine

# Tester la connectivité
ping 8.8.8.8
curl ifconfig.me   # IP publique

# Identifier le sous-réseau
ipcalc 192.168.1.10/24
```
