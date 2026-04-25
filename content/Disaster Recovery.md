---
title: Disaster Recovery
tags:
  - reliability
  - intermediate
---

# Disaster Recovery (DR)

## Définition

Le Disaster Recovery (reprise après sinistre) est l'ensemble des stratégies et processus permettant de restaurer les systèmes et données après un incident majeur : panne matérielle, erreur humaine, cyberattaque, catastrophe naturelle.

> [!warning] Pourquoi c'est critique
> Sans plan DR, un incident majeur peut signifier des jours d'arrêt, une perte de données irréversible et des dommages réputationnels. "It's not a matter of IF you'll have a disaster, but WHEN."

## Métriques clés

```
RTO (Recovery Time Objective)   → Combien de temps pour revenir en ligne ?
RPO (Recovery Point Objective)  → Combien de données peut-on perdre (en temps) ?

Exemple : RTO = 4h, RPO = 1h
→ On doit être opérationnel en 4h max
→ On peut perdre au max 1h de données (backups toutes les heures)
```

## Niveaux de DR

| Niveau | Description | RTO | RPO |
|--------|-------------|-----|-----|
| Backup & Restore | Sauvegarder et restaurer | 24h+ | 24h |
| Pilot light | Infrastructure minimale en veille | 4-8h | 1h |
| Warm standby | Replica réduit toujours actif | 30min-2h | Minutes |
| Multi-site active/active | Deux sites en production | Secondes | Zéro |

## Liens

- [[RTO RPO]]
- [[Backup strategies]]
- [[Chaos engineering]]
- [[Runbooks]]
- [[Incident response]]
- [[Incident Management]]
