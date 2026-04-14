---
title: Logging
tags:
  - intermediate
---
# Logging

## Parent
- [[Observability]]

## Enfants
- [[Structured logs]]
- [[Centralized logging]]
- [[Loki]]
- [[Log retention]]

---

## Définition

Les logs sont des enregistrements textuels d'événements dans un système. Ils répondent à "pourquoi" un problème s'est produit — complément des métriques qui répondent à "combien". Les logs modernes sont structurés (JSON) et centralisés.

---

## Niveaux de log

| Niveau | Usage |
|---|---|
| DEBUG | Diagnostic détaillé (dev uniquement) |
| INFO | Événements normaux du business |
| WARNING | Situation anormale mais non bloquante |
| ERROR | Erreur récupérable |
| CRITICAL | Erreur fatale, service indisponible |

---

## Pourquoi c'est important

> [!tip] Les logs pour le "pourquoi"
> Quand Prometheus détecte une anomalie (spike d'erreurs), les logs permettent de comprendre pourquoi : quelle requête a échoué, quelle exception a été levée, quel utilisateur était concerné.

---

> [!note]
> Voir [[Structured logs]] pour le format JSON, [[Centralized logging]] pour la collecte, [[Loki]] pour la stack Grafana.
