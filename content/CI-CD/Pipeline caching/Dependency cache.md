---
title: Dependency cache
tags:
  - intermediate
---
# Dependency cache

---

## Définition

Le dependency cache conserve les [[Package]] installés (node_modules, pip packages, Maven [[Artifacts]], Go [[Modules]]) entre les runs CI pour éviter de les télécharger à chaque build.

---

## Par gestionnaire de packages

```yaml
# Node.js (npm)
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'

# Python (pip)
- uses: actions/setup-python@v5
  with:
    python-version: '3.12'
    cache: 'pip'

# Go modules
- uses: actions/cache@v3
  with:
    path: |
      ~/go/pkg/mod
      ~/.cache/go-build
    key: ${{ runner.os }}-go-${{ hashFiles('**/go.sum') }}

# Maven
- uses: actions/cache@v3
  with:
    path: ~/.m2/repository
    key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
```

---

## GitLab CI

```yaml
test:
  cache:
    key:
      files:
        - package-lock.json    # cache invalidé si ce fichier change
    paths:
      - node_modules/
    policy: pull-push           # lire ET écrire le cache
```

---

> [!warning]
> Toujours inclure le fichier de lock dans la cache key. Sinon, les dépendances mises à jour peuvent être ignorées et le cache corrompu servi à la place.
