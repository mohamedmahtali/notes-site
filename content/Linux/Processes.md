---
title: Processes
tags:
  - beginner
---

# Processes

## Parent
- [[Linux]]

## Enfants
- [[ps]]
- [[top]]
- [[htop]]
- [[Signals]]
- [[nice and renice]]
- [[Foreground and background]]

---

## Définition

Un processus est un programme en cours d'exécution. Chaque processus a un PID (Process ID) unique, un PPID (Parent PID), un utilisateur propriétaire, et consomme des ressources CPU/mémoire. Le kernel Linux orchestre leur exécution via le scheduler.

---

## Commandes essentielles

```bash
# Lister les processus
ps aux                    # tous les processus
ps aux | grep nginx       # filtrer
pgrep -la nginx           # chercher par nom

# Monitoring temps réel
top                       # classique
htop                      # version améliorée

# Tuer un processus
kill PID                  # SIGTERM (arrêt propre)
kill -9 PID               # SIGKILL (immédiat)
killall nginx             # tuer par nom
pkill -f "node server"    # tuer par pattern

# PID d'un processus
pidof nginx
pgrep nginx

# Informations détaillées
cat /proc/PID/status
ls -la /proc/PID/
```

---

## Hiérarchie des processus

```bash
# Voir l'arbre des processus
pstree
pstree -p    # avec PIDs
```

---

## Ressources

```bash
# Utilisation mémoire d'un processus
cat /proc/PID/status | grep VmRSS

# Fichiers ouverts par un processus
lsof -p PID

# Ports utilisés par un processus
ss -tlnp | grep PID
```
