---
title: ss
tags:
  - intermediate
---

# ss

## Parent
- [[Troubleshooting]]

---

## Définition

`ss` (socket statistics) est le successeur moderne de `netstat`. Plus rapide et avec plus d'informations, il affiche les connexions réseau actives, les ports en écoute, et les statistiques des sockets.

---

## Commandes

```bash
# Ports TCP en écoute (remplace netstat -tlnp)
ss -tlnp

# Ports UDP en écoute
ss -ulnp

# Toutes les connexions établies
ss -tnp

# Connexions sur un port spécifique
ss -tnp '( dport = :80 or sport = :80 )'

# Statistiques résumées
ss -s

# Connexions d'un processus (par PID)
ss -p | grep pid=1234

# Sockets Unix (locaux)
ss -xnp
```

---

## Lire la sortie

```
State    Recv-Q  Send-Q  Local Address:Port  Peer Address:Port  Process
LISTEN   0       128     0.0.0.0:80         0.0.0.0:*          users:(("nginx",pid=123))
ESTAB    0       0       192.168.1.10:443   203.0.113.5:54321
```

| Colonne | Signification |
|---|---|
| State | LISTEN / ESTAB / TIME-WAIT / CLOSE-WAIT |
| Recv-Q | Données reçues en attente de lecture |
| Send-Q | Données envoyées non acquittées |
