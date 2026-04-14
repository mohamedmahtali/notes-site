---
title: Images
tags:
  - intermediate
---
# Images

## Parent
- [[Virtual machines]]

---

## Définition

Les images de VM (AMI sur AWS, Machine Image sur GCP) sont des snapshots du disque d'une instance qui servent de modèle pour créer de nouvelles VMs. Elles incluent l'OS, les logiciels installés, et la configuration.

---

## Types d'images

| Type | Description |
|---|---|
| Images officielles AWS/GCP | Ubuntu, Amazon Linux, Windows — maintenues par les providers |
| Images marketplace | Logiciels préinstallés (Nginx, Jenkins, GitLab) |
| Custom images | Images créées depuis une instance configurée |
| Golden images | Images de référence de l'entreprise avec sécurité baseline |

---

## Créer une AMI custom

```bash
# 1. Configurer une instance comme souhaité
# 2. Créer l'AMI
aws ec2 create-image   --instance-id i-1234567890abcdef0   --name "myapp-golden-image-v1.0"   --description "Golden image with app stack"

# Lister ses AMIs
aws ec2 describe-images --owners self   --query 'Images[*].[ImageId,Name,CreationDate]' --output table

# Utiliser l'AMI pour lancer une instance
aws ec2 run-instances --image-id ami-custom123 --instance-type t3.medium
```

---

## Packer — automatiser la construction d'images

```hcl
# template.pkr.hcl
source "amazon-ebs" "ubuntu" {
  ami_name      = "myapp-{{timestamp}}"
  instance_type = "t3.micro"
  source_ami_filter {
    filters = { name = "ubuntu/images/hvm-ssd/ubuntu-22.04-amd64-server-*" }
    owners  = ["099720109477"]  # Canonical
    most_recent = true
  }
}

build {
  sources = ["source.amazon-ebs.ubuntu"]
  provisioner "shell" {
    script = "scripts/setup.sh"
  }
}
```
