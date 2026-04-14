---
title: kubectl
tags:
  - beginner
---
# kubectl

## Parent
- [[Kubernetes]]

## Enfants
- [[get]]
- [[apply]]
- [[describe]]
- [[logs]]
- [[exec]]

---

## Définition

kubectl est l'outil CLI officiel pour interagir avec un cluster Kubernetes. Il communique avec l'API server et permet de gérer toutes les ressources Kubernetes : pods, services, deployments, etc.

---

## Configuration

```bash
# Fichier de config
cat ~/.kube/config

# Voir les contextes disponibles
kubectl config get-contexts

# Changer de contexte (cluster)
kubectl config use-context production-cluster

# Changer de namespace par défaut
kubectl config set-context --current --namespace=production
```

---

## Commandes essentielles

```bash
# Ressources courantes
kubectl get pods,services,deployments
kubectl get all                         # tout dans le namespace

# Format de sortie
kubectl get pods -o wide               # IPs et nodes
kubectl get pod myapp -o yaml          # YAML complet
kubectl get pods -o jsonpath='{.items[*].metadata.name}'

# Opérations
kubectl apply -f manifest.yaml         # créer/mettre à jour
kubectl delete -f manifest.yaml        # supprimer
kubectl diff -f manifest.yaml          # voir les changements avant apply

# Debug
kubectl describe pod myapp             # détails + events
kubectl logs myapp -f                  # logs en direct
kubectl exec -it myapp -- /bin/sh      # shell dans le pod
```

---

## Alias utiles

```bash
alias k=kubectl
alias kgp='kubectl get pods'
alias kgs='kubectl get services'
alias kgd='kubectl get deployments'
alias kdp='kubectl describe pod'

# Complétion bash
source <(kubectl completion bash)
```
