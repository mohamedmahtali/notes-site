---
title: Schedule trigger
tags:
  - intermediate
---
# Schedule trigger

## Parent
- [[Pipeline triggers]]

---

## Définition

Le schedule trigger déclenche un pipeline selon une expression cron, indépendamment des pushs de code. Utile pour les nightly builds, les scans de sécurité périodiques, les tests de performance réguliers.

---

## Cas d'usage

- **Nightly builds** : build + tests complets à 2h du matin
- **Security scans** : scan de CVE quotidien sur les images en production
- **Performance baselines** : benchmark hebdomadaire
- **Cleanup** : purge des artefacts anciens chaque dimanche

---

## GitHub Actions

```yaml
on:
  schedule:
    # Chaque jour à 3h UTC (éviter les heures pleines)
    - cron: '0 3 * * *'
    # Chaque lundi à 9h
    - cron: '0 9 * * 1'

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Scan production image
        run: |
          trivy image --severity HIGH,CRITICAL             myregistry/myapp:production
```

---

## GitLab CI

```yaml
nightly-test:
  script:
    - npm run test:full
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
  only:
    - schedules    # déclenché uniquement par un schedule
```

---

> [!tip]
> Utiliser des heures UTC décalées (3h, 4h) pour les scheduled builds. Éviter minuit et les heures rondes — beaucoup de services déclenchent leurs maintenances à ces heures.
