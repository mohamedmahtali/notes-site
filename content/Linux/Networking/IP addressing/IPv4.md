---
title: IPv4
tags:
  - beginner
---

# IPv4

## Parent
- [[IP addressing]]

---

## Définition

IPv4 est la version 4 du protocole IP, utilisant des adresses sur 32 bits (4 octets) notées en décimal pointé. C'est encore le protocole dominant malgré l'épuisement des adresses publiques.

---

## Format

```
192 . 168 . 1 . 10
 ↑      ↑    ↑   ↑
Octet 1 2    3   4  (0-255 chacun)
```

---

## Classes d'adresses

```
Classe A : 0.0.0.0  – 127.255.255.255  /8   (grands réseaux)
Classe B : 128.0.0.0 – 191.255.255.255 /16  (réseaux moyens)
Classe C : 192.0.0.0 – 223.255.255.255 /24  (petits réseaux)
```

---

## Commandes

```bash
# Voir les IPs IPv4
ip -4 addr show

# Ping IPv4 explicite
ping -4 google.com

# Configurer une IP
ip addr add 192.168.1.10/24 dev eth0
```
