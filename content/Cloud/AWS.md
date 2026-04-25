---
title: AWS
tags:
  - intermediate
---
# AWS

---

## Définition

Amazon Web [[Services]] (AWS) est le leader mondial du [[Cloud]] avec plus de 200 services. Lancé en 2006, il couvre compute, stockage, bases de données, réseau, ML, IoT, et plus encore.

---

## Services fondamentaux

| Catégorie | Service | Description |
|---|---|---|
| Compute | EC2 | Machines virtuelles |
| Compute | Lambda | Fonctions serverless |
| Stockage | S3 | [[Object storage]] |
| Stockage | EBS | Block storage pour EC2 |
| BDD | RDS | Bases de données managées |
| Réseau | VPC | Réseau privé virtuel |
| IAM | IAM | Identité et accès |
| Container | EKS | [[Kubernetes]] managé |
| Container | ECS | Container service AWS natif |

---

## Configuration CLI

```bash
# Installer et configurer
pip install awscli
aws configure
# AWS Access Key ID: ...
# AWS Secret Access Key: ...
# Default region name: eu-west-1
# Default output format: json

# Vérifier
aws sts get-caller-identity
aws ec2 describe-regions --output table
```

---

> [!note]
> Voir [[EC2]], [[S3]], [[IAM]], [[VPC]], [[EKS]] pour les services détaillés.
