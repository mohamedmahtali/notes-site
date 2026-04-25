---
title: Operators
tags:
  - advanced
---
# Operators

---

## Définition

Un Operator [[Kubernetes]] est une application qui étend l'API Kubernetes pour gérer des applications complexes. Il combine des Custom Resource Definitions (CRDs) avec un controller qui automatise les opérations (deployment, backup, failover, scaling) spécifiques à une application.

---

## Pourquoi les Operators

> [!tip] Automatiser l'expertise humaine
> Gérer une base de données en production requiert une expertise : backup, réplication, failover, scaling. Un Operator encode cette expertise dans du code et l'exécute automatiquement. CloudNative PG opère PostgreSQL, Strimzi opère Kafka.

---

## Operators populaires

| Operator | Application |
|---|---|
| CloudNative PG | PostgreSQL |
| Strimzi | Apache Kafka |
| [[Prometheus]] Operator | Prometheus + [[Alertmanager]] |
| cert-manager | Gestion de certificats [[TLS]] |
| Argo CD | [[GitOps]] CD |
| [[Vault]] Operator | HashiCorp Vault |

---

## Exemple avec CloudNative PG

```yaml
# Au lieu de gérer StatefulSet + PVC + configmaps manuellement :
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: postgres-cluster
spec:
  instances: 3
  storage:
    size: 100Gi
    storageClass: fast-ssd
  backup:
    barmanObjectStore:
      destinationPath: s3://my-bucket/postgres/
      s3Credentials:
        accessKeyId:
          name: aws-creds
          key: ACCESS_KEY_ID
```

---

> [!note]
> Voir [[CRD]] pour les [[Types]] custom, [[Custom controllers]] pour implémenter un Operator, [[Reconciliation loop]] pour le pattern de base.
