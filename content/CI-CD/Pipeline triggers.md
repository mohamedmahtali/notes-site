---
title: Pipeline triggers
tags:
  - intermediate
---
# Pipeline triggers

---

## Définition

Les [[Pipeline]] triggers définissent les événements qui déclenchent l'exécution d'un pipeline CI/CD. Un même repo peut avoir plusieurs triggers pour différents pipelines (CI rapide sur chaque PR, déploiement complet sur [[Merge]], nightly build le soir).

---

## Types de triggers

| Trigger | Événement | Usage typique |
|---|---|---|
| Push | [[Commit]] poussé | CI sur chaque branche |
| Pull/Merge Request | PR ouverte/mise à jour | Validation avant merge |
| Schedule | [[Cron]] expression | Nightly builds, scans |
| Manual | Clic humain | Déploiements prod |
| Webhook | Événement externe | Intégrations tierces |
| Tag | Tag [[Git]] créé | Release officielle |

---

## Configuration multi-triggers

```yaml
# GitHub Actions
on:
  push:
    branches: [main, 'release/*']
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 3 * * *'        # 3h chaque nuit
  workflow_dispatch:             # manuel
  release:
    types: [published]
```

---

> [!tip]
> Configurer des pipelines différents selon le trigger : pipeline léger (lint + [[Unit tests]]) sur chaque push, pipeline complet (e2e + deploy [[Staging]]) sur merge vers main seulement.
