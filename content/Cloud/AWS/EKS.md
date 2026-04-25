---
title: EKS
tags:
  - intermediate
---
# EKS

---

## Définition

Amazon EKS (Elastic [[Kubernetes]] Service) est le service Kubernetes managé d'[[AWS]]. AWS gère le [[Control plane]] ([[API server]], [[etcd]], [[Scheduler]]), toi tu gères les [[Node]] workers et les workloads.

---

## Création d'un cluster

```bash
# Avec eksctl (recommandé)
eksctl create cluster   --name my-cluster   --region eu-west-1   --node-type t3.medium   --nodes 3   --nodes-min 2   --nodes-max 10   --managed

# Configurer kubectl
aws eks update-kubeconfig   --region eu-west-1   --name my-cluster

# Vérifier
kubectl get nodes
```

---

## Node groups

```bash
# Managed node group (recommandé)
eksctl create nodegroup   --cluster my-cluster   --name ng-spot   --instance-types t3.medium,t3a.medium   --spot   --nodes-min 0   --nodes-max 10

# Fargate (serverless nodes)
eksctl create fargateprofile   --cluster my-cluster   --name my-app   --namespace my-namespace
```

---

## IAM pour les pods (IRSA)

```bash
# Créer un service account avec rôle IAM
eksctl create iamserviceaccount   --cluster my-cluster   --namespace production   --name myapp-sa   --attach-policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess   --approve
```

---

> [!tip]
> Utiliser Karpenter plutôt que [[Cluster]] Autoscaler pour l'[[Autoscaling]] des nodes — plus rapide, plus économique (sélection optimale des [[Types]] d'instances).
