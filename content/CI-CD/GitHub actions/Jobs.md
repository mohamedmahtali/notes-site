---
title: Jobs
tags:
  - intermediate
---
# Jobs

## Parent
- [[GitHub actions]]

---

## Définition

Un job est un ensemble de steps qui s'exécutent sur le même runner. Par défaut, les jobs tournent en parallèle. L'ordre peut être contrôlé avec `needs`. Chaque job a son propre environnement isolé.

---

## Jobs parallèles et séquentiels

```yaml
jobs:
  lint:                          # tourne en parallèle avec test
    runs-on: ubuntu-latest
    steps:
      - run: npm run lint

  test:                          # tourne en parallèle avec lint
    runs-on: ubuntu-latest
    steps:
      - run: npm test

  build:
    needs: [lint, test]          # attend lint ET test
    runs-on: ubuntu-latest
    steps:
      - run: npm run build

  deploy:
    needs: build                 # attend build seulement
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

---

## Matrix strategy

```yaml
test:
  strategy:
    matrix:
      os: [ubuntu-latest, windows-latest]
      node: ['18', '20', '22']
      exclude:
        - os: windows-latest
          node: '18'
    fail-fast: false              # continuer même si une combinaison échoue

  runs-on: ${{ matrix.os }}
  steps:
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node }}
    - run: npm test
```

---

## Conditions

```yaml
deploy:
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  runs-on: ubuntu-latest
```
