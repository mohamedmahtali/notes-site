---
title: Deploy stage
tags:
  - intermediate
---
# Deploy stage

## Parent
- [[Pipeline]]

## Enfants
- [[Staging]]
- [[Production]]
- [[Rollback]]

---

## Définition

Le deploy stage prend l'artefact validé par les tests et le déploie dans un ou plusieurs environnements. Un pipeline typique déploie d'abord en staging (automatiquement) puis en production (avec approbation manuelle ou automatique).

---

## Pourquoi c'est important

> [!tip] Déploiement = procédure codifiée
> Le deploy stage remplace les runbooks manuels par du code versionné. Chaque déploiement est identique, auditabl, et reproductible — plus de "ça marche sur mon poste".

---

## Exemple avec environnements

```yaml
deploy-staging:
  needs: test
  runs-on: ubuntu-latest
  environment: staging
  steps:
    - name: Deploy to staging
      run: |
        kubectl set image deployment/myapp           app=myregistry/myapp:${{ github.sha }}           --namespace=staging

deploy-production:
  needs: deploy-staging
  runs-on: ubuntu-latest
  environment:
    name: production
    url: https://myapp.com
  steps:
    - name: Deploy to production
      run: |
        kubectl set image deployment/myapp           app=myregistry/myapp:${{ github.sha }}           --namespace=production
```

---

> [!note]
> L'environnement `production` dans GitHub Actions peut nécessiter une approbation manuelle via les **environment protection rules**.
