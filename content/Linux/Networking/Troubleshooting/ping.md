---
title: ping
tags:
  - beginner
---

# ping

---

## Définition

`ping` envoie des paquets ICMP Echo Request et mesure si la cible répond et en combien de temps. C'est le premier outil de diagnostic réseau — vérifie la connectivité basique (couche 3).

---

## Utilisation

```bash
# Ping basique (Ctrl+C pour arrêter)
ping 8.8.8.8
ping google.com

# Nombre de paquets limité
ping -c 4 8.8.8.8

# Interval personnalisé
ping -i 0.5 8.8.8.8    # toutes les 0.5 secondes

# Taille du paquet
ping -s 1400 8.8.8.8   # tester la fragmentation

# Ping silencieux (pour scripts)
if ping -c 1 -q 8.8.8.8 > /dev/null 2>&1; then
    echo "Internet accessible"
fi
```

---

## Lire la sortie

```
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=118 time=12.3 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=11.8 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss
round-trip min/avg/max = 11.8/12.0/12.3 ms
```

| Métrique | Signification |
|---|---|
| `ttl` | Time to live (sauts restants) |
| `time` | RTT en millisecondes |
| `packet loss` | % paquets perdus |

---

> [!note]
> Un ping qui échoue ne signifie pas toujours que la machine est down — ICMP est souvent bloqué par les [[Firewall]] en production. Utiliser `nc -zv` ou `curl` pour tester au niveau applicatif.
