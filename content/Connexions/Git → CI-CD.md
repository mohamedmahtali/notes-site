---
title: "Git → CI/CD : du commit au déploiement"
tags:
  - connexion
  - git
  - cicd
  - beginner
---

# Git → CI/CD : du commit au déploiement

## La connexion fondamentale

[[Git]] et [[CI-CD]] sont inséparables : un `git push` est le déclencheur universel de toute chaîne d'automatisation DevOps. Sans ce lien, CI/CD n'existe pas — c'est le commit qui met tout en mouvement.

```
Développeur
    │
    ▼
git commit -m "feat: add payment flow"
    │
    ▼
git push origin feature/payment
    │
    ▼  (webhook GitHub/GitLab)
┌─────────────────────────────────┐
│         Pipeline CI/CD          │
│                                 │
│  Build → Test → Lint → Scan     │
│              │                  │
│         (si succès)             │
│              ▼                  │
│  Package (image Docker)         │
│              ▼                  │
│  Deploy (staging → prod)        │
└─────────────────────────────────┘
```

## Ce que Git apporte à CI/CD

| Concept Git | Rôle dans CI/CD |
|------------|-----------------|
| **[[Branch]]** | Déclenche des pipelines différents (feature vs main) |
| **[[Pull request]]** | Exécute les checks avant merge (CI obligatoire) |
| **[[Commit]]** | Identifiant unique de chaque build (`SHA` = version) |
| **[[Git tags]]** | Déclenche les déploiements de release |
| **[[Git hooks]]** | Pre-commit local : lint, tests rapides avant push |

## En pratique — GitHub Actions

```yaml
# .github/workflows/ci.yml
on:
  push:
    branches: [main, 'feature/**']
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
      - run: docker build -t app:${{ github.sha }} .
```

Le `github.sha` est le hash du commit Git — chaque image Docker est ainsi tracée à son commit source.

## Flux par type de branche

```
feature/* → push → CI (build + test) seulement
main      → merge PR → CI + deploy staging
tag v*.*  → release → CI + deploy production
```

## Points d'attention

> [!warning] Ne pas bypasser les hooks
> `git push --no-verify` contourne les [[Git hooks]] et peut envoyer du code non testé directement dans le pipeline. À proscrire sur les branches protégées.

> [!tip] Commit message = contexte de déploiement
> Les messages de commit (`feat:`, `fix:`, `chore:`) permettent aux pipelines de [[CI-CD]] de générer des changelogs automatiques et de conditionner certaines étapes.

## Pour aller plus loin

- [[Commit message]] — conventions (Conventional Commits, semver)
- [[Git workflow]] — Git flow vs trunk-based, impact sur la stratégie CI/CD
- [[Pull request]] — protections de branches, required checks
- [[CI-CD]] — pipelines complets, artifacts, déploiements
