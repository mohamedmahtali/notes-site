---
title: Manual trigger
tags:
  - intermediate
---
# Manual trigger

## Parent
- [[Pipeline triggers]]

---

## Définition

Le manual trigger permet de déclencher un pipeline (ou un stage spécifique) par une action humaine explicite, sans événement Git. Utilisé pour les déploiements en production, les rollbacks, ou les opérations ponctuelles.

---

## GitHub Actions — workflow_dispatch

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production
      confirm:
        description: 'Type DEPLOY to confirm'
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Validate confirmation
        run: |
          [ "${{ inputs.confirm }}" = "DEPLOY" ] || exit 1

      - name: Deploy
        run: ./deploy.sh ${{ inputs.environment }}
```

---

## GitLab CI — when: manual

```yaml
deploy:production:
  stage: deploy
  script:
    - ./deploy.sh production
  when: manual              # bouton dans l'UI GitLab
  allow_failure: false      # bloque le pipeline si non déclenché
  environment:
    name: production
```

---

> [!tip]
> Combiner le manual trigger avec des environment protection rules (GitHub) ou des protected environments (GitLab) pour limiter qui peut déclencher les déploiements en production.
