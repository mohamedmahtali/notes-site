---
title: Continuous integration
tags:
  - intermediate
---
# Continuous integration

## Parent
- [[CI-CD]]

## Enfants
- [[Automated build]]
- [[Automated tests]]
- [[Code quality checks]]

---

## Définition

L'intégration continue (CI) est la pratique d'intégrer fréquemment le code de tous les développeurs dans une branche partagée, avec validation automatisée à chaque push. L'objectif : détecter les conflits et les bugs au plus tôt.

---

## Pourquoi c'est important

> [!tip] Intégrer tôt, intégrer souvent
> Sans CI : les branches vivent des semaines séparément, les merge conflicts deviennent des cauchemars, et les bugs sont découverts tardivement. Avec CI : chaque commit est validé en quelques minutes, les problèmes sont détectés immédiatement.

---

## Principes fondamentaux

1. **Branche principale toujours verte** — le main/master doit toujours compiler et passer les tests
2. **Commits fréquents** — au moins une fois par jour, idéalement plusieurs fois
3. **Build rapide** — feedback en moins de 10 minutes
4. **Visibilité** — tout le monde voit le statut du build

---

## Exemple de workflow CI

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint
        run: npm run lint
      - name: Type check
        run: npm run type-check
      - name: Unit tests
        run: npm test -- --coverage
      - name: Build
        run: npm run build
```

---

> [!note]
> Voir [[Automated build]], [[Automated tests]], [[Code quality checks]] pour le détail de chaque composant CI.
