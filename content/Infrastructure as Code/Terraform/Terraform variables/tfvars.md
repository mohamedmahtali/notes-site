---
title: tfvars
tags:
  - beginner
---
# tfvars

---

## Définition

Les fichiers `.tfvars` contiennent les valeurs des [[Variables]] [[Terraform]] pour un environnement donné. Ils permettent de séparer la définition des variables (code) de leurs valeurs (configuration).

---

## Format

```hcl
# production.tfvars
environment       = "production"
instance_type     = "t3.large"
instance_count    = 3
enable_https      = true
availability_zones = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]

tags = {
  Project     = "myapp"
  Environment = "production"
  Owner       = "platform-team"
  CostCenter  = "engineering"
}
```

---

## Utilisation

```bash
# Spécifier le fichier
terraform apply -var-file=production.tfvars

# Plusieurs fichiers (ordre important — le dernier gagne)
terraform apply   -var-file=common.tfvars   -var-file=production.tfvars

# Auto-chargé (terraform.tfvars ou *.auto.tfvars)
ls *.tfvars
# terraform.tfvars  → chargé automatiquement
# production.auto.tfvars → chargé automatiquement
```

---

> [!warning]
> Ne jamais committer les fichiers `.tfvars` contenant des [[Secrets]] (mots de passe, access keys). Les ajouter au `.gitignore`. Utiliser des variables d'environnement `TF_VAR_*` ou un [[Vault]] pour les secrets.
