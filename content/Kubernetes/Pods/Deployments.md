---
title: Deployments
tags:
  - beginner
---
# Deployments

---

## Définition

Un Deployment est l'objet [[Kubernetes]] pour déployer des applications stateless. Il gère les [[ReplicaSets]], garantit le nombre de réplicas désiré, et orchestre les mises à jour progressives avec possibilité de [[Rollback]].

---

## Manifeste

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1           # pods supplémentaires max pendant update
      maxUnavailable: 0     # 0 downtime
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:1.0
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "500m"
```

---

## Commandes essentielles

```bash
# Créer / appliquer
kubectl apply -f deployment.yaml

# Voir les déploiements
kubectl get deployments
kubectl get deploy -o wide

# Mettre à jour l'image
kubectl set image deployment/myapp app=myapp:2.0

# Suivre le rolling update
kubectl rollout status deployment/myapp

# Rollback
kubectl rollout undo deployment/myapp

# Scaler
kubectl scale deployment myapp --replicas=5
```

---

> [!tip]
> Toujours versionner les images (`myapp:1.2.3`) plutôt que `latest`. Avec `latest`, `kubectl set image` ne déclenchera pas un nouveau rollout si l'image locale est déjà `latest`.
