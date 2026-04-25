---
title: Defaults
tags:
  - beginner
---
# Defaults

---

## Définition

Les valeurs par défaut dans les [[Variables]] [[Terraform]] permettent à un module d'être utilisé sans que l'appelant ne spécifie toutes les valeurs. Les variables sans default sont requises.

---

## Variables requises vs optionnelles

```hcl
# Requise — doit être fournie à l'apply
variable "environment" {
  type        = string
  description = "Target environment (staging/production)"
  # Pas de default
}

# Optionnelle — utilise le défaut si non fournie
variable "instance_type" {
  type    = string
  default = "t3.medium"
}

# Nullable — peut être null pour désactiver
variable "monitoring_interval" {
  type    = number
  default = null   # null = désactivé
}
```

---

## Terraform demande interactivement

```bash
terraform apply
# var.environment
#   Target environment (staging/production)
#
#   Enter a value: production
```

---

## Bonnes pratiques

```hcl
# Défauts sûrs pour dev/test, overrider pour prod
variable "deletion_protection" {
  type    = bool
  default = false    # false en dev pour faciliter les tests
}

# Dans prod.tfvars :
# deletion_protection = true
```
