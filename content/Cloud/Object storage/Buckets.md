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
