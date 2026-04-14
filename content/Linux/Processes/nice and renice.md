---
title: nice and renice
tags:
  - intermediate
---

# nice and renice

## Parent
- [[Processes]]

---

## Définition

`nice` et `renice` contrôlent la priorité de scheduling des processus. La valeur nice va de -20 (priorité maximale) à +19 (priorité minimale). Plus la valeur est basse, plus le processus reçoit de temps CPU.

---

## Commandes

```bash
# Lancer avec une priorité réduite (tâche de fond)
nice -n 10 ./backup.sh
nice -n 19 ./compression-lourde.sh   # priorité minimale

# Lancer avec haute priorité (root requis pour valeurs négatives)
sudo nice -n -5 ./service-critique

# Changer la priorité d'un processus existant
renice 15 -p PID           # par PID
renice -n 10 -p $(pgrep backup)

# Voir la priorité des processus
ps -eo pid,ni,cmd | grep "mon-processus"
top   # colonne NI
```

---

## Valeurs recommandées

| Usage | Nice value |
|---|---|
| Services critiques | 0 (défaut) ou négatif (root) |
| Services normaux | 0 |
| Jobs batch, backup | +10 à +15 |
| Tâches très basses priorité | +19 |

---

> [!tip]
> Utiliser `nice +10` pour les scripts de backup et maintenance qui tournent en parallèle avec les services de production. Ça garantit que les services critiques gardent la priorité CPU.
