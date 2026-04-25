---
title: Cloud Storage
tags:
  - beginner
---
# Cloud Storage

---

## Définition

[[Google [[Cloud]]]] Storage est l'équivalent GCP de S3. Il stocke des objets dans des [[Buckets]] avec une durabilité de 99.999999999%. Accessible via gsutil CLI, le SDK Cloud Storage, ou l'API REST.

---

## Commandes essentielles

```bash
# Créer un bucket
gsutil mb -l europe-west1 gs://my-unique-bucket

# Upload
gsutil cp ./file.txt gs://my-bucket/
gsutil -m cp -r ./build/ gs://my-bucket/static/   # parallèle

# Sync
gsutil rsync -r -d ./dist/ gs://my-bucket/static/

# Lister
gsutil ls gs://my-bucket/
gsutil du -sh gs://my-bucket/    # taille totale

# Supprimer
gsutil rm gs://my-bucket/file.txt
gsutil -m rm -r gs://my-bucket/folder/
```

---

## Classes de stockage

| Classe | Accès minimum | Prix |
|---|---|---|
| Standard | Aucun | $0.020/GB |
| Nearline | 30 jours | $0.010/GB |
| Coldline | 90 jours | $0.004/GB |
| Archive | 365 jours | $0.0012/GB |
