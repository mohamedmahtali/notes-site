---
title: Cloud controller manager
tags:
  - advanced
---
# Cloud controller manager

## Parent
- [[Control plane]]

---

## Définition

Le Cloud Controller Manager (CCM) est le composant qui intègre Kubernetes avec l'API du cloud provider (AWS, GCP, Azure). Il gère les ressources cloud spécifiques : load balancers, disques persistants, routes réseau.

---

## Rôle du CCM

```
Service type: LoadBalancer
    → CCM crée un AWS ELB / GCP Load Balancer / Azure LB

PersistentVolumeClaim (StorageClass: gp2)
    → CCM provisionne un AWS EBS volume

Node joins cluster
    → CCM récupère les informations cloud du node (zone, instance type)
    → Ajoute les labels cloud.google.com/gke-nodepool, topology.kubernetes.io/zone
```

---

## Controllers dans le CCM

| Controller | Fonction |
|---|---|
| Node controller | Synchronise l'état des nodes avec l'API cloud |
| Route controller | Configure les routes réseau dans le VPC |
| Service controller | Crée/supprime les load balancers cloud |

---

## Sans CCM (cluster on-premise)

Sur des clusters bare-metal ou on-premise, le CCM est absent. Pour avoir des LoadBalancers, utiliser MetalLB. Pour du stockage dynamique, utiliser les CSI drivers appropriés.

```bash
# Voir si le CCM tourne
kubectl get pods -n kube-system | grep cloud-controller

# Labels ajoutés par le CCM sur les nodes
kubectl get node worker-1 -o jsonpath='{.metadata.labels}' | jq .
```

---

> [!note]
> Depuis Kubernetes 1.11, le CCM est un binaire séparé du kube-controller-manager. Chaque cloud provider maintient son propre CCM (aws-cloud-controller-manager, gke-cloud-controller-manager, etc.).
