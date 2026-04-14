---
title: Process scheduler
tags:
  - advanced
---

# Process scheduler

## Parent
- [[Kernel]]

---

## Définition

Le scheduler (ordonnanceur) du kernel Linux décide quel processus s'exécute sur quel CPU à chaque instant. Linux utilise le CFS (Completely Fair Scheduler) depuis 2.6.23, qui garantit une répartition équitable du CPU entre les processus.

---

## CFS (Completely Fair Scheduler)

```
- Chaque processus a un "virtual runtime" qui s'incrémente
- Le scheduler choisit toujours le processus avec le vruntime le plus bas
- Les processus à haute priorité (nice basse) s'incrémentent plus lentement
- Résultat : répartition équitable, faible latence
```

---

## Priorités et nice

```bash
# Voir la priorité des processus
ps -eo pid,ni,pri,cmd | head -10

# PRI = priorité réelle (calculée par kernel)
# NI = nice value (-20 à +19)
# PRI = 20 + NI (pour les processus normaux)

# Changer la priorité
nice -n 10 ./script.sh     # lancer avec nice +10
renice -n -5 -p PID        # modifier (root pour valeurs négatives)
```

---

## Classes de scheduling

```bash
# SCHED_OTHER (CFS) : processus normaux
# SCHED_FIFO : temps réel, FIFO
# SCHED_RR : temps réel, round-robin
# SCHED_IDLE : ultra basse priorité

# Voir la classe d'un processus
chrt -p PID

# Définir la classe temps réel
chrt -f -p 50 PID    # FIFO priorité 50
```
