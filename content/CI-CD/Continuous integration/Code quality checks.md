---
title: Code quality checks
tags:
  - intermediate
---
# Code quality checks

## Parent
- [[Continuous integration]]

---

## Définition

Les code quality checks automatisés vérifient le style (linting), les types statiques, la couverture de tests, et la complexité cyclomatique. Ils maintiennent la qualité du code sans revue manuelle exhaustive.

---

## Outils courants

| Vérification | Outil JS/TS | Outil Python | Outil Go |
|---|---|---|---|
| Linting | ESLint, Biome | Ruff, flake8 | golangci-lint |
| Formatage | Prettier | Black, isort | gofmt |
| Types | TypeScript | mypy, pyright | natif |
| Couverture | Jest --coverage | pytest-cov | go test -cover |
| Complexité | complexity-report | radon | gocyclo |

---

## Exemple pipeline

```yaml
quality:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - run: npm ci

    - name: Lint
      run: npx eslint . --max-warnings 0

    - name: Type check
      run: npx tsc --noEmit

    - name: Format check
      run: npx prettier --check .

    - name: Check coverage threshold
      run: |
        npm test -- --coverage --coverageThreshold='
          {"global":{"branches":70,"functions":70,"lines":80}}'
```

---

> [!tip]
> Configurer des gates de qualité (quality gates) : le pipeline échoue si la couverture descend sous 70%, ou si ESLint trouve des erreurs. Pas d'exceptions — ça crée une dette technique invisible.
