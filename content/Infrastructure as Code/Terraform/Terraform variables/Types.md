---
title: Types
tags:
  - beginner
---
# Types

## Parent
- [[Terraform variables]]

---

## Définition

Terraform supporte plusieurs types de variables : primitifs (string, number, bool) et complexes (list, set, map, object, tuple).

---

## Types et exemples

```hcl
# string
variable "region" {
  type    = string
  default = "eu-west-1"
}

# number
variable "port" {
  type    = number
  default = 8080
}

# bool
variable "enable_https" {
  type    = bool
  default = true
}

# list(string)
variable "availability_zones" {
  type    = list(string)
  default = ["eu-west-1a", "eu-west-1b"]
}

# map(string)
variable "tags" {
  type = map(string)
  default = {
    Project = "myapp"
    Owner   = "platform-team"
  }
}

# object (struct typé)
variable "database" {
  type = object({
    engine  = string
    version = string
    size    = number
  })
  default = {
    engine  = "postgres"
    version = "15"
    size    = 20
  }
}
```

---

> [!tip]
> Utiliser `object` pour les variables complexes plutôt que des maps non-typées — cela permet la validation et l'autocomplétion dans les éditeurs.
