---
title: Push trigger
tags:
  - beginner
---
# Push trigger

---

## Définition

Le push trigger déclenche un [[Pipeline]] à chaque `git push` vers les branches configurées. C'est le trigger le plus courant pour le CI — chaque [[Commit]] sur une branche de feature ou sur main déclenche la validation automatique.

---

## Configuration

```yaml
# GitHub Actions
on:
  push:
    branches:
      - main
      - develop
      - 'feature/**'
    paths:
      - 'src/**'           # seulement si src/ change
      - '**.py'
    tags:
      - 'v*'               # ou sur les tags de release

# GitLab CI
workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "push"
```

---

## Filtrage des paths

```yaml
# Ne pas déclencher pour des changements docs
on:
  push:
    paths-ignore:
      - '**.md'
      - 'docs/**'
      - '.github/ISSUE_TEMPLATE/**'
```

---

> [!tip]
> Utiliser `paths` pour éviter de lancer un pipeline complet quand seule la documentation change. Ça économise des minutes de build et réduit le bruit.
