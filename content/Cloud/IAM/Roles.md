---
title: Roles
tags:
  - intermediate
---
# Roles

## Parent
- [[IAM]]

---

## Définition

Les IAM roles sont des identités assumables par des services, instances EC2, fonctions Lambda, ou des utilisateurs d'autres comptes. Ils utilisent des credentials temporaires (STS) — plus sécurisés que les access keys permanentes.

---

## Cas d'usage

- EC2 accède à S3 sans access keys hardcodées
- Lambda lit/écrit dans DynamoDB
- Cross-account access entre comptes AWS
- OIDC federated access (GitHub Actions → AWS)

---

## EC2 Instance Profile

```bash
# Créer un rôle pour EC2
aws iam create-role   --role-name EC2-S3-Access   --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ec2.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attacher une politique
aws iam attach-role-policy   --role-name EC2-S3-Access   --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Créer l'instance profile
aws iam create-instance-profile --instance-profile-name EC2-S3-Access
aws iam add-role-to-instance-profile   --instance-profile-name EC2-S3-Access --role-name EC2-S3-Access
```

---

## GitHub Actions → AWS (OIDC)

```yaml
# Dans le workflow GitHub Actions
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::ACCOUNT:role/github-actions
    aws-region: eu-west-1
    # Pas de secrets nécessaires — utilise OIDC
```
