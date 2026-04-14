---
title: GKE
tags:
  - intermediate
---
# GKE

## Parent
- [[Google Cloud]]

---

## Définition

Google Kubernetes Engine (GKE) est le service Kubernetes managé de GCP. C'est le plus mature des K8s managés (Google est l'inventeur de Kubernetes). GKE propose Autopilot (serverless nodes) et Standard (nodes gérés par l'utilisateur).

---

## Créer un cluster

```bash
# Cluster Autopilot (recommandé — serverless nodes)
gcloud container clusters create-auto my-cluster   --region europe-west1   --release-channel regular

# Cluster Standard
gcloud container clusters create my-cluster   --num-nodes=3   --machine-type=e2-standard-4   --region=europe-west1   --enable-autoscaling   --min-nodes=1 --max-nodes=10

# Configurer kubectl
gcloud container clusters get-credentials my-cluster --region europe-west1

# Vérifier
kubectl get nodes
```

---

## Autopilot vs Standard

| | Autopilot | Standard |
|---|---|---|
| Nodes | Gérés par Google | Gérés par l'utilisateur |
| Facturation | Par pod | Par node |
| Sécurité | Renforcée | Configurable |
| Contrôle | Limité | Total |

---

> [!tip]
> GKE Autopilot est idéal pour la plupart des équipes : zéro gestion des nodes, scaling automatique, facturation à la requête. Standard si tu as besoin de nodes GPU ou de configuration fine des nodes.
