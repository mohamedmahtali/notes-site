---
title: StatefulSets
tags:
  - intermediate
---
# StatefulSets

---

## Définition

Un StatefulSet gère des applications stateful (bases de données, caches, systèmes distribués) où chaque pod a une identité stable et un stockage persistant dédié. Contrairement aux [[Deployments]], les [[Pods]] ne sont pas interchangeables.

---

## Différences avec Deployments

| Aspect | Deployment | StatefulSet |
|---|---|---|
| Nom des pods | Aléatoire (myapp-abc12) | Ordonné (myapp-0, myapp-1) |
| Stockage | Partagé | Dédié par pod |
| Démarrage | Parallèle | Ordonné (0, puis 1, puis 2) |
| Suppression | Aléatoire | Inverse (2, puis 1, puis 0) |
| [[DNS]] | Non stable | Stable (myapp-0.myapp.ns.svc) |

---

## Manifeste

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres       # headless service requis
  replicas: 3
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:       # PVC créé automatiquement par pod
  - metadata:
      name: data
    spec:
      accessModes: [ReadWriteOnce]
      resources:
        requests:
          storage: 10Gi
```

---

> [!note]
> Pour les BDD en production sur K8s, évaluer des solutions comme CloudNative PG (PostgreSQL), Strimzi (Kafka), ou utiliser des [[Services]] managés (RDS, [[Cloud]] SQL) plutôt que de gérer le StatefulSet manuellement.
