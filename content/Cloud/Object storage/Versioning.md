---
title: Versioning
tags:
  - intermediate
---
# Versioning

## Parent
- [[Object storage]]

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

> [!warning]
> Le versioning augmente les coûts de stockage — chaque version occupe de l'espace. Combiner avec des [[Lifecycle rules]] pour supprimer automatiquement les vieilles versions après X jours.
