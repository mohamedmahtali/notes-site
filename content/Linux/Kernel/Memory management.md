---
title: Memory management
tags:
  - advanced
---

# Memory management

---

## Définition

La gestion mémoire du [[Kernel]] [[Linux]] alloue et gère la RAM entre les processus. Elle utilise la mémoire virtuelle (chaque processus a son propre espace d'adressage), la pagination, et le [[Swap]] pour gérer plus de mémoire que la RAM physique disponible.

---

## Commandes

```bash
# Mémoire disponible
free -h
# total    used    free  shared  buff/cache  available
# 7.7Gi   3.2Gi   1.5Gi  200Mi      3.0Gi      4.3Gi

cat /proc/meminfo

# Mémoire par processus
ps -eo pid,rss,cmd --sort=-rss | head -10
cat /proc/PID/status | grep -i mem

# Utilisation mémoire détaillée
smem -r    # si installé
```

---

## Cache mémoire

Linux utilise toute la RAM disponible comme cache disque (buff/cache). Ce n'est pas de la mémoire "perdue" — elle est libérée si un processus en a besoin.

```bash
# La colonne "available" est plus pertinente que "free"
free -h | grep Mem | awk '{print "Available:", $7}'

# Vider le cache (rarement nécessaire)
sync; echo 3 > /proc/sys/vm/drop_caches
```
