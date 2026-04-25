---
title: Merge request trigger
tags:
  - intermediate
---
# Merge request trigger

---

## Définition

Le [[Merge]] request trigger (ou [[Pull request]] trigger) déclenche un [[Pipeline]] chaque fois qu'une PR/MR est ouverte, mise à jour, ou rouverte. C'est le gate de qualité avant qu'un changement ne soit intégré dans la branche principale.

---

## Pourquoi c'est important

> [!tip] Valider avant de merger
> Le pipeline PR est le dernier filet de sécurité avant l'intégration. Configurer des [[Branch]] protection rules pour exiger que ce pipeline soit vert avant de permettre le merge.

---

## GitHub Actions

```yaml
on:
  pull_request:
    branches: [main, develop]
    types:
      - opened
      - synchronize    # nouveau commit dans la PR
      - reopened
    paths:
      - 'src/**'
```

---

## GitLab CI

```yaml
workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  rules:
    - if: $CI_MERGE_REQUEST_ID      # seulement en MR
```

---

## Branch protection (GitHub)

```
Settings → Branches → Add rule → "main"
☑ Require status checks to pass before merging
☑ Require branches to be up to date before merging
Status checks required: [CI / test, CI / build]
```

---

> [!note]
> Le pipeline PR peut être différent (plus léger) du pipeline post-merge. Exemple : lint + [[Unit tests]] en PR, déploiement [[Staging]] sur merge vers main.
