---
title: Routing
tags:
  - intermediate
---

# Routing

---

## Définition

Le routage détermine le chemin qu'un paquet emprunte pour atteindre sa destination. Chaque hôte [[Linux]] a une table de routage qui indique via quelle interface et quelle [[Gateway]] envoyer les paquets.

---

## Commandes

```bash
# Voir la table de routage
ip route show
# default via 192.168.1.1 dev eth0 proto dhcp
# 192.168.1.0/24 dev eth0 proto kernel scope link

# Route par défaut (gateway)
ip route show default

# Ajouter une route
ip route add 10.0.0.0/8 via 192.168.1.1
ip route add default via 192.168.1.1

# Supprimer une route
ip route del 10.0.0.0/8

# Quelle interface serait utilisée pour atteindre une IP ?
ip route get 8.8.8.8
# 8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.10

# Activer le forwarding IP (pour un routeur/NAT)
echo 1 > /proc/sys/net/ipv4/ip_forward
# Permanent : net.ipv4.ip_forward = 1 dans /etc/sysctl.conf
```

---

## Table de routage typique

```
Destination     Gateway         Interface
0.0.0.0/0       192.168.1.1     eth0    ← route par défaut
192.168.1.0/24  0.0.0.0         eth0    ← réseau local (direct)
10.0.0.0/8      10.8.0.1        tun0    ← via VPN
```
