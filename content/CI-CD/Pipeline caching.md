---
title: Pipeline caching
tags:
  - intermediate
---
# Pipeline caching

---

## Définition

Le [[Pipeline]] caching conserve les résultats d'étapes coûteuses (installation de dépendances, compilation) entre les runs du pipeline pour accélérer les builds. Un bon cache peut réduire le temps de build de 10 minutes à 2 minutes.

---

## Pourquoi c'est important

> [!tip] npm install ne devrait prendre que quelques secondes
> Sans cache, chaque run installe toutes les dépendances [[FROM]] scratch. Avec cache : si `package-lock.json` n'a pas changé, les `node_modules` sont restaurés en secondes depuis le cache.

---

## Stratégie de cache key

```yaml
# Bonne clé de cache : hash du fichier de lock
key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}

# Si package-lock.json change → cache miss → réinstallation
# Si pas de changement → cache hit → restauration rapide
```

---

## GitHub Actions

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-

# Ou utiliser actions/setup-node avec cache intégré
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'            # cache automatique
```

---

> [!note]
> Voir [[Dependency cache]] pour les détails par gestionnaire de [[Package]], [[Docker layer cache]] pour le cache des builds [[Docker]].

## Explorer

- **[[Pipeline]]** — structure complète du pipeline CI/CD
- **[[Build stage]]** — étape de build où le cache est le plus utile
- **[[Pipeline triggers]]** — déclencheurs qui créent de nouveaux runs
