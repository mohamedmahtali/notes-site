---
title: State locking
tags:
  - intermediate
---
# State locking

---

## Définition

Le state locking empêche plusieurs opérations [[Terraform]] concurrentes de modifier le state simultanément. Sans locking, deux `terraform apply` en parallèle peuvent corrompre le state.

---

## Mécanisme AWS (DynamoDB)

```hcl
terraform {
  backend "s3" {
    bucket         = "mycompany-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "terraform-state-lock"   # active le locking
  }
}
```

```bash
# Quand un apply tourne, DynamoDB contient :
# LockID: "mycompany-terraform-state/prod/terraform.tfstate"
# Info: {"ID":"...","Operation":"OperationTypeApply","Who":"alice@..."}

# Si un autre apply tente de démarrer :
# Error: Error locking state: Error acquiring the state lock
```

---

## Forcer la libération d'un lock (lock orphelin)

```bash
# Si un apply a crashé et laissé un lock orphelin
terraform force-unlock LOCK-ID

# Trouver le LOCK-ID dans le message d'erreur ou dans DynamoDB
aws dynamodb scan --table-name terraform-state-lock
```

---

> [!warning]
> Ne jamais `force-unlock` si un autre apply tourne vraiment. Vérifier d'abord qu'il n'y a pas d'opération en cours. Un force-unlock d'un apply actif peut corrompre le state.
