---
title: top
tags:
  - beginner
---

# top

## Parent
- [[Processes]]

---

## Définition

`top` est un outil de monitoring des processus en temps réel. Il affiche les processus triés par consommation CPU, et se rafraîchit toutes les 3 secondes par défaut.

---

## Utilisation

```bash
# Lancer top
top

# Options
top -u nginx         # filtrer par utilisateur
top -p 1234,5678    # surveiller des PIDs spécifiques
top -b -n 1         # mode batch (une capture, pour scripts)
top -b -n 1 | head -20 > snapshot.txt
```

---

## Raccourcis dans top

```
q        → quitter
k        → kill un processus (saisir le PID)
r        → renice (changer la priorité)
M        → trier par mémoire
P        → trier par CPU (défaut)
T        → trier par temps CPU
1        → afficher chaque CPU séparément
h        → aide
```

---

## Lire l'en-tête

```
top - 14:32:10  up 5 days,  2:14,  2 users,  load average: 0.42, 0.38, 0.35
Tasks: 132 total,   1 running, 131 sleeping
%Cpu(s):  2.1 us,  0.5 sy,  0.0 ni, 97.1 id,  0.3 wa
MiB Mem:  7952.0 total,  1234.5 free,  4521.3 used
```

| Métrique | Signification |
|---|---|
| load average | Charge moyenne sur 1/5/15 min |
| us | CPU user space |
| sy | CPU kernel |
| wa | Attente I/O disque |
| id | CPU idle |
