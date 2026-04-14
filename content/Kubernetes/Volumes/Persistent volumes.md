---
title: Persistent volumes
tags:
  - intermediate
---
# Persistent volumes

## Parent
- [[Volumes]]

## Enfants
- [[Storage classes]]
- [[Reclaim policies]]

---

## Définition

Un PersistentVolume (PV) est un morceau de stockage dans le cluster provisionné par un administrateur ou dynamiquement via une StorageClass. C'est une ressource cluster-wide, indépendante du cycle de vie des pods.

---

## Modes d'accès

| Mode | Description |
|---|---|
| `ReadWriteOnce` | Lecture/écriture par un seul node |
| `ReadOnlyMany` | Lecture seule par plusieurs nodes |
| `ReadWriteMany` | Lecture/écriture par plusieurs nodes (NFS, EFS) |
| `ReadWriteOncePod` | R/W par un seul pod (K8s 1.22+) |

---

## PV statique (admin-provisionné)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-data-1
spec:
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: fast-ssd
  awsElasticBlockStore:       # ou nfs, csi, hostPath...
    volumeID: vol-0a1b2c3d4e5f
    fsType: ext4
```

---

```bash
kubectl get pv
kubectl describe pv pv-data-1
# STATUS: Available → PVC peut le lier
# STATUS: Bound     → lié à un PVC
# STATUS: Released  → PVC supprimé, PV à recycler/supprimer
```

---

> [!tip]
> En production cloud, utiliser le provisionnement dynamique via [[Storage classes]] plutôt que des PVs statiques. Le CSI driver crée automatiquement les disques cloud à la demande.
