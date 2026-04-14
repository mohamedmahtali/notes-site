---
title: Stable identity
tags:
  - intermediate
---
# Stable identity

## Parent
- [[StatefulSets]]

---

## Définition

L'identité stable d'un StatefulSet signifie que chaque pod conserve le même nom et la même adresse DNS, même après un redémarrage. `postgres-0` reste toujours `postgres-0` — contrairement aux pods de Deployment qui ont un nom aléatoire.

---

## Nommage et DNS

```
StatefulSet: postgres, replicas: 3
Pods: postgres-0, postgres-1, postgres-2

Service headless: postgres (clusterIP: None)

DNS par pod:
  postgres-0.postgres.default.svc.cluster.local
  postgres-1.postgres.default.svc.cluster.local
  postgres-2.postgres.default.svc.cluster.local
```

---

## Service headless

```yaml
# Service headless requis pour le DNS stable
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  clusterIP: None       # headless = pas de ClusterIP virtuelle
  selector:
    app: postgres
  ports:
  - port: 5432
```

---

## Utilisation du DNS stable

```yaml
# Configuration PostgreSQL replica pointant vers le primary
env:
- name: POSTGRES_PRIMARY_HOST
  value: postgres-0.postgres.default.svc.cluster.local
```

---

> [!tip]
> Le DNS stable permet aux membres d'un cluster distribué (Kafka, Elasticsearch, PostgreSQL HA) de se localiser mutuellement de façon fiable. `postgres-0` est toujours le primary, `postgres-1` et `postgres-2` sont les replicas.
