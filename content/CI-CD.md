---
title: CI/CD
tags:
  - intermediate
---
# CI/CD

## Parent
- [[DevOps]]

## Enfants
- [[Pipeline]]
- [[Continuous integration]]
- [[Continuous delivery]]
- [[Continuous deployment]]
- [[GitHub actions]]
- [[GitLab CI]]
- [[Jenkins]]
- [[Runners]]
- [[Artifacts]]
- [[Pipeline triggers]]
- [[Pipeline caching]]

---

## Définition

CI/CD (Continuous Integration / Continuous Delivery ou Deployment) est un ensemble de pratiques qui automatisent la construction, les tests et le déploiement du code. L'objectif : livrer des changements fréquemment, en toute confiance, avec un minimum d'intervention manuelle.

---

## Les trois piliers

| Pratique | Objectif | Fréquence |
|---|---|---|
| [[Continuous integration]] | Intégrer et tester chaque changement | À chaque commit |
| [[Continuous delivery]] | Rendre chaque build deployable | À chaque merge |
| [[Continuous deployment]] | Déployer automatiquement en prod | À chaque merge validé |

---

## Pourquoi c'est important

> [!tip] De semaines à minutes
> Sans CI/CD : intégration mensuelle douloureuse, bugs découverts tard, déploiements manuels risqués. Avec CI/CD : feedback en minutes, bugs détectés immédiatement, déploiements répétables et auditables.

---

## Flux typique

```
Code push → CI Pipeline
    ├── Build (compile, containerize)
    ├── Test (unit, integration, e2e, security)
    ├── Quality gates (coverage, linting)
    └── Artifact (image Docker, binary, package)
         ↓ CD Pipeline
    ├── Deploy staging → tests manuels / smoke tests
    ├── Approval (manuel ou automatique)
    └── Deploy production → monitoring
```

---

> [!note]
> Voir [[GitHub actions]] et [[GitLab CI]] pour les implémentations concrètes, [[Pipeline]] pour la structure détaillée des stages.
