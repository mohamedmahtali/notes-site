---
title: Versioning
tags:
  - intermediate
---
# Versioning

---

## Définition

Le versioning d'un bucket conserve toutes les versions d'un objet lors des mises à jour ou suppressions. Permet de restaurer une version précédente en cas d'erreur ou de suppression accidentelle.

---

## AWS S3 Versioning

```bash
# Activer le versioning
aws s3api put-bucket-versioning   --bucket my-bucket   --versioning-configuration Status=Enabled

# Lister les versions d'un objet
aws s3api list-object-versions   --bucket my-bucket   --prefix my-file.txt

# Restaurer une version précédente
aws s3api copy-object   --bucket my-bucket   --copy-source my-bucket/my-file.txt?versionId=abc123   --key my-file.txt

# Supprimer une version spécifique
aws s3api delete-object   --bucket my-bucket   --key my-file.txt   --version-id abc123
```

---

## Gérer les coûts — lifecycle sur les anciennes versions

```bash
# Supprimer automatiquement les vieilles versions après 30 jours
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-bucket \
  --lifecycle-configuration '{
    "Rules": [{
      "ID": "expire-old-versions",
      "Status": "Enabled",
      "Filter": {},
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 30
      },
      "ExpiredObjectDeleteMarker": true
    }]
  }'
```

## MFA Delete — protection contre la suppression

```bash
# Activer MFA Delete (nécessite un device MFA et les credentials root)
aws s3api put-bucket-versioning \
  --bucket my-bucket \
  --versioning-configuration '{
    "Status": "Enabled",
    "MFADelete": "Enabled"
  }' \
  --mfa "arn:aws:iam::ACCOUNT:mfa/root-account-mfa-device 123456"

# Avec MFA Delete : impossible de supprimer une version sans le token MFA
# Protection contre les ransomwares et les erreurs humaines
```

## Restauration rapide

```bash
# Voir toutes les versions avec leurs dates
aws s3api list-object-versions \
  --bucket my-bucket \
  --prefix config.yaml \
  --query 'Versions[*].{ID:VersionId,Date:LastModified}' \
  --output table

# Restaurer la version d'avant-hier
aws s3api copy-object \
  --bucket my-bucket \
  --copy-source "my-bucket/config.yaml?versionId=<VERSION_ID>" \
  --key config.yaml
```

> [!warning]
> Le versioning augmente les coûts de stockage — chaque version occupe de l'espace. Combiner avec une lifecycle rule pour supprimer automatiquement les vieilles versions après 30 jours.
