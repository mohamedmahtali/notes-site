---
title: Memory limits
tags:
  - intermediate
---

# Memory limits

## Parent
- [[Resource limits]]

---

## Définition

Les memory limits définissent la quantité maximale de RAM qu'un conteneur peut utiliser. Quand cette limite est dépassée, le kernel Linux tue le processus le plus gourmand du conteneur (OOM Killer).

---

## Options

```bash
# Limite mémoire à 512 Mo
docker run --memory=512m mon-app

# Limite mémoire + swap total (recommandé : égal à --memory)
docker run --memory=512m --memory-swap=512m mon-app
# → --memory-swap = mémoire + swap, donc swap = 0 ici

# Réservation (soft limit, pour le scheduling)
docker run --memory=512m --memory-reservation=256m mon-app
```

---

## Unités acceptées

```
b   → octets
k   → kilooctets
m   → mégaoctets
g   → gigaoctets

Ex: 256m, 1g, 512m
```

---

## En Docker Compose

```yaml
services:
  api:
    image: mon-app:latest
    mem_limit: 512m
    mem_reservation: 256m
    memswap_limit: 512m
```

---

## Diagnostiquer un OOMKill

```bash
docker inspect mon-app | grep OOMKilled
# "OOMKilled": true

# Logs kernel
dmesg | grep "Killed process"
```

> [!warning]
> Sans `--memory-swap`, le swap disponible est 2x la limite mémoire par défaut. Toujours définir `--memory-swap=--memory` pour désactiver le swap et avoir un comportement prévisible.
