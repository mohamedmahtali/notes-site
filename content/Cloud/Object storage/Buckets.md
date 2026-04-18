---
title: Buckets
tags:
  - beginner
---
# Buckets

## Parent
- [[Object storage]]

---

## Définition

Un bucket est un conteneur de premier niveau pour les objets dans un service d'object storage. Les noms de buckets sont uniques globalement (S3) ou par projet (GCP). Chaque objet dans un bucket a une clé unique.

---

## Créer et configurer un bucket

```bash
# AWS S3
aws s3 mb s3://my-unique-bucket-2024 --region eu-west-1

# Bloquer l'accès public (recommandé par défaut)
aws s3api put-public-access-block   --bucket my-unique-bucket-2024   --public-access-block-configuration     BlockPublicAcls=true,IgnorePublicAcls=true,    BlockPublicPolicy=true,RestrictPublicBuckets=true

# Activer le chiffrement
aws s3api put-bucket-encryption   --bucket my-unique-bucket-2024   --server-side-encryption-configuration     '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"aws:kms"}}]}'

# GCP
gsutil mb -l EU gs://my-bucket-2024/
```

---

> [!warning]
> Par défaut depuis 2023, S3 bloque l'accès public sur les nouveaux buckets. Ne jamais désactiver ce blocage sauf pour les buckets de website hosting intentionnellement publics.

## Lifecycle policy — gestion automatique des coûts

```bash
# Appliquer une policy de lifecycle sur S3
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-unique-bucket-2024 \
  --lifecycle-configuration '{
    "Rules": [{
      "ID": "archive-and-delete",
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Transitions": [
        { "Days": 30, "StorageClass": "STANDARD_IA" },
        { "Days": 90, "StorageClass": "GLACIER" }
      ],
      "Expiration": { "Days": 365 }
    }]
  }'
```

## Presigned URLs — accès temporaire sans credentials

```bash
# Générer une URL signée valable 1h (lecture)
aws s3 presign s3://my-bucket/reports/report.pdf \
  --expires-in 3600

# → https://my-bucket.s3.amazonaws.com/reports/report.pdf?X-Amz-Signature=...
# Partager cette URL — elle expire automatiquement
```

## Réplication cross-région

```bash
# Activer la réplication vers une autre région (disaster recovery)
aws s3api put-bucket-replication \
  --bucket my-unique-bucket-2024 \
  --replication-configuration '{
    "Role": "arn:aws:iam::ACCOUNT:role/s3-replication-role",
    "Rules": [{
      "Status": "Enabled",
      "Destination": {
        "Bucket": "arn:aws:s3:::my-bucket-replica-eu-central-1",
        "StorageClass": "STANDARD_IA"
      }
    }]
  }'
```
