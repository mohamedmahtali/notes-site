---
title: Google Cloud
tags:
  - intermediate
---
# Google Cloud

## Parent
- [[Cloud]]

## Enfants
- [[Compute Engine]]
- [[GKE]]
- [[Cloud Storage]]
- [[IAM]]

---

## Définition

Google Cloud Platform (GCP) est le troisième cloud provider mondial. Il est reconnu pour ses capacités en data/ML (BigQuery, Vertex AI), son réseau mondial, et Kubernetes (GKE est le plus mature des K8s managés — c'est l'inventeur de K8s).

---

## Services fondamentaux

| Catégorie | Service AWS équivalent | GCP |
|---|---|---|
| VM | EC2 | Compute Engine |
| K8s | EKS | GKE |
| Serverless | Lambda | Cloud Functions / Cloud Run |
| Object storage | S3 | Cloud Storage |
| BDD managée | RDS | Cloud SQL |
| IAM | IAM | Cloud IAM |

---

## Configuration CLI

```bash
# Installer gcloud SDK
curl https://sdk.cloud.google.com | bash
gcloud init

# Configurer le projet
gcloud config set project my-project-id
gcloud config set compute/region europe-west1

# Authentification
gcloud auth login
gcloud auth application-default login   # pour les SDKs

# Vérifier
gcloud config list
gcloud projects list
```
