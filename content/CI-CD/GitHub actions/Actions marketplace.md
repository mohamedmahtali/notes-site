---
title: Actions marketplace
tags:
  - beginner
---
# Actions marketplace

## Parent
- [[GitHub actions]]

---

## Définition

Le GitHub Actions Marketplace est un catalogue d'actions réutilisables créées par GitHub et la communauté. Ces actions encapsulent des tâches courantes (checkout, setup langages, déploiement) pour éviter d'écrire des scripts from scratch.

---

## Actions essentielles

```yaml
# Checkout du code
- uses: actions/checkout@v4
  with:
    fetch-depth: 0      # historique complet (pour semantic-release)

# Setup Node.js avec cache npm
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'

# Setup Python
- uses: actions/setup-python@v5
  with:
    python-version: '3.12'
    cache: 'pip'

# Cache général
- uses: actions/cache@v3
  with:
    path: ~/.cache
    key: ${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}

# Upload artefacts
- uses: actions/upload-artifact@v4
  with:
    name: build
    path: dist/
    retention-days: 7

# Docker Build & Push
- uses: docker/build-push-action@v5
  with:
    push: true
    tags: myimage:latest
```

---

## Créer sa propre action

```yaml
# action.yml (dans un repo dédié)
name: 'My Custom Action'
inputs:
  environment:
    required: true
runs:
  using: 'composite'
  steps:
    - run: ./deploy.sh ${{ inputs.environment }}
      shell: bash
```

---

> [!warning]
> Toujours épingler les actions à une version spécifique (`@v4`) ou un SHA pour éviter des changements non intentionnels. Éviter `@latest` en production.
