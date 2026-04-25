---
title: Crontab syntax
tags:
  - intermediate
---

# Crontab syntax

---

## Définition

La syntaxe crontab définit l'horaire d'exécution des tâches via 5 champs : minute, heure, jour du mois, mois, jour de la semaine.

---

## Format

```
MIN  HEURE  JOUR_MOIS  MOIS  JOUR_SEMAINE  COMMANDE
 │     │        │        │       │
 │     │        │        │       └── 0-7 (0 et 7=dim, 1=lun)
 │     │        │        └────────── 1-12
 │     │        └─────────────────── 1-31
 │     └──────────────────────────── 0-23
 └────────────────────────────────── 0-59

* = toute valeur
*/5 = toutes les 5 unités
1,15 = le 1er et le 15
1-5 = de 1 à 5
```

---

## Exemples

```cron
# Chaque minute
* * * * * /script.sh

# Toutes les 5 minutes
*/5 * * * * /script.sh

# Chaque jour à minuit
0 0 * * * /script.sh

# Chaque lundi à 9h
0 9 * * 1 /script.sh

# Le 1er de chaque mois à 2h30
30 2 1 * * /script.sh

# Du lundi au vendredi à 8h
0 8 * * 1-5 /script.sh
```

---

## Raccourcis

```cron
@reboot   → au démarrage
@daily    → 0 0 * * *
@weekly   → 0 0 * * 0
@monthly  → 0 0 1 * *
@hourly   → 0 * * * *
```

---

> [!tip]
> Utiliser [crontab.guru](https://crontab.guru) pour valider et visualiser une expression [[Cron]].
