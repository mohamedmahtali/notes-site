---
title: Ephemeral ports
tags:
  - intermediate
---

# Ephemeral ports

## Parent
- [[Ports]]

---

## Définition

Les ports éphémères (49152-65535) sont des ports temporaires attribués automatiquement par le kernel à un client lors d'une connexion sortante. Ils permettent d'identifier la connexion côté client.

---

## Fonctionnement

```
Client (port éphémère 54321)  →  Serveur (port 80)
Socket : 192.168.1.5:54321 → 93.184.216.34:80

Le kernel choisit le port 54321 automatiquement dans la plage éphémère.
À la fin de la connexion, le port est libéré et réutilisable.
```

---

## Configuration

```bash
# Voir la plage éphémère configurée
cat /proc/sys/net/ipv4/ip_local_port_range
# 32768 60999

# Modifier (plus de ports disponibles = plus de connexions simultanées)
echo "1024 65535" > /proc/sys/net/ipv4/ip_local_port_range

# Permanent dans /etc/sysctl.conf
net.ipv4.ip_local_port_range = 1024 65535
```

---

## Voir les ports éphémères en cours

```bash
ss -tn | head -20
# ESTAB  0  0  192.168.1.5:54321  93.184.216.34:443
#                        ^^^^^
#                    port éphémère
```
