---
title: Metrics
tags:
  - intermediate
---
# Metrics

## Parent
- [[Observability]]

## Enfants
- [[USE method]]
- [[RED method]]
- [[Infrastructure metrics]]
- [[Application metrics]]

---

## Définition

Les métriques sont des mesures numériques collectées périodiquement : CPU, mémoire, requêtes par seconde, taux d'erreur, latence. Elles donnent une vue quantitative de l'état du système au fil du temps.

---

## Types de métriques

| Type | Description | Exemple |
|---|---|---|
| Counter | Toujours croissant | Nombre de requêtes total |
| Gauge | Valeur instantanée | CPU actuel, connexions ouvertes |
| Histogram | Distribution de valeurs | Latences p50/p95/p99 |
| Summary | Quantiles calculés côté client | Identique histogram, moins flexible |

---

## Pourquoi c'est important

> [!tip] Les métriques répondent à "combien"
> Les métriques permettent de détecter les anomalies (spike de latence), de planifier la capacité, et de mesurer l'impact des déploiements. Les logs répondent à "pourquoi", les métriques à "combien" et "depuis quand".

---

> [!note]
> Voir [[USE method]] pour les métriques d'infra, [[RED method]] pour les métriques applicatives, [[Monitoring/Prometheus]] pour la collecte.
