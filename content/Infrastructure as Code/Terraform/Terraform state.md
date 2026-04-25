---
title: Terraform state
tags:
  - intermediate
---
# Terraform state

---

## Définition

Le state [[Terraform]] est un fichier JSON (`terraform.tfstate`) qui mappe les ressources définies dans le code aux ressources réelles dans le [[Cloud]]. C'est la source de vérité pour Terraform — il sait ce qu'il gère et quel est l'état actuel.

---

## Pourquoi c'est important

> [!warning] Le state est critique
> Sans state, Terraform ne peut pas savoir quelles ressources existent déjà. Perte du state = Terraform pense que tout doit être recréé. Toujours stocker le state à distance (S3, GCS, Terraform Cloud) en production.

---

## Commandes state

```bash
# Lister les ressources dans le state
terraform state list

# Voir les détails d'une ressource dans le state
terraform state show aws_instance.web

# Renommer une ressource dans le state (sans la détruire)
terraform state mv aws_instance.web aws_instance.webserver

# Supprimer une ressource du state (sans la détruire)
terraform state rm aws_instance.web

# Importer une ressource existante dans le state
terraform import aws_instance.existing i-1234567890abcdef0

# Forcer la mise à jour du state
terraform refresh
```

---

> [!note]
> Voir [[Remote state]] pour stocker le state dans S3/GCS, [[State locking]] pour éviter les conflits concurrents, [[Drift]] pour détecter les changements manuels.
