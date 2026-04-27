---
title: Object storage
tags:
  - beginner
---
# Object storage

## Définition

L'object storage stocke les données comme des objets (fichier + métadonnées + identifiant unique). Contrairement au block storage, il est accessible via HTTP REST. Exemples : [[AWS]] S3, GCP Cloud Storage, [[Azure]] Blob Storage.

## Caractéristiques

| Aspect | Description |
|---|---|
| Scalabilité | Pratiquement illimitée (exaoctets) |
| Durabilité | 99.999999999% (11 neuf) sur S3 Standard |
| Accès | HTTP REST (GET, PUT, DELETE) |
| Prix | ~$0.023/GB/mois (S3 Standard) |
| Latence | ms à secondes — pas adapté aux BDD |

## Usages courants

- Assets statiques (images, CSS, JS)
- Backups et archives
- Artefacts de build, images Docker layers
- Datasets ML
- Logs centralisés
- State [[Terraform]]
- Hébergement de site statique

## AWS S3 — opérations essentielles

```bash
# Uploader un fichier
aws s3 cp ./image.png s3://my-bucket/images/

# Synchroniser un dossier local → bucket (build statique)
aws s3 sync ./dist/ s3://my-bucket/ --delete

# Lister le contenu
aws s3 ls s3://my-bucket/images/ --human-readable

# Télécharger
aws s3 cp s3://my-bucket/backup.tar.gz ./

# Supprimer
aws s3 rm s3://my-bucket/old-file.png
aws s3 rm s3://my-bucket/logs/ --recursive
```

## Versioning

```bash
# Activer le versioning
aws s3api put-bucket-versioning \
  --bucket my-bucket \
  --versioning-configuration Status=Enabled

# Lister les versions d'un objet
aws s3api list-object-versions \
  --bucket my-bucket --prefix myfile.txt

# Restaurer une version précédente
aws s3api copy-object \
  --bucket my-bucket \
  --copy-source my-bucket/myfile.txt?versionId=abc123 \
  --key myfile.txt
```

## Lifecycle rules — gestion automatique du coût

```json
{
  "Rules": [{
    "ID": "archive-and-delete",
    "Status": "Enabled",
    "Filter": {"Prefix": "logs/"},
    "Transitions": [
      {"Days": 30,  "StorageClass": "STANDARD_IA"},
      {"Days": 90,  "StorageClass": "GLACIER"}
    ],
    "Expiration": {"Days": 365}
  }]
}
```

```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-bucket \
  --lifecycle-configuration file://lifecycle.json
```

## Classes de stockage S3

| Classe | Accès | Prix | Usage |
|--------|-------|------|-------|
| Standard | Fréquent | ~$0.023/GB | Assets actifs |
| Standard-IA | Rare | ~$0.0125/GB | Backups récents |
| Glacier | Archivage | ~$0.004/GB | Archives long terme |
| Glacier Deep Archive | Rarement | ~$0.00099/GB | Conformité/audit |

## Pre-signed URLs — accès temporaire sans credentials

```bash
# Générer un lien de téléchargement valable 1h
aws s3 presign s3://my-bucket/private-report.pdf --expires-in 3600

# Via SDK Python
import boto3
s3 = boto3.client('s3')
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': 'my-bucket', 'Key': 'private-report.pdf'},
    ExpiresIn=3600
)
```

Utile pour partager un fichier privé temporairement sans rendre le bucket public.

## Hébergement site statique

```bash
# Activer l'hébergement statique
aws s3 website s3://my-bucket \
  --index-document index.html \
  --error-document 404.html

# URL : http://my-bucket.s3-website-eu-west-1.amazonaws.com
# En production : combiner avec CloudFront (CDN + HTTPS)
```

## Explorer

- **[[AWS]]** — S3 dans l'écosystème AWS
- **[[Cloud computing]]** — IaaS/PaaS/SaaS, contexte cloud général
- **[[Terraform state]]** — backend S3 pour stocker le state Terraform
