---
title: Progressive rollout
tags:
  - advanced
---
# Progressive rollout

## Parent
- [[Continuous deployment]]

---

## Définition

Le progressive rollout déploie une nouvelle version graduellement : d'abord à 1% des utilisateurs, puis 10%, 25%, 100%. Si des métriques dégradent à n'importe quelle étape, le rollback est automatique.

---

## Stratégies

### Canary deployment
```bash
# Kubernetes — 10% du trafic vers la nouvelle version
kubectl scale deployment myapp --replicas=9       # version stable
kubectl scale deployment myapp-canary --replicas=1 # nouvelle version (10%)

# Avec un ingress controller
kubectl annotate ingress myapp   nginx.ingress.kubernetes.io/canary: "true"   nginx.ingress.kubernetes.io/canary-weight: "10"
```

### Blue/Green deployment
```bash
# Switch instantané entre deux environnements identiques
kubectl patch service myapp -p '{"spec":{"selector":{"version":"green"}}}'

# Rollback immédiat
kubectl patch service myapp -p '{"spec":{"selector":{"version":"blue"}}}'
```

---

## Automatisation avec Argo Rollouts

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
spec:
  strategy:
    canary:
      steps:
      - setWeight: 5
      - pause: {duration: 5m}
      - setWeight: 25
      - pause: {duration: 10m}
      - setWeight: 100
      analysis:
        templates:
        - templateName: error-rate
        args:
        - name: threshold
          value: "1"
```
