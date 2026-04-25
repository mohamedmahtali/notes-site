---
title: Continuous delivery
tags:
  - intermediate
---
# Continuous delivery

---

## Définition

La livraison continue (CD) s'assure que chaque build validé est **prêt à être déployé** en production à tout moment. Le déploiement lui-même reste une décision humaine — c'est la différence avec le déploiement continu.

---

## Pourquoi c'est important

> [!tip] Déployer quand on veut, pas quand on peut
> La livraison continue élimine la peur du déploiement. Chaque version est testée, documentée, et deployable en un clic. Les équipes business peuvent choisir le moment du déploiement sans dépendre d'un "jour de release".

---

## Workflow livraison continue

```
Code → CI (build + test) → Staging deploy → Manual approval → Prod deploy
```

```yaml
release:
  needs: [test, deploy-staging]
  runs-on: ubuntu-latest
  environment:
    name: production          # déclenche l'approbation manuelle
    url: https://myapp.com
  steps:
    - name: Deploy to production
      run: helm upgrade myapp ./chart --set image.tag=${{ github.sha }}
```

---

## Critères de "release readiness"

- ✅ Tous les tests passent (unit, intégration, e2e)
- ✅ [[Staging]] déployé et smoke tests verts
- ✅ Pas de vulnérabilités critiques
- ✅ Documentation à jour
- ✅ Métriques de performance dans les seuils

---

> [!note]
> Voir [[Continuous deployment]] pour l'automatisation complète sans approbation manuelle.
