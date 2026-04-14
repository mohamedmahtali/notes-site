---
title: Blob Storage
tags:
  - beginner
---
# Blob Storage

## Parent
- [[Azure]]

---

## Définition

Azure Blob Storage est l'équivalent Azure de S3. Il stocke des objets non-structurés dans des conteneurs (l'équivalent des buckets S3). Les blobs sont organisés dans des Storage Accounts.

---

## Commandes essentielles

```bash
# Créer un storage account
az storage account create   --name mystorageaccount2024   --resource-group myapp-rg   --location westeurope   --sku Standard_LRS   --kind StorageV2

# Créer un conteneur
az storage container create   --account-name mystorageaccount2024   --name my-container

# Upload
az storage blob upload   --account-name mystorageaccount2024   --container-name my-container   --file ./data.csv   --name data/data.csv

# Lister
az storage blob list   --account-name mystorageaccount2024   --container-name my-container   --output table

# Download
az storage blob download   --account-name mystorageaccount2024   --container-name my-container   --name data/data.csv   --file ./data-downloaded.csv
```
