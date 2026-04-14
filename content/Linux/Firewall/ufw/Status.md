---
title: Status
tags:
  - beginner
---

# Status

## Parent
- [[ufw]]

---

## Définition

`ufw status` affiche l'état du firewall (actif/inactif) et la liste des règles actives.

---

## Commandes

```bash
# État simple
ufw status
# Status: active
# To                         Action  From
# 22/tcp                     ALLOW   Anywhere
# 80/tcp                     ALLOW   Anywhere
# 443/tcp                    ALLOW   Anywhere

# Avec plus de détails
ufw status verbose

# Avec numéros (pour supprimer par numéro)
ufw status numbered
# [ 1] 22/tcp   ALLOW IN  Anywhere
# [ 2] 80/tcp   ALLOW IN  Anywhere

# Supprimer par numéro
ufw delete 1
```

---

## Vérifications rapides

```bash
# UFW actif ?
ufw status | grep "Status: active"

# Port spécifique ouvert ?
ufw status | grep "443"

# Logs
tail -f /var/log/ufw.log
```
