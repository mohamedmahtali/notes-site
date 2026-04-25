---
title: GitHub actions
tags:
  - intermediate
---
# GitHub actions

---

## Définition

GitHub Actions est la plateforme CI/CD intégrée à GitHub. Les workflows sont définis en YAML dans `.github/workflows/` et déclenchés par des événements [[Git]] (push, PR, schedule). Elle est gratuite pour les repos publics, et inclut des minutes pour les repos privés.

---

## Pourquoi c'est important

> [!tip] CI/CD sans infrastructure à gérer
> GitHub Actions élimine le besoin d'héberger [[Jenkins]] ou un serveur CI. Les [[Runners]] GitHub-hosted (ubuntu-latest, windows-latest, macos-latest) sont provisionnés automatiquement pour chaque job.

---

## Structure d'un workflow

```yaml
# .github/workflows/ci.yml
name: CI Pipeline                    # nom affiché dans l'UI

on:                                  # événements déclencheurs
  push:
    branches: [main]
  pull_request:

env:                                 # variables globales
  NODE_VERSION: '20'

jobs:
  test:                              # nom du job
    runs-on: ubuntu-latest           # type de runner
    steps:
      - uses: actions/checkout@v4   # action réutilisable
      - name: Setup Node            # étape nommée
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
      - run: npm ci                 # commande shell
      - run: npm test
```

---

## Variables et secrets

```yaml
steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}            # secret GitHub
      ENVIRONMENT: ${{ vars.ENVIRONMENT }}        # variable de repo
      COMMIT_SHA: ${{ github.sha }}               # contexte GitHub
    run: ./deploy.sh
```

---

> [!note]
> Voir [[Workflows]], [[Jobs]], [[Steps]] pour approfondir chaque concept.
