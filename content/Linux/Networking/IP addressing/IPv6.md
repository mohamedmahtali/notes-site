---
title: IPv6
tags:
  - intermediate
---

# IPv6

## Parent
- [[IP addressing]]

---

## Définition

IPv6 est la version 6 du protocole IP, utilisant des adresses sur 128 bits notées en hexadécimal. Il résout l'épuisement des adresses IPv4 (3.4 × 10^38 adresses possibles vs 4.3 milliards).

---

## Format

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
→ Abrégé : 2001:db8:85a3::8a2e:370:7334

:: représente des groupes de zéros consécutifs
```

---

## Adresses spéciales

```
::1           → loopback (équivalent 127.0.0.1)
fe80::/10     → link-local (autoconfiguration)
::/0          → route par défaut
2001:db8::/32 → plage réservée documentation
```

---

## Commandes

```bash
# IPs IPv6
ip -6 addr show

# Ping IPv6
ping6 google.com
ping -6 google.com

# Ajouter une IP IPv6
ip -6 addr add 2001:db8::10/64 dev eth0

# Table de routage IPv6
ip -6 route show
```
