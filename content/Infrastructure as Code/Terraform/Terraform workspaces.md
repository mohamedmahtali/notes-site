---
title: Terraform workspaces
tags:
  - intermediate
---
# Terraform workspaces

## Parent
- [[Terraform]]

---

## Définition

Les workspaces Terraform permettent de gérer plusieurs instances d'une même configuration avec des states séparés. Pratique pour gérer staging/production depuis le même code.

---

## Commandes

```bash
# Lister les workspaces
terraform workspace list
# * default
#   staging
#   production

# Créer un workspace
terraform workspace new staging
terraform workspace new production

# Changer de workspace
terraform workspace select production

# Workspace actuel
terraform workspace show
```

---

## Utilisation dans le code

```hcl
locals {
  env_config = {
    default = {
      instance_type = "t3.micro"
      replicas      = 1
    }
    staging = {
      instance_type = "t3.medium"
      replicas      = 2
    }
    production = {
      instance_type = "t3.large"
      replicas      = 5
    }
  }
  config = local.env_config[terraform.workspace]
}

resource "aws_instance" "web" {
  count         = local.config.replicas
  instance_type = local.config.instance_type
}
```

---

> [!warning]
> Les workspaces partagent les providers et modules mais ont des states séparés. Pour des environnements vraiment isolés (comptes AWS séparés, projets GCP séparés), préférer des répertoires séparés avec des backends séparés.
