---
title: Persistent volume claims
tags:
  - intermediate
---
# Persistent volume claims

---

## Définition

Un PersistentVolumeClaim (PVC) est une demande de stockage par un pod. Il spécifie la taille et le mode d'accès requis. [[Kubernetes]] lie le PVC à un PV disponible (statique ou dynamiquement provisionné).

---

## Manifeste

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-data
  namespace: production
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast-ssd    # StorageClass à utiliser
  resources:
    requests:
      storage: 50Gi
```

---

## Utiliser dans un pod

```yaml
spec:
  containers:
  - name: postgres
    image: postgres:15
    volumeMounts:
    - name: pgdata
      mountPath: /var/lib/postgresql/data
  volumes:
  - name: pgdata
    persistentVolumeClaim:
      claimName: postgres-data    # lier le PVC
```

---

## Cycle de vie

```bash
# Voir les PVCs et leur statut
kubectl get pvc
# NAME           STATUS   VOLUME        CAPACITY   ACCESS MODES   STORAGECLASS
# postgres-data  Bound    pvc-abc123    50Gi       RWO            fast-ssd

# Pending = en attente d'un PV disponible
# Bound    = lié à un PV
# Lost     = PV sous-jacent disparu

# Agrandir un PVC (si StorageClass allowVolumeExpansion: true)
kubectl patch pvc postgres-data -p '{"spec":{"resources":{"requests":{"storage":"100Gi"}}}}'
```
