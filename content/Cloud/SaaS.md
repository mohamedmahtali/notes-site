---
title: SaaS
tags:
  - beginner
---
# SaaS

---

## Définition

Software as a Service : le provider gère tout — infra, OS, runtime, application. Tu utilises le logiciel via un navigateur ou une API. Pas de déploiement, pas de maintenance.

---

## Exemples SaaS DevOps

| Produit | Usage |
|---|---|
| GitHub / GitLab.com | Code hosting, CI/CD |
| Datadog | [[Monitoring]] |
| PagerDuty | Alerting/on-call |
| Snyk | [[Security]] scanning |
| [[Terraform]] [[Cloud]] | IaC state management |
| [[Grafana]] Cloud | [[Observability]] |
| Slack | Communication |

---

## Modèle de responsabilité SaaS

```
Tu es responsable de :
- Les données que tu soumets
- Les accès utilisateurs (IAM/SSO)
- La configuration de l'application
- L'intégration avec tes systèmes

Le provider est responsable de :
- L'infrastructure
- La disponibilité (SLA)
- Les mises à jour
- La sécurité de la plateforme
```

---

> [!tip]
> Pour les outils [[DevOps]] internes, évaluer SaaS vs self-hosted (ex: GitHub vs GitLab self-hosted, Datadog vs stack ELK). SaaS = moins de maintenance, plus cher ; self-hosted = contrôle total, overhead opérationnel.
