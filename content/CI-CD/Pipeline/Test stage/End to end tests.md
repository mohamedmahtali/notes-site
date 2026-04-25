---
title: End to end tests
tags:
  - advanced
---
# End to end tests

---

## Définition

Les tests end-to-end (e2e) simulent le comportement d'un utilisateur réel en interagissant avec l'application déployée via son interface (UI ou API). Ils valident les parcours utilisateur complets, de l'entrée à la sortie.

---

## Pourquoi c'est important

> [!warning] Lents mais essentiels
> Les e2e tests sont les plus lents (minutes à heures) et les plus fragiles (breakages sur changements UI). Mais ils sont les seuls à détecter les régressions de bout en bout. Les limiter aux parcours critiques (connexion, achat, checkout).

---

## Playwright en pipeline

```yaml
e2e:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    - name: Install Playwright
      run: npx playwright install --with-deps chromium

    - name: Start app
      run: docker compose up -d

    - name: Wait for app
      run: npx wait-on http://localhost:3000

    - name: Run e2e tests
      run: npx playwright test

    - name: Upload test artifacts
      if: failure()
      uses: actions/upload-artifact@v4
      with:
        name: playwright-report
        path: playwright-report/
```

---

> [!tip]
> Utiliser Playwright ou Cypress. Garder les e2e dans un stage séparé qui ne bloque pas le déploiement [[Staging]] — ils peuvent tourner en parallèle sur l'[[ENV]] de staging déjà déployé.
