---
title: A record
tags:
  - beginner
---

# A record

---

## Définition

Un enregistrement A (Address record) mappe un nom de domaine vers une adresse [[IPv4]]. C'est l'enregistrement [[DNS]] le plus fondamental.

---

## Exemples

```
nom             TTL   type  valeur
www.example.com 300   A     203.0.113.10
api.example.com 300   A     203.0.113.20
```

---

## Commandes

```bash
# Interroger un A record
dig www.example.com A
dig +short www.example.com A

# Résultat
# www.example.com. 300 IN A 203.0.113.10
```

---

## Cas d'usage

```
www       → serveur web
api       → serveur API
mail      → serveur mail
vpn       → serveur VPN
*         → wildcard (tous les sous-domaines)
```

> [!note]
> Pour [[IPv6]], l'équivalent est l'enregistrement `AAAA` qui pointe vers une adresse IPv6.
