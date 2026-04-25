---
title: Cheat sheet Cloud CLI
tags:
  - cloud
  - intermediate
---

# Cheat sheet Cloud CLI

## AWS CLI

```bash
# Configuration
aws configure
aws configure list
aws configure --profile dev

# EC2
aws ec2 describe-instances --output table
aws ec2 describe-instances --filters "Name=tag:Name,Values=web*"
aws ec2 start-instances --instance-ids i-1234567890abcdef0
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
aws ec2 describe-security-groups --group-ids sg-12345

# S3
aws s3 ls                              # Lister les buckets
aws s3 ls s3://mybucket/               # Contenu d'un bucket
aws s3 cp file.txt s3://mybucket/      # Upload
aws s3 sync ./dir s3://mybucket/dir/   # Synchroniser
aws s3 rm s3://mybucket/file.txt       # Supprimer
aws s3api get-bucket-policy --bucket mybucket

# IAM
aws iam list-users
aws iam list-roles
aws iam get-user --user-name alice
aws iam list-attached-user-policies --user-name alice
aws sts get-caller-identity            # Qui suis-je ?

# EKS
aws eks update-kubeconfig --name mycluster --region eu-west-1
aws eks describe-cluster --name mycluster
aws eks list-nodegroups --cluster-name mycluster
```

## gcloud (GCP)

```bash
# Auth & config
gcloud auth login
gcloud config set project my-project-id
gcloud config list

# Compute
gcloud compute instances list
gcloud compute instances start myvm --zone=europe-west1-b
gcloud compute instances stop myvm --zone=europe-west1-b
gcloud compute ssh myvm --zone=europe-west1-b

# GKE
gcloud container clusters get-credentials mycluster --zone europe-west1-b
gcloud container clusters list

# Cloud Storage
gcloud storage ls
gcloud storage cp file.txt gs://mybucket/
gcloud storage ls gs://mybucket/
```

## Azure CLI

```bash
# Auth & config
az login
az account list --output table
az account set --subscription "My Subscription"

# VMs
az vm list --output table
az vm start --name myvm --resource-group mygroup
az vm stop --name myvm --resource-group mygroup

# AKS
az aks get-credentials --name mycluster --resource-group mygroup
az aks list --output table

# Blob Storage
az storage account list
az storage blob list --container-name mycontainer --account-name myaccount
az storage blob upload --file file.txt --container-name mycontainer \
  --name file.txt --account-name myaccount
```

## Liens

- [[Cloud]]
- [[AWS]]
- [[Google Cloud]]
- [[Azure]]
- [[IAM]]
