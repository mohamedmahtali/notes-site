---
title: Ports
tags:
  - beginner
---

# Ports

---

## Définition

Un port est un numéro (0-65535) qui identifie un service spécifique sur une machine. IP adresse la machine, le port adresse le service. Un socket = IP + Port + Protocole.

---

## Catégories

| Plage | Nom | Usage |
|---|---|---|
| 0-1023 | Well-known ports | [[Services]] standards (root requis) |
| 1024-49151 | Registered ports | Services utilisateurs enregistrés |
| 49152-65535 | [[Ephemeral ports]] | Ports temporaires clients |

---

## Commandes

```bash
# Ports en écoute
ss -tlnp                  # TCP en écoute
ss -ulnp                  # UDP en écoute
ss -tlnp | grep :80       # port spécifique

# Tester un port
nc -zv 192.168.1.10 80    # test TCP
nc -zvw3 host port        # avec timeout 3s

# Processus utilisant un port
lsof -i :8080
ss -tlnp | grep 8080
fuser 8080/tcp
```
