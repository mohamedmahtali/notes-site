---
title: Rolling updates
tags:
  - intermediate
---
# Rolling updates

---

## Définition

Un rolling update remplace progressivement les [[Pods]] de l'ancienne version par des pods de la nouvelle version, sans downtime. Le trafic continue d'être servi par les pods disponibles pendant la transition.

---

## Configuration

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # nombre max de pods en plus pendant l'update
      maxUnavailable: 0  # 0 = zero-downtime (toujours autant de pods dispo)
```

---

## Déroulement

```
Initial: 3 pods v1.0 en Running

1. Créer 1 pod v2.0 (maxSurge=1 → 4 pods total)
2. Attendre que v2.0 soit Ready
3. Supprimer 1 pod v1.0
4. Répéter jusqu'à remplacement complet

Final: 3 pods v2.0 en Running
```

---

## Commandes

```bash
# Déclencher un rolling update
kubectl set image deployment/myapp app=myapp:2.0
# ou
kubectl apply -f deployment-v2.yaml

# Suivre l'avancement
kubectl rollout status deployment/myapp

# Voir l'historique
kubectl rollout history deployment/myapp
kubectl rollout history deployment/myapp --revision=3

# Pause / resume (déploiement canary manuel)
kubectl rollout pause deployment/myapp
kubectl rollout resume deployment/myapp
```

---

> [!tip]
> Configurer `minReadySeconds` dans le Deployment pour que le [[Scheduler]] attende que le pod soit stable avant de continuer le rolling update. Évite de passer à la suite si le pod crashe immédiatement.
