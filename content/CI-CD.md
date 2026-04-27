---
title: CI/CD
tags:
  - intermediate
---
# CI/CD

---

## Définition

CI/CD (Continuous Integration / Continuous Delivery ou Deployment) est un ensemble de pratiques qui automatisent la construction, les tests et le déploiement du code. L'objectif : livrer des changements fréquemment, en toute confiance, avec un minimum d'intervention manuelle.

---

## Les trois piliers

| Pratique | Objectif | Fréquence |
|---|---|---|
| [[Continuous integration]] | Intégrer et tester chaque changement | À chaque [[Commit]] |
| [[Continuous delivery]] | Rendre chaque build deployable | À chaque [[Merge]] |
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

---

## Prérequis

Avant CI/CD, avoir de bonnes bases en : [[Git]] (branches, merge, pull requests), [[Docker]] (images, conteneurs).

---

## Explorer CI/CD

### Concepts fondamentaux
- **[[Continuous integration]]** — build et tests automatiques à chaque commit
- **[[Continuous delivery]]** — chaque build prêt à déployer en un clic
- **[[Continuous deployment]]** — déploiement automatique en production
- **[[Pipeline]]** — structure des stages (build, test, deploy)

### Outils
- **[[GitHub actions]]** — CI/CD natif GitHub, workflows YAML, marketplace
- **[[GitLab CI]]** — `.gitlab-ci.yml`, runners, stages, environments
- **[[Jenkins]]** — serveur CI auto-hébergé, Jenkinsfile, agents

### Optimisation & Opérations
- **[[Pipeline caching]]** — accélérer les builds en mettant en cache les dépendances
- **[[Artifacts]]** — gérer les sorties de build (images Docker, binaires, packages)
- **[[Pipeline triggers]]** — déclencher sur push, PR, schedule, API
- **[[Runners]]** — exécuteurs CI (self-hosted, shared, Docker executor)

> [!tip] Lab pratique
> → [[Lab CI-CD — Pipeline GitHub Actions complet]]

> [!note] Connexion
> → [[Git → CI-CD]] — du commit git au déploiement automatique
