---
title: Chains
tags:
  - advanced
---

# Chains

## Parent
- [[iptables]]

---

## Définition

Les chains (chaînes) iptables sont des séquences ordonnées de règles. Chaque paquet traverse une ou plusieurs chains selon son type. Si aucune règle ne correspond, la politique par défaut de la chain s'applique.

---

## Chains built-in

```
INPUT    : paquets entrants destinés à la machine
OUTPUT   : paquets sortants émis par la machine
FORWARD  : paquets en transit (machine = routeur)
PREROUTING : avant la décision de routage (DNAT, load balancing)
POSTROUTING : après la décision de routage (SNAT, masquerade)
```

---

## Flux des paquets

```
Paquet entrant :
Network → PREROUTING → routage → INPUT → Processus local
                               → FORWARD → POSTROUTING → Network

Paquet sortant :
Processus local → OUTPUT → POSTROUTING → Network
```

---

## Commandes

```bash
# Voir les chains et règles
iptables -L         # table filter
iptables -t nat -L  # table nat

# Créer une chain custom
iptables -N DOCKER
iptables -N LOGGING

# Sauter vers une chain custom
iptables -A INPUT -j LOGGING

# Vider une chain
iptables -F INPUT
```
