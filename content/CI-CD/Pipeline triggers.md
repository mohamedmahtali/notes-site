---
title: Pipeline triggers
tags:
  - intermediate
---
# Pipeline triggers

## Définition

Les Pipeline triggers définissent les événements qui déclenchent l'exécution d'un pipeline CI/CD. Un même repo peut avoir plusieurs triggers pour différents pipelines (CI rapide sur chaque PR, déploiement complet sur merge, nightly build le soir).

## Types de triggers

| Trigger | Événement | Usage typique |
|---|---|---|
| Push | Commit poussé | CI sur chaque branche |
| Pull/Merge Request | PR ouverte/mise à jour | Validation avant merge |
| Schedule | Cron expression | Nightly builds, scans de sécurité |
| Manual | Clic humain | Déploiements en production |
| Webhook | Événement externe | Intégrations tierces |
| Tag | Tag Git créé | Release officielle |

## GitHub Actions

```yaml
on:
  push:
    branches: [main, 'release/*']
    paths:
      - 'src/**'           # uniquement si le code source change
      - 'Dockerfile'
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 3 * * *'   # 3h chaque nuit (UTC)
  workflow_dispatch:        # déclenchement manuel depuis l'UI
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
  release:
    types: [published]      # à la publication d'une release GitHub
```

## GitLab CI

```yaml
# gitlab-ci.yml
workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == "main"
    - if: $CI_COMMIT_TAG

deploy-prod:
  stage: deploy
  rules:
    - if: $CI_COMMIT_TAG =~ /^v\d+\.\d+\.\d+$/   # tag semver uniquement
      when: manual
  script:
    - ./deploy.sh production

nightly-scan:
  stage: security
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
  script:
    - trivy image $CI_REGISTRY_IMAGE:latest
```

## Stratégie par branche

```
feature/* → push → pipeline léger (lint + unit tests, ~2 min)
main      → merge → pipeline complet (build + e2e + deploy staging, ~10 min)
v*.*.*    → tag   → pipeline release (build + deploy prod, manuel)
nightly   → cron  → pipeline sécurité (scan CVE, dépendances, ~5 min)
```

> [!tip]
> Filtrer par `paths` sur GitHub Actions (ou `changes` sur GitLab) pour éviter de déclencher un pipeline complet quand seul un fichier README change.

## Explorer

- **[[Pipeline]]** — structure complète d'un pipeline CI/CD
- **[[Pipeline caching]]** — accélérer les builds entre les runs
- **[[Git workflow]]** — stratégies de branches (trunk-based, gitflow)
- **[[Git → CI-CD]]** — comment Git alimente les pipelines
