---
title: Volumes
tags:
  - intermediate
---
# Volumes

## Définition

Les volumes Kubernetes permettent aux containers de persister des données et de les partager entre containers d'un même pod. Contrairement aux layers Docker, les volumes survivent aux redémarrages du container (mais pas forcément à la suppression du pod).

## Types de volumes

| Type | Durée de vie | Usage |
|---|---|---|
| `emptyDir` | Durée du pod | Partage inter-containers, cache temporaire |
| `hostPath` | Permanente (Node) | Accès au filesystem du node |
| `configMap` / `secret` | Durée du pod | Injecter de la configuration |
| `persistentVolumeClaim` | Indépendante du pod | Stockage persistant production |
| `emptyDir (Memory)` | Durée du pod | tmpfs en mémoire (très rapide) |

## Volumes simples dans un Pod

```yaml
spec:
  containers:
    - name: app
      volumeMounts:
        - name: data
          mountPath: /var/data
        - name: config
          mountPath: /etc/config
          readOnly: true
        - name: cache
          mountPath: /tmp/cache
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: my-pvc
    - name: config
      configMap:
        name: app-config
    - name: cache
      emptyDir:
        medium: Memory      # tmpfs
        sizeLimit: 256Mi
```

## Flux PV → PVC → Pod (stockage persistant)

Le stockage persistant en production suit ce flux en 3 objets :

```
StorageClass (définit le type de stockage)
  ↓ provisionne dynamiquement
PersistentVolume / PV (ressource de stockage réelle)
  ↓ claim
PersistentVolumeClaim / PVC (demande de stockage par le pod)
  ↓ monte dans
Pod
```

### StorageClass

```yaml
# StorageClass AWS EBS (souvent déjà présente sur EKS)
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3-encrypted
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  encrypted: "true"
reclaimPolicy: Delete       # Delete ou Retain
volumeBindingMode: WaitForFirstConsumer
```

### PersistentVolumeClaim

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-data
  namespace: production
spec:
  accessModes:
    - ReadWriteOnce         # RWO = un seul node, RWX = multi-nodes
  storageClassName: gp3-encrypted
  resources:
    requests:
      storage: 20Gi
```

### Utiliser le PVC dans un Pod

```yaml
spec:
  containers:
    - name: postgres
      image: postgres:16
      volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: postgres-data
```

## Access Modes

| Mode | Abrév. | Description |
|------|--------|-------------|
| ReadWriteOnce | RWO | Lecture/écriture par un seul node |
| ReadOnlyMany | ROX | Lecture seule par plusieurs nodes |
| ReadWriteMany | RWX | Lecture/écriture par plusieurs nodes |

EBS (AWS) ne supporte que RWO. EFS (AWS) supporte RWX. En pratique, la plupart des bases de données n'ont besoin que de RWO.

## Reclaim Policies

| Policy | Comportement à la suppression du PVC | Usage |
|--------|--------------------------------------|-------|
| `Delete` | Supprime le PV et les données | Dev, stateless |
| `Retain` | Garde le PV (données sauvegardées) | Production, BDD |
| `Recycle` | Supprime les fichiers, réutilise le PV | Déprécié |

> [!warning] hostPath en production
> `hostPath` monte un chemin du node hôte dans le container. Dangereux en production : le pod est lié à un node spécifique, et un container compromis peut lire le filesystem de l'hôte. Réservé aux DaemonSets légitimes (node-exporter, log collectors).

## Explorer

- **[[Persistent volumes]]** — PV, PVC, cycle de vie complet
- **[[emptyDir]]** — partage inter-containers, tmpfs
- **[[ConfigMaps]]** — injection de configuration via volume
- **[[Secrets]]** — injection de secrets sensibles via volume
- **[[StatefulSets]]** — workloads avec stockage persistant dédié par pod
