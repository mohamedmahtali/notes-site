---
title: etcd
tags:
  - advanced
---
# etcd

---

## Définition

etcd est la base de données clé-valeur distribuée qui stocke tout l'état du [[Cluster]] [[Kubernetes]] : [[Pods]], [[Services]], [[ConfigMaps]], [[Secrets]], etc. C'est le seul composant avec état dans le [[Control plane]] — si etcd est perdu, le cluster est perdu.

---

## Pourquoi c'est important

> [!warning] Sauvegarder etcd = sauvegarder le cluster
> Sans backup etcd, un incident sur le control plane peut signifier la perte de tout l'état du cluster. En production, etcd tourne en cluster de 3 ou 5 nœuds (consensus Raft) avec des snapshots automatiques.

---

## Caractéristiques clés

- **Consensus Raft** : tolérance à la panne de (n-1)/2 membres (3 membres → 1 panne tolérée)
- **Watch API** : notifie les clients des changements en temps réel
- **MVCC** : Multi-Version Concurrency Control
- **Strongly consistent** : toutes les lectures reflètent le dernier write

---

## Backup et restauration

```bash
# Snapshot etcd (depuis un node control plane)
ETCDCTL_API=3 etcdctl snapshot save backup.db   --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key

# Vérifier le snapshot
etcdctl snapshot status backup.db --write-out=table

# Restaurer
etcdctl snapshot restore backup.db   --data-dir=/var/lib/etcd-restore
```

---

> [!tip]
> Automatiser les snapshots etcd via un CronJob. Stocker les backups hors du cluster (S3, GCS). Tester la restauration régulièrement.
