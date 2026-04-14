---
title: traceroute
tags:
  - intermediate
---

# traceroute

## Parent
- [[Troubleshooting]]

---

## Définition

`traceroute` affiche le chemin réseau (tous les routeurs intermédiaires) entre la machine locale et une destination. Il identifie où la connectivité s'interrompt.

---

## Utilisation

```bash
# Traceroute standard (UDP)
traceroute 8.8.8.8
traceroute google.com

# Via TCP port 80 (passe mieux les firewalls)
traceroute -T -p 80 8.8.8.8

# Limiter les sauts
traceroute -m 15 8.8.8.8

# mtr – traceroute interactif (recommandé)
mtr 8.8.8.8
mtr --report 8.8.8.8    # rapport non-interactif
```

---

## Lire la sortie

```
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max
 1  192.168.1.1 (192.168.1.1)  1.2 ms      ← gateway locale
 2  10.0.0.1 (10.0.0.1)  5.4 ms           ← FAI
 3  * * *                                  ← routeur ICMP bloqué
 4  8.8.8.8 (8.8.8.8)  12.3 ms            ← destination
```

| Symbole | Signification |
|---|---|
| IP + temps | Saut normal |
| `* * *` | ICMP bloqué ou timeout |
| Temps élevé | Latence à ce saut |
