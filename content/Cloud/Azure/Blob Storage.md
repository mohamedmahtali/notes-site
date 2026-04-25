---
title: Blob Storage
tags:
  - beginner
---
# Blob Storage

---

## Définition

[[Azure]] Blob Storage est l'équivalent Azure de S3. Il stocke des objets non-structurés dans des conteneurs (l'équivalent des [[Buckets]] S3). Les blobs sont organisés dans des Storage Accounts.

---

## Commandes essentielles

```bash
# Créer un storage account
az storage account create \
  --name mystorageaccount2024 \
  --resource-group myapp-rg \
  --location westeurope \
  --sku Standard_LRS \
  --kind StorageV2

# Créer un conteneur
az storage container create \
  --account-name mystorageaccount2024 \
  --name my-container

# Upload / Download
az storage blob upload \
  --account-name mystorageaccount2024 \
  --container-name my-container \
  --file ./data.csv \
  --name data/data.csv

az storage blob download \
  --account-name mystorageaccount2024 \
  --container-name my-container \
  --name data/data.csv \
  --file ./data-downloaded.csv
```

## Tiers de stockage

| Tier | Usage | Coût stockage | Coût accès |
|------|-------|--------------|-----------|
| **Hot** | Données fréquemment accédées | Élevé | Faible |
| **Cool** | Données peu accédées (>30j) | Moyen | Moyen |
| **Cold** | Archives rarement accédées (>90j) | Faible | Élevé |
| **Archive** | Archives long terme (>180j) | Très faible | Très élevé + délai |

```bash
# Changer le tier d'un blob
az storage blob set-tier \
  --account-name mystorageaccount2024 \
  --container-name my-container \
  --name data/old-data.csv \
  --tier Cool
```

## Lifecycle policy (archivage automatique)

```json
{
  "rules": [{
    "name": "archive-old-data",
    "type": "Lifecycle",
    "definition": {
      "filters": { "blobTypes": ["blockBlob"], "prefixMatch": ["data/"] },
      "actions": {
        "baseBlob": {
          "tierToCool": { "daysAfterModificationGreaterThan": 30 },
          "tierToArchive": { "daysAfterModificationGreaterThan": 90 },
          "delete": { "daysAfterModificationGreaterThan": 365 }
        }
      }
    }
  }]
}
```

## SAS Token — accès temporaire

```bash
# Générer un SAS pour 1h (lecture seule)
az storage blob generate-sas \
  --account-name mystorageaccount2024 \
  --container-name my-container \
  --name data/report.pdf \
  --permissions r \
  --expiry $(date -u -d "+1 hour" +%Y-%m-%dT%H:%MZ) \
  --output tsv
```
