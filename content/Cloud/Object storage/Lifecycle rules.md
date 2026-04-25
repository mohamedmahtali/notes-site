---
title: Lifecycle rules
tags:
  - intermediate
---
# Lifecycle rules

---

## Définition

Les lifecycle rules automatisent la gestion du cycle de vie des objets : transition vers des classes de stockage moins chères après X jours, suppression automatique des objets ou versions anciennes.

---

## AWS S3 Lifecycle

```bash
aws s3api put-bucket-lifecycle-configuration   --bucket my-bucket   --lifecycle-configuration '{
    "Rules": [
      {
        "ID": "archive-old-logs",
        "Status": "Enabled",
        "Filter": {"Prefix": "logs/"},
        "Transitions": [
          {"Days": 30, "StorageClass": "STANDARD_IA"},
          {"Days": 90, "StorageClass": "GLACIER"}
        ],
        "Expiration": {"Days": 365}
      },
      {
        "ID": "delete-old-versions",
        "Status": "Enabled",
        "NoncurrentVersionExpiration": {"NoncurrentDays": 30}
      }
    ]
  }'
```

---

## Transitions de classes

```
Day 0   : Objet créé → S3 Standard ($0.023/GB)
Day 30  : Transition → S3 Standard-IA ($0.0125/GB)
Day 90  : Transition → S3 Glacier ($0.004/GB)
Day 365 : Expiration → Suppression automatique
```

---

> [!tip]
> Les lifecycle rules sont essentielles pour maîtriser les coûts S3. Les logs et artefacts de build s'accumulent rapidement — automatiser leur archivage et suppression dès le départ.
