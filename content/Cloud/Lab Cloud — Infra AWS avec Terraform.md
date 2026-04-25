---
title: "Lab Cloud — Infra AWS avec Terraform"
tags:
  - cloud
  - intermediate
---

# Lab Cloud — Infra AWS avec Terraform

## Objectif

Provisionner une infrastructure AWS complète avec Terraform : VPC, sous-réseaux, [[Security [[Groups]]]], une instance [[EC2]] avec user-data, et un bucket S3.

> [!warning] Coût AWS
> Ce lab crée des ressources AWS facturées. Penser à `terraform destroy` à la fin. Coût estimé < 0.10€ si détruit dans l'heure.

> [!note] Prérequis
> - Compte AWS avec accès programmatique (Access Key + Secret Key)
> - Terraform installé (`terraform version`)
> - AWS CLI configuré (`aws configure`)

---

## Étape 1 — Structure du projet

```bash
mkdir aws-lab && cd aws-lab

# Fichiers à créer :
# main.tf, variables.tf, outputs.tf, terraform.tfvars
```

---

## Étape 2 — Variables et provider

```hcl
# variables.tf
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "devops-lab"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}
```

```hcl
# terraform.tfvars
aws_region   = "eu-west-1"
project_name = "devops-lab"
environment  = "dev"
```

---

## Étape 3 — Infrastructure principale

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# ── VPC ──────────────────────────────────────────────
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = { Name = "${var.project_name}-vpc" }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  tags   = { Name = "${var.project_name}-igw" }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "${var.aws_region}a"
  tags = { Name = "${var.project_name}-public-subnet" }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# ── Security Group ────────────────────────────────────
resource "aws_security_group" "web" {
  name   = "${var.project_name}-web-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Restreindre à ton IP en prod !
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ── EC2 ──────────────────────────────────────────────
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-22.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = <<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y nginx
    systemctl start nginx
    systemctl enable nginx
    echo "<h1>Hello from Terraform! Env: ${var.environment}</h1>" > /var/www/html/index.html
  EOF

  tags = { Name = "${var.project_name}-web" }
}

# ── S3 Bucket ────────────────────────────────────────
resource "aws_s3_bucket" "assets" {
  bucket = "${var.project_name}-assets-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
  byte_length = 4
}

resource "aws_s3_bucket_versioning" "assets" {
  bucket = aws_s3_bucket.assets.id
  versioning_configuration { status = "Enabled" }
}
```

```hcl
# outputs.tf
output "web_public_ip" {
  value = aws_instance.web.public_ip
}

output "web_url" {
  value = "http://${aws_instance.web.public_ip}"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.assets.bucket
}
```

---

## Étape 4 — Appliquer

```bash
terraform init
terraform fmt
terraform validate
terraform plan

terraform apply   # Confirmer avec "yes"
```

---

## Étape 5 — Vérifier et détruire

```bash
# Tester
curl $(terraform output -raw web_url)

# Voir les ressources créées
terraform state list

# Détruire (IMPORTANT - éviter les frais)
terraform destroy
```

---

## Vérification finale

- [ ] `terraform apply` sans erreur
- [ ] Page [[Nginx]] accessible via l'IP publique
- [ ] Bucket S3 créé avec [[Versioning]] activé
- [ ] `terraform destroy` nettoie tout

## Liens

- [[Cloud]]
- [[AWS]]
- [[Terraform]]
- [[VPC]]
- [[IAM]]
