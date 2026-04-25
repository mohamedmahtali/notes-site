---
title: Terraform variables
tags:
  - beginner
---
# Terraform variables

---

## Définition

Les [[Variables]] [[Terraform]] permettent de paramétrer les configurations pour les rendre réutilisables entre environnements. Elles remplacent les valeurs hardcodées par des paramètres configurables.

---

## Déclaration

```hcl
# variables.tf
variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "staging"
  validation {
    condition     = contains(["staging", "production"], var.environment)
    error_message = "Environment must be staging or production."
  }
}

variable "instance_count" {
  type    = number
  default = 1
}

variable "tags" {
  type = map(string)
  default = {
    Project = "myapp"
    Team    = "platform"
  }
}
```

---

## Utilisation

```hcl
resource "aws_instance" "web" {
  count         = var.instance_count
  instance_type = var.environment == "production" ? "t3.large" : "t3.micro"
  tags          = merge(var.tags, { Environment = var.environment })
}
```

---

## Passer des valeurs

```bash
# CLI
terraform apply -var="environment=production" -var="instance_count=3"

# Fichier
terraform apply -var-file=prod.tfvars

# Variable d'environnement (TF_VAR_*)
export TF_VAR_environment=production
terraform apply
```
