---
title: Availability target
tags:
  - beginner
---
# Availability target

## Parent
- [[SLO SLA SLI]]

---

## Définition

La cible de disponibilité (availability target) définit le pourcentage de temps pendant lequel un service doit fonctionner correctement. Elle est exprimée en "neuf" et détermine le budget d'erreur disponible.

---

## Table de disponibilité

| SLO | Downtime/mois | Downtime/an | Fenêtre downtime/jour |
|---|---|---|---|
| 99% | 7h 18min | 3j 15h | 14.4 min |
| 99.5% | 3h 39min | 1j 19h | 7.2 min |
| 99.9% | 43 min | 8h 45min | 1.44 min |
| 99.95% | 21 min | 4h 22min | 43 sec |
| 99.99% | 4.3 min | 52 min | 8.6 sec |
| 99.999% | 26 sec | 5 min | 0.86 sec |

---

## Choisir la bonne cible

```
Questions à se poser :
1. Quel est l'impact business d'une heure de downtime ?
2. Quel est le coût pour atteindre 99.99% vs 99.9% ?
3. Les dépendances peuvent-elles maintenir 99.99% ?

(Si une dépendance est à 99.9%, le service composé ne peut pas dépasser 99.9%)
```

---

> [!warning]
> Ne pas viser une disponibilité plus haute que celle de tes dépendances. Si tu dépends d'AWS S3 (99.9% SLA) et de la DB (99.95% SLA), tu ne peux pas garantir plus de 99.85% (multiplication des indisponibilités).
