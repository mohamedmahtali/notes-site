---
title: AWS provider
tags:
  - intermediate
---
# AWS provider

## Parent
- [[Terraform providers]]

---

## Définition

Le provider AWS est le plus utilisé dans l'écosystème Terraform. Il expose plus de 1000 ressources et data sources pour gérer l'ensemble des services AWS.

---

## Configuration

```hcl
provider "aws" {
  region = "eu-west-1"

  # Authentification (dans cet ordre de priorité) :
  # 1. Variables d'environnement AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY
  # 2. Fichier ~/.aws/credentials
  # 3. Instance profile EC2 / EKS IAM role
  # 4. Terraform Cloud workspace variables

  # Provider multiple (multi-région)
  alias  = "us-east-1"
  region = "us-east-1"
}

# Utiliser le provider alias
resource "aws_instance" "us" {
  provider      = aws.us-east-1
  ami           = data.aws_ami.ubuntu_us.id
  instance_type = "t3.micro"
}
```

---

## Data sources courants

```hcl
# Récupérer l'AMI Ubuntu la plus récente
data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-22.04-amd64-server-*"]
  }
  owners = ["099720109477"]  # Canonical
}

# Récupérer le VPC par défaut
data "aws_vpc" "default" {
  default = true
}

# Récupérer les AZs disponibles
data "aws_availability_zones" "available" {
  state = "available"
}
```
