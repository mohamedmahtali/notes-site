---
title: Storage classes
tags:
  - intermediate
---
# Storage classes

---

## Définition

Une StorageClass décrit les "classes" de stockage disponibles dans un [[Cluster]] (SSD, HDD, NFS, réplication...). Quand un PVC référence une StorageClass, le provisioner associé crée automatiquement le PV — c'est le provisionnement dynamique.

---

## StorageClasses AWS EKS

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  iops: "3000"
  throughput: "125"
  encrypted: "true"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer  # attend le pod pour optimiser la zone
allowVolumeExpansion: true
```

---

## StorageClass par défaut

```bash
# Voir les storage classes
kubectl get storageclass
kubectl get sc

# Marquer comme défaut
kubectl patch storageclass gp2   -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

---

## Utilisation dans un PVC

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes: [ReadWriteOnce]
  storageClassName: fast-ssd   # ou omettre pour utiliser le défaut
  resources:
    requests:
      storage: 20Gi
```
