---
title: Error budget
tags:
  - intermediate
---
# Error budget

## Parent
- [[SLO SLA SLI]]

---

## Définition

Le budget d'erreur est la quantité de downtime/erreurs "permise" par le SLO sur une période donnée. Avec un SLO de 99.9% sur 30 jours, le budget d'erreur est de 0.1% × 30 jours = 43 minutes.

---

## Calcul du budget d'erreur

```
Budget d'erreur = (1 - SLO) × période

Exemple : SLO 99.9% sur 30 jours
Budget = 0.001 × 30 × 24 × 60 = 43.2 minutes

Budget consommé par incident :
- Incident de 10 min = 23% du budget mensuel consommé
- Reste : 33.2 min pour le reste du mois
```

---

## Error budget en PromQL

```promql
# Budget consommé (sur les 30 derniers jours)
1 - (
  sum_over_time(http_success_rate[30d:5m])
  / (30 * 24 * 60 / 5)   # nombre de points sur 30 jours
)

# % de budget restant
(1 - slo_target) - error_budget_consumed
/ (1 - slo_target) * 100
```

---

## Décisions basées sur le budget

```
Budget > 50% restant → Déploiements agressifs, expériences autorisées
Budget 25-50% restant → Prudence, focus stabilité
Budget < 25% restant → Gel des déploiements, focus fiabilité
Budget épuisé → Incidente majeur déclaré, post-mortem requis
```

---

> [!tip]
> Le budget d'erreur est un outil de décision puissant : si le budget est plein, l'équipe peut prendre des risques (nouvelles fonctionnalités, refactoring). Si le budget est épuisé, la priorité est la fiabilité.
