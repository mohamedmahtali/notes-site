---
title: Object storage
tags:
  - beginner
---
# Object storage

---

## Définition

L'object storage est un paradigme de stockage qui stocke les données comme des objets (fichier + métadonnées + identifiant unique). Contrairement au block storage, il est accessible via HTTP REST. Exemples : [[AWS]] S3, GCP [[Cloud Storage]], [[Azure]] [[Blob Storage]].

---

## Caractéristiques

| Aspect | Description |
|---|---|
| Scalabilité | Pratiquement illimitée |
| Durabilité | 99.999999999% (11 neuf) sur S3 |
| Accès | HTTP REST ([[get]], PUT, DELETE) |
| Prix | ~$0.023/GB/mois (S3 Standard) |
| Latence | ms à secondes (pas pour BDD) |

---

## Usages courants

- Assets statiques (images, CSS, JS)
- Backups et archives
- Artefacts de build / images [[Docker]] [[Layers]]
- Datasets ML
- Logs centralisés
- State [[Terraform]]

---

```bash
# AWS S3
aws s3 cp ./image.png s3://my-bucket/images/
aws s3 sync ./build/ s3://my-bucket/static/

# GCP Cloud Storage
gsutil cp ./image.png gs://my-bucket/images/
gsutil rsync -r ./build/ gs://my-bucket/static/
```
