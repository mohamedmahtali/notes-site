---
title: "IaC + GitOps : l'infrastructure pilotée par Git"
tags:
  - connexion
  - iac
  - gitops
  - intermediate
---

# IaC + GitOps : l'infrastructure pilotée par Git

## La synergie

[[Infrastructure as Code]] (IaC) et [[GitOps]] sont deux faces d'une même philosophie : **tout dans Git, rien de manuel**. IaC décrit l'infrastructure en code. GitOps utilise Git comme source de vérité et réconcilie automatiquement l'état réel vers l'état déclaré.

```
┌─────────────────────────────────────────────────┐
│                  Git Repository                  │
│                                                  │
│   infra/               apps/                     │
│   ├── main.tf          ├── deployment.yaml       │
│   ├── vpc.tf           ├── service.yaml          │
│   └── eks.tf           └── ingress.yaml          │
│         │                      │                 │
└─────────┼──────────────────────┼─────────────────┘
          │                      │
          ▼                      ▼
    Terraform              ArgoCD / Flux
    (IaC)                  (GitOps agent)
          │                      │
          ▼                      ▼
    Cloud Provider          Kubernetes Cluster
    (AWS, GCP, Azure)       (apps déployées)
```

## Qui fait quoi

| Outil | Domaine | Déclenchement |
|-------|---------|---------------|
| **[[Terraform]]** | Infra cloud (VPC, EKS, RDS...) | CI/CD ou manuel (`terraform apply`) |
| **[[Ansible]]** | Configuration système (packages, users) | Pipeline ou playbook |
| **[[ArgoCD]]** | Apps Kubernetes (Deployments, Services) | Pull automatique depuis Git |
| **[[Flux]]** | Apps Kubernetes + Helm charts | Pull automatique depuis Git |

## Workflow typique

```
1. PR : modifier infra/eks.tf (changer la taille des nœuds)
   │
   ▼
2. terraform plan → revue dans la PR
   │
   ▼
3. Merge PR → terraform apply (via CI/CD)
   │  Le cluster EKS est redimensionné
   ▼
4. PR : modifier apps/deployment.yaml (nouvelle version)
   │
   ▼
5. Merge PR → ArgoCD détecte la différence
   │
   ▼
6. ArgoCD réconcilie → rolling update dans K8s
```

## Séparation des responsabilités

```
Terraform = "construire la maison"
  → VPC, subnets, cluster Kubernetes, bases de données,
    buckets S3, certificats, DNS...

GitOps (ArgoCD/Flux) = "meubler et gérer la maison"
  → Déployer les applications dans le cluster,
    gérer les versions, rollbacks, environments...
```

> [!tip] Deux repos ou un seul ?
> Pattern courant : **repo infra** (Terraform) séparé du **repo app** (manifests K8s). Cela permet des cycles de release indépendants — l'infra change rarement, les apps souvent.

## Points d'attention

> [!warning] Terraform state = source de vérité de l'infra
> Le [[Terraform state]] doit être partagé (backend S3 + DynamoDB lock) et jamais modifié manuellement. ArgoCD ne connaît pas le state Terraform — les deux systèmes sont indépendants.

> [!warning] Éviter le drift
> Si quelqu'un modifie une ressource cloud manuellement (console AWS), Terraform et GitOps ne le savent pas. Les deux outils détectent le drift lors du prochain `plan` ou `sync`, mais il faut le corriger.

## Pour aller plus loin

- [[Terraform]] — plan, apply, destroy, modules
- [[Terraform state]] — backend distant, locking, workspace
- [[ArgoCD]] — Application CRD, sync policies, health checks
- [[Flux]] — Kustomization, HelmRelease, image automation
- [[GitOps]] — principes, pull vs push model
