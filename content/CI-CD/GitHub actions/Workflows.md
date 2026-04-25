---
title: Workflows
tags:
  - intermediate
---
# Workflows

---

## Définition

Un workflow [[GitHub actions]] est un processus automatisé défini dans un fichier YAML sous `.github/workflows/`. Chaque repo peut avoir plusieurs workflows déclenchés par des événements différents.

---

## Événements déclencheurs

```yaml
on:
  push:                          # push sur une branche
    branches: [main, develop]
    paths: ['src/**', '**.py']   # seulement si ces fichiers changent

  pull_request:                  # ouverture/mise à jour d'une PR
    types: [opened, synchronize, reopened]
    branches: [main]

  schedule:                      # cron
    - cron: '0 2 * * 1'         # chaque lundi à 2h

  workflow_dispatch:             # déclenchement manuel
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
        type: choice
        options: [staging, production]

  release:                       # lors d'une release GitHub
    types: [published]
```

---

## Workflow réutilisable

```yaml
# .github/workflows/reusable-deploy.yml
on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string

# Dans un autre workflow
jobs:
  deploy:
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: production
    secrets: inherit
```

---

> [!tip]
> Utiliser `paths` pour ne déclencher le workflow que si les fichiers pertinents changent — ça évite de tourner le [[Pipeline]] complet pour une modification de README.
