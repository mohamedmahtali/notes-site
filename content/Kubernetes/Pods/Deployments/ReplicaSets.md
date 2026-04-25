---
title: ReplicaSets
tags:
  - intermediate
---
# ReplicaSets

---

## Définition

Un ReplicaSet garantit qu'un nombre spécifié de réplicas d'un pod tourne en permanence. Les [[Deployments]] créent et gèrent les ReplicaSets automatiquement — on n'utilise généralement pas les ReplicaSets directement.

---

## Relation Deployment → ReplicaSet → Pod

```
Deployment (myapp)
    ├── ReplicaSet (myapp-7d4b9c8f5)  ← version actuelle
    │       ├── Pod (myapp-7d4b9c8f5-abc12)
    │       ├── Pod (myapp-7d4b9c8f5-def34)
    │       └── Pod (myapp-7d4b9c8f5-ghi56)
    └── ReplicaSet (myapp-6c3a8b7e4)  ← ancienne version (0 réplicas)
```

---

## Commandes

```bash
# Voir les ReplicaSets
kubectl get replicasets
kubectl get rs

# Voir l'historique des RS d'un Deployment
kubectl get rs -l app=myapp

# Describe un RS
kubectl describe rs myapp-7d4b9c8f5

# Le RS créé manuellement (rare)
kubectl apply -f - <<'EOF'
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myapp-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:1.0
EOF
```

---

> [!note]
> [[Kubernetes]] conserve les anciens ReplicaSets (avec 0 réplicas) pour permettre le [[Rollback]]. Le nombre de revisions conservées est contrôlé par `.spec.revisionHistoryLimit` dans le Deployment.
