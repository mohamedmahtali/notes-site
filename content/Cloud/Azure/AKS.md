---
title: AKS
tags:
  - intermediate
---
# AKS

---

## Définition

[[Azure]] [[Kubernetes]] Service (AKS) est le service Kubernetes managé d'Azure. Il s'intègre nativement avec [[Azure AD]] ([[RBAC]]), Azure Container Registry, et Azure Monitor.

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

## Node pools — séparer les workloads

```bash
# Ajouter un node pool GPU pour les workloads ML
az aks nodepool add \
  --resource-group myapp-rg \
  --cluster-name my-aks-cluster \
  --name gpupool \
  --node-count 2 \
  --node-vm-size Standard_NC6 \
  --node-taints "sku=gpu:NoSchedule" \
  --labels workload=ml

# Scaler un node pool manuellement
az aks nodepool scale \
  --resource-group myapp-rg \
  --cluster-name my-aks-cluster \
  --name nodepool1 \
  --node-count 5

# Mettre à jour le node pool (upgrade OS)
az aks nodepool upgrade \
  --resource-group myapp-rg \
  --cluster-name my-aks-cluster \
  --name nodepool1 \
  --kubernetes-version 1.29.0
```

## Monitoring avec Azure Monitor

```bash
# Activer Container Insights
az aks enable-addons \
  --resource-group myapp-rg \
  --name my-aks-cluster \
  --addons monitoring \
  --workspace-resource-id /subscriptions/.../workspaces/my-log-analytics

# Voir les logs de container via Azure CLI
az monitor log-analytics query \
  --workspace my-log-analytics \
  --analytics-query "ContainerLog | where LogEntry contains 'ERROR' | limit 50"
```

## Intégration Azure Container Registry

```bash
# Attacher ACR au cluster AKS (pull d'images sans credentials)
az aks update \
  --resource-group myapp-rg \
  --name my-aks-cluster \
  --attach-acr myregistry

# Vérifier les autorisations
az aks check-acr \
  --resource-group myapp-rg \
  --name my-aks-cluster \
  --acr myregistry.azurecr.io
```

> [!tip]
> Utiliser Azure CNI avec Cilium sur AKS pour des NetworkPolicies avancées et de meilleures performances réseau. Le CNI kubenet par défaut a des limitations pour les gros [[Cluster]].
