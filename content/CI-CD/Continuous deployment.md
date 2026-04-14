---
title: Continuous deployment
tags:
  - advanced
---
# Continuous deployment

## Parent
- [[CI-CD]]

## Enfants
- [[Progressive rollout]]
- [[Automated release]]

---

## Définition

Le déploiement continu (CD) va plus loin que la livraison continue : chaque commit qui passe tous les tests est **automatiquement déployé en production**, sans approbation manuelle. Nécessite une confiance totale dans le pipeline de tests.

---

## Pourquoi c'est important

> [!tip] Des dizaines de déploiements par jour
> Des entreprises comme Amazon déploient en production des milliers de fois par jour. C'est possible grâce au déploiement continu : chaque changement est petit, testé, et deployé immédiatement. Les gros "release days" risqués disparaissent.

---

## Prérequis

Avant de passer au déploiement continu :
- ✅ Suite de tests automatisés complète et fiable
- ✅ Monitoring et alerting en place
- ✅ Rollback automatisé fonctionnel
- ✅ Feature flags pour désactiver du code sans redéployer
- ✅ Déploiement progressif (canary/blue-green)

---

## Exemple pipeline CD complet

```yaml
deploy:
  needs: [test, security-scan]
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  steps:
    - name: Deploy canary (5%)
      run: |
        kubectl set image deployment/myapp-canary           app=myapp:${{ github.sha }}

    - name: Monitor canary for 10min
      run: ./scripts/wait-and-check-metrics.sh 600

    - name: Full rollout
      run: |
        kubectl set image deployment/myapp           app=myapp:${{ github.sha }}
        kubectl rollout status deployment/myapp
```

---

> [!warning]
> Le déploiement continu n'est pas adapté à tous les contextes (applications médicales, financières avec compliance stricte). Évaluer les risques avant d'éliminer l'approbation manuelle.
