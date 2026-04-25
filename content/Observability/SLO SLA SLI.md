---
title: SLO SLA SLI
tags:
  - intermediate
---
# SLO SLA SLI

---

## Définition

SLI, SLO et SLA sont les trois niveaux de mesure de la fiabilité d'un service, popularisés par le Google SRE book.

---

## Les trois concepts

| Terme | Définition | Exemple |
|---|---|---|
| **SLI** | Service Level Indicator — métrique de fiabilité | Taux de requêtes réussies = 99.5% |
| **SLO** | Service Level Objective — objectif cible | SLI doit être ≥ 99.9% sur 30 jours |
| **SLA** | Service Level Agreement — contrat avec pénalités | Disponibilité garantie 99.5% ou remboursement |

---

## SLIs courants

```promql
# Availability SLI
sum(rate(http_requests_total{status!~"5.."}[5m]))
/ sum(rate(http_requests_total[5m]))

# Latency SLI — % de requêtes < 200ms
sum(rate(http_request_duration_seconds_bucket{le="0.2"}[5m]))
/ sum(rate(http_request_duration_seconds_count[5m]))
```

---

## Choisir un SLO

```
99.9%   = 8.7h downtime/an   (trois neuf)
99.99%  = 52 min downtime/an (quatre neuf)
99.999% = 5 min downtime/an  (cinq neuf)

Règle pratique :
- API publique externe  → 99.9%
- Service critique      → 99.95%
- Infrastructure core   → 99.99%
- Ne pas viser 100%     → impossible et trop cher
```

---

> [!note]
> Voir [[Error budget]] pour comprendre comment gérer la "marge d'erreur" d'un SLO, [[Availability target]] pour calculer les fenêtres de downtime acceptable.
