---
title: Steps
tags:
  - beginner
---
# Steps

## Parent
- [[GitHub actions]]

---

## Définition

Les steps sont les instructions individuelles d'un job. Chaque step est soit une commande shell (`run`), soit une action réutilisable (`uses`). Ils s'exécutent séquentiellement sur le même runner et partagent le même filesystem.

---

## Types de steps

```yaml
steps:
  # Action GitHub Marketplace
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0

  # Commande shell
  - name: Install dependencies
    run: npm ci

  # Script multi-lignes
  - name: Build and tag
    run: |
      npm run build
      docker build -t myapp:${{ github.sha }} .
      docker push myapp:${{ github.sha }}

  # Step conditionnel
  - name: Deploy
    if: github.ref == 'refs/heads/main'
    run: ./deploy.sh

  # Step avec timeout
  - name: Long running test
    timeout-minutes: 30
    run: npm run test:e2e

  # Continuer même si échec
  - name: Upload results
    if: always()
    uses: actions/upload-artifact@v4
    with:
      name: test-results
      path: results/
```

---

## Outputs entre steps

```yaml
- name: Get version
  id: version
  run: echo "tag=$(git describe --tags)" >> $GITHUB_OUTPUT

- name: Use version
  run: echo "Deploying version ${{ steps.version.outputs.tag }}"
```
