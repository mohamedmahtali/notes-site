---
title: Terraform plan
tags:
  - beginner
---
# Terraform plan

## Parent
- [[Terraform]]

---

## Définition

`terraform plan` génère un plan d'exécution qui montre exactement ce que Terraform va créer, modifier, ou détruire. C'est l'étape de prévisualisation — aucune modification n'est appliquée.

---

## Pourquoi c'est important

> [!tip] Review avant d'agir
> Toujours exécuter `plan` avant `apply`. Un plan détaille chaque changement avec le signe `+` (create), `~` (update), `-` (destroy). Relire attentivement avant de valider.

---

## Utilisation

```bash
# Plan standard
terraform plan

# Plan avec output dans un fichier
terraform plan -out=tfplan.binary

# Appliquer exactement ce plan
terraform apply tfplan.binary

# Plan pour une ressource spécifique
terraform plan -target=aws_instance.web

# Plan avec variables
terraform plan -var="environment=production" -var-file=prod.tfvars

# Sortie JSON (pour outils d'analyse)
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary | jq '.resource_changes[] | select(.change.actions | contains(["delete"]))'
```

---

## Lire un plan

```
# aws_instance.web will be created
+ resource "aws_instance" "web" {
    + ami                         = "ami-0c55b159cbfafe1f0"
    + instance_type               = "t3.medium"
    + tags                        = {
        + "Environment" = "production"
        + "Name"        = "web-server"
      }
  }

Plan: 1 to add, 0 to change, 0 to destroy.
```

---

> [!warning]
> Le symbole `-/+` signifie destroy puis create (replacement). Cela cause un downtime si c'est une instance de production. Vérifier si `create_before_destroy` dans le lifecycle peut éviter ça.
