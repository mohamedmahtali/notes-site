---
title: Game days
tags:
  - reliability
  - intermediate
---

# Game days

## Définition

Un "game day" est un exercice planifié où une équipe simule intentionnellement un incident majeur pour tester les plans de réponse, les runbooks, et la coordination des équipes. C'est un entraînement à la réponse aux incidents.

> [!tip] Pourquoi faire des game days ?
> Un incident réel est le pire moment pour découvrir que le runbook est obsolète, que les accès de prod sont mal configurés, ou que personne ne sait comment scaler la base de données. Les game days révèlent ces problèmes sans la pression d'une vraie crise.

## Organisation d'un game day

```
1. Préparer le scénario (ex: "perte de la région AWS us-east-1")
2. Définir les objectifs (tester le failover, mesurer le RTO réel)
3. Notifier les parties prenantes (support, management)
4. Exécuter l'exercice (injecter la panne)
5. Observer et mesurer (RTO réel vs objectif, points de blocage)
6. Débriefing (postmortem, actions correctives)
```

## Scénarios typiques

| Scénario | Ce qu'on teste |
|----------|---------------|
| Perte d'une zone de disponibilité | Failover automatique |
| Base de données primaire down | Basculement replica, RTO |
| Disque plein sur les workers | Alertes, remédiation |
| Certificat [[TLS]] expiré | Détection, rotation |
| Déploiement raté en production | [[Rollback]], communication |
| Clé [[SSH]] compromise | Rotation d'accès, audit |

## Liens

- [[Chaos engineering]]
- [[Failure injection]]
- [[Runbooks]]
- [[Incident response]]
