---
title: Drift
tags:
  - intermediate
---
# Drift

## Parent
- [[Terraform state]]

---

## Définition

Le drift est la divergence entre l'infrastructure réelle (dans le cloud) et l'état Terraform (dans le state). Il se produit quand des modifications sont faites manuellement dans la console cloud sans passer par Terraform.

---

## Détecter le drift

```bash
# terraform plan détecte les drifts
terraform plan
# Si l'infra a été modifiée manuellement :
# ~ resource "aws_instance" "web" {
#     ~ instance_type = "t3.medium" -> "t3.large"  # changé manuellement !
#   }

# Refresh explicite du state
terraform refresh

# Vérification de drift dans CI (sans appliquer)
terraform plan -detailed-exitcode
# Exit code 0: pas de changement
# Exit code 1: erreur
# Exit code 2: changements détectés (drift ou code modifié)
```

---

## Corriger le drift

```bash
# Option 1 : appliquer le code Terraform (revenir à l'état désiré)
terraform apply    # remet l'instance en t3.medium

# Option 2 : mettre à jour le code pour refléter le changement
# Modifier main.tf : instance_type = "t3.large"
# puis : terraform apply (pas de changement si code = réalité)
```

---

> [!tip]
> Configurer une alerte CI qui tourne `terraform plan` toutes les nuits pour détecter le drift. Un drift non détecté peut mener à des surprises lors du prochain apply.
