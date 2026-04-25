---
title: RTO et RPO
tags:
  - reliability
  - intermediate
---

# RTO et RPO

## Définition

- **RTO (Recovery Time Objective)** : durée maximale acceptable d'interruption de service après un incident. "Dans combien de temps doit-on être de nouveau opérationnel ?"
- **RPO (Recovery Point Objective)** : quantité maximale de données qu'on accepte de perdre, exprimée en temps. "Jusqu'à quand on peut remonter dans les données ?"

> [!tip] RTO et RPO pilotent l'architecture DR
> Un RTO de 4h autorise une restauration manuelle depuis des backups. Un RTO de 30 secondes impose une réplication en temps réel et un basculement automatique.

## Relation RTO/RPO et coût

```
Disponibilité    RTO        RPO        Coût
─────────────────────────────────────────────
99%              72h        24h        Faible
99.9%            8h         1h         Moyen
99.99%           1h         15min      Élevé
99.999%          5min       1min       Très élevé
Active/Active    ~0         ~0         Maximal
```

## Calculer ses besoins

```
Questions à se poser :
1. Combien coûte 1h d'arrêt ? (pertes financières, SLA pénalités)
2. Quelle est la fréquence des transactions ? (→ RPO)
3. Combien de temps pour restaurer manuellement ? (→ RTO actuel)
4. Quel est le budget DR acceptable ?
```

## Documenter les SLOs de DR

```yaml
# Exemple de DR objectives par service
services:
  payment-api:
    rto: 30m
    rpo: 5m
    tier: critical

  user-dashboard:
    rto: 4h
    rpo: 1h
    tier: standard

  analytics:
    rto: 24h
    rpo: 24h
    tier: low
```

## Liens

- [[Disaster Recovery]]
- [[Backup strategies]]
- [[Incident response]]
