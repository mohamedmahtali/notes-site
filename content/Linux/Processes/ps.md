---
title: ps
tags:
  - beginner
---

# ps

## Parent
- [[Processes]]

---

## Définition

`ps` (process status) affiche un snapshot des processus actifs. C'est la commande de base pour voir quels processus tournent, leur PID, leur état, et leur consommation.

---

## Commandes

```bash
# Tous les processus (format BSD)
ps aux

# Tous les processus (format Unix)
ps -ef

# Chercher un processus
ps aux | grep nginx
ps -ef | grep python

# Processus d'un utilisateur
ps -u www-data

# Format personnalisé
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -10

# Processus fils d'un PID
ps --ppid 1234
```

---

## Colonnes importantes

```
USER    PID  %CPU %MEM    VSZ   RSS  STAT  COMMAND
root      1   0.0  0.1  16952  1212  Ss    /sbin/init
www      123  2.1  5.3 512345 54321  S     nginx: worker
```

| Colonne | Signification |
|---|---|
| PID | Process ID |
| %CPU | % CPU utilisé |
| %MEM | % mémoire physique utilisée |
| RSS | Mémoire résidente (ko) |
| STAT | État (S=sleeping, R=running, Z=zombie, D=disk wait) |
| VSZ | Mémoire virtuelle totale |
