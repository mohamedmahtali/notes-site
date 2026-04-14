---
title: Remote state
tags:
  - intermediate
---
# Remote state

## Parent
- [[Terraform state]]

---

## Définition

Le remote state stocke `terraform.tfstate` dans un backend distant (S3, GCS, Azure Blob, Terraform Cloud). Indispensable en équipe pour partager l'état et éviter les conflits.

---

## Backend S3 (recommandé AWS)

```hcl
# versions.tf
terraform {
  backend "s3" {
    bucket         = "mycompany-terraform-state"
    key            = "production/app/terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"   # pour le locking
  }
}
```

---

## Créer le bucket S3 et la table DynamoDB

```bash
# Bucket S3
aws s3 mb s3://mycompany-terraform-state --region eu-west-1
aws s3api put-bucket-versioning   --bucket mycompany-terraform-state   --versioning-configuration Status=Enabled

# Table DynamoDB pour le locking
aws dynamodb create-table   --table-name terraform-state-lock   --attribute-definitions AttributeName=LockID,AttributeType=S   --key-schema AttributeName=LockID,KeyType=HASH   --billing-mode PAY_PER_REQUEST
```

---

## Backend GCS (GCP)

```hcl
terraform {
  backend "gcs" {
    bucket = "mycompany-terraform-state"
    prefix = "production/app"
  }
}
```

---

## Accès au state depuis un autre module

```hcl
data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "mycompany-terraform-state"
    key    = "production/network/terraform.tfstate"
    region = "eu-west-1"
  }
}

resource "aws_instance" "web" {
  subnet_id = data.terraform_remote_state.network.outputs.private_subnet_id
}
```
