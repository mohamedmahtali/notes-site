---
title: Observability
tags:
  - observability
  - intermediate
---

# Observability (Observabilité)

## Définition

L'observabilité est la capacité à comprendre l'état interne d'un système à partir de ses sorties externes. Un système observable permet de répondre à la question "pourquoi ça ne marche pas ?" sans avoir à redéployer du code de debug.

> [!tip] Pourquoi c'est important
> Sans observabilité, les incidents en production sont des boîtes noires. L'observabilité réduit le MTTR (Mean Time To Recovery), permet la détection proactive des problèmes avant qu'ils impactent les utilisateurs, et aide à comprendre le comportement réel du système sous charge.

## Les 3 piliers

```
Metrics ──────── Qu'est-ce qui se passe ? (chiffres, tendances)
Logs ─────────── Que s'est-il passé exactement ? (événements)
Traces ───────── Comment une requête a traversé le système ?
```

| Pilier | Outil standard | Usage |
|--------|---------------|-------|
| [[Metrics]] | [[Monitoring/Prometheus\|Prometheus]] | [[Dashboards]], alertes, SLOs |
| [[Logging]] | [[Logging/Loki\|Loki]], ELK | Debug, audit, compliance |
| [[Tracing]] | Jaeger, Zipkin, [[Tracing/OpenTelemetry\|OpenTelemetry]] | Latence inter-[[Services]] |

## Concepts clés

- **[[SLO SLA SLI]]** — Définir et mesurer la fiabilité (99.9% uptime)
- **[[Grafana]]** — Visualisation unifiée metrics + logs + traces
- **[[Monitoring]]** — Collecte et analyse des métriques système/applicatif
- **Alerting** — Notification automatique sur seuils (PagerDuty, Slack)

## Les 4 Golden Signals (Google SRE)

| Signal | Définition |
|--------|-----------|
| **Latency** | Temps de réponse des requêtes |
| **Traffic** | Volume de requêtes par seconde |
| **Errors** | Taux d'erreurs (4xx, 5xx) |
| **Saturation** | Utilisation des ressources (CPU, RAM) |

## Liens

- [[Monitoring]]
- [[Logging]]
- [[Metrics]]
- [[Tracing]]
- [[Grafana]]
- [[SLO SLA SLI]]
