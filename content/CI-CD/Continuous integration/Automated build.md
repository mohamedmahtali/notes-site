---
title: Automated build
tags:
  - beginner
---
# Automated build

---

## Définition

Un automated build compile automatiquement le code source à chaque [[Commit]] ou [[Pull request]], sans intervention humaine. Il valide que le code compile et produit un artefact utilisable.

---

## Pourquoi c'est important

> [!tip] La première ligne de défense
> Un build qui échoue = un problème détecté avant la revue de code. Même sans tests, un build automatisé empêche de merger du code qui ne compile pas.

---

## Exemple

```yaml
build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'
        cache: 'npm'

    - name: Install dependencies
      run: npm ci

    - name: Build
      run: npm run build

    - name: Upload build artifact
      uses: actions/upload-artifact@v4
      with:
        name: build-${{ github.sha }}
        path: dist/
```

---

> [!note]
> `npm ci` est préférable à `npm install` en CI : il utilise exactement le `package-lock.json` et échoue s'il y a une divergence.
