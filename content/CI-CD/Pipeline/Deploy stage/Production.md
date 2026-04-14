---
title: Production
tags:
  - intermediate
---
# Production

## Parent
- [[Deploy stage]]

---

## Définition

L'environnement de production est l'environnement live où les utilisateurs finaux accèdent à l'application. Les déploiements en production nécessitent généralement une approbation manuelle ou des critères stricts (tests passés, staging validé).

---

## Pourquoi c'est important

> [!warning] Ici, les erreurs coûtent cher
> Une panne en production impacte directement les utilisateurs et la réputation. Toujours avoir un plan de rollback, monitorer immédiatement après déploiement, et utiliser des stratégies de déploiement progressif (blue/green, canary).

---

## Protection GitHub Actions

```yaml
# Dans les settings GitHub : Environments → production
# Configurer : Required reviewers, wait timer, branch restrictions

deploy-production:
  needs: deploy-staging
  environment:
    name: production
    url: https://myapp.com
  steps:
    - name: Deploy canary (10%)
      run: |
        kubectl set image deployment/myapp-canary           app=myregistry/myapp:${{ github.sha }}

    - name: Verify canary metrics
      run: ./scripts/check-error-rate.sh --threshold 1

    - name: Full rollout
      run: |
        kubectl set image deployment/myapp           app=myregistry/myapp:${{ github.sha }}
```

---

> [!tip]
> Toujours monitorer les métriques (error rate, latency, saturation) pendant les 15 premières minutes post-déploiement. Configurer une alerte automatique qui déclenche un [[Rollback]] si les métriques dégradent.
