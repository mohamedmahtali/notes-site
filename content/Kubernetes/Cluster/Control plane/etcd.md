---
title: etcd
tags:
  - advanced
---
# etcd

## Définition

etcd est la base de données clé-valeur distribuée qui stocke tout l'état du [[Cluster]] [[Kubernetes]] : [[Pods]], [[Services]], [[ConfigMaps]], [[Secrets]], RBAC, etc. C'est le seul composant avec état dans le [[Control plane]] — si etcd est perdu sans backup, le cluster est perdu.

> [!warning] Sauvegarder etcd = sauvegarder le cluster
> Sans backup etcd, un incident sur le control plane peut signifier la perte de tout l'état du cluster. En production, etcd tourne en cluster de 3 ou 5 nœuds (consensus Raft) avec des snapshots automatiques.

## Rôle dans le Control Plane

```
kubectl apply → API Server → etcd (écrit l'état désiré)
                     ↑
Controller Manager ──┘ (lit l'état, reconcile)
Scheduler          ──┘ (lit les pods non schedulés)
kubelet            ──┘ (lit via API Server, rapporte état réel)
```

Tout passe par l'API Server — aucun composant n'écrit dans etcd directement.

## Consensus Raft — tolérance aux pannes

```
Cluster de 3 nœuds :
  etcd-1 (leader)  ←→  etcd-2  ←→  etcd-3
  
  → Quorum = 2 nœuds minimum
  → 1 panne tolérée (3 - 1 = 2 ≥ quorum)

Cluster de 5 nœuds :
  → Quorum = 3 nœuds minimum
  → 2 pannes tolérées

Règle : toujours un nombre impair (3 ou 5). Jamais 2 ou 4.
```

Un cluster 5 nœuds coûte plus cher mais tolère 2 pannes simultanées — utile pour les déploiements multi-AZ.

## Backup et restauration

```bash
# Snapshot etcd (depuis un node control plane)
ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-$(date +%Y%m%d).db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Vérifier l'intégrité du snapshot
etcdctl snapshot status /backup/etcd-20240115.db --write-out=table

# Restaurer (à faire quand kube-apiserver est stoppé)
etcdctl snapshot restore /backup/etcd-20240115.db \
  --data-dir=/var/lib/etcd-restore \
  --name etcd-1 \
  --initial-cluster etcd-1=https://10.0.0.1:2380 \
  --initial-advertise-peer-urls https://10.0.0.1:2380
```

## Automatiser les backups

```yaml
# CronJob K8s pour backup quotidien vers S3
apiVersion: batch/v1
kind: CronJob
metadata:
  name: etcd-backup
  namespace: kube-system
spec:
  schedule: "0 3 * * *"   # 3h du matin
  jobTemplate:
    spec:
      template:
        spec:
          hostNetwork: true
          containers:
            - name: etcd-backup
              image: bitnami/etcd:latest
              command:
                - /bin/sh
                - -c
                - |
                  etcdctl snapshot save /tmp/backup.db \
                    --endpoints=https://127.0.0.1:2379 \
                    --cacert=/etc/ssl/etcd/ca.crt \
                    --cert=/etc/ssl/etcd/server.crt \
                    --key=/etc/ssl/etcd/server.key
                  aws s3 cp /tmp/backup.db s3://my-etcd-backups/$(date +%Y%m%d).db
```

## Opérations courantes

```bash
# Vérifier l'état du cluster etcd
etcdctl member list --write-out=table

# Vérifier la santé
etcdctl endpoint health \
  --endpoints=https://10.0.0.1:2379,https://10.0.0.2:2379,https://10.0.0.3:2379

# Compacter (réduire la taille) — à faire périodiquement
etcdctl compact $(etcdctl endpoint status --write-out=json | jq '.[0].Status.header.revision')
etcdctl defrag
```

## Explorer

- **[[Control plane]]** — API Server, Scheduler, Controller Manager
- **[[Secrets]]** — stockés dans etcd, chiffrement au repos configurable
- **[[Cluster]]** — architecture globale du cluster Kubernetes
