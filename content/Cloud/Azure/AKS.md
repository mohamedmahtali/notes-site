---
title: AKS
tags:
  - intermediate
---
# AKS

## Parent
- [[Azure]]

---

## Définition

Azure Kubernetes Service (AKS) est le service Kubernetes managé d'Azure. Il s'intègre nativement avec Azure AD (RBAC), Azure Container Registry, et Azure Monitor.

---

## Créer un cluster AKS

```bash
# Créer le cluster
az aks create   --resource-group myapp-rg   --name my-aks-cluster   --node-count 3   --node-vm-size Standard_D2s_v3   --enable-cluster-autoscaler   --min-count 1 --max-count 10   --generate-ssh-keys   --enable-azure-rbac

# Configurer kubectl
az aks get-credentials   --resource-group myapp-rg   --name my-aks-cluster

kubectl get nodes
```

---

## Workload Identity (remplace les Service Principals)

```bash
az aks update   --resource-group myapp-rg   --name my-aks-cluster   --enable-oidc-issuer   --enable-workload-identity
```

---

> [!tip]
> Utiliser Azure CNI avec Cilium sur AKS pour des NetworkPolicies avancées et de meilleures performances réseau. Le CNI kubenet par défaut a des limitations pour les gros clusters.
