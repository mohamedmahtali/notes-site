---
title: Staging
tags:
  - intermediate
---
# Staging

## Parent
- [[Deploy stage]]

---

## Définition

L'environnement de staging est une réplique de la production où les déploiements automatiques atterrissent avant la production. Il sert à valider le comportement réel de l'application avec des données réalistes.

---

## Pourquoi c'est important

> [!tip] La dernière ligne de défense avant la prod
> Staging est là pour attraper les problèmes qui passent à travers les tests automatisés : problèmes de configuration, de performance, d'intégration avec des services tiers, ou de comportement sous charge réelle.

---

## Bonnes pratiques

```yaml
deploy-staging:
  needs: [build, test]
  runs-on: ubuntu-latest
  environment:
    name: staging
    url: https://staging.myapp.com
  steps:
    - name: Deploy
      run: |
        helm upgrade --install myapp ./chart           --namespace staging           --set image.tag=${{ github.sha }}           --set replicas=1           --values values.staging.yaml

    - name: Smoke test
      run: |
        sleep 30
        curl -f https://staging.myapp.com/health || exit 1
```

---

## Différences staging vs prod

| Aspect | Staging | Production |
|---|---|---|
| Déploiement | Automatique | Manuel/protégé |
| Données | Anonymisées | Réelles |
| Réplicas | 1 | 3+ |
| Monitoring | Basique | Complet |
