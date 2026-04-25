---
title: Namespaces
tags:
  - beginner
---
# Namespaces

---

## Définition

Les namespaces sont des [[Partitions]] virtuelles d'un [[Cluster]] [[Kubernetes]]. Ils isolent les ressources ([[Pods]], [[Services]], [[ConfigMaps]]) entre équipes ou environnements. Par défaut, Kubernetes crée 4 namespaces.

---

## Namespaces par défaut

| Namespace | Usage |
|---|---|
| `default` | Ressources créées sans namespace explicite |
| `kube-system` | Composants Kubernetes ([[API server]], [[Scheduler]], [[DNS]]) |
| `kube-public` | Données accessibles sans authentification |
| `kube-node-lease` | Heartbeats des [[Node]] |

---

## Gestion des namespaces

```bash
# Lister les namespaces
kubectl get namespaces
kubectl get ns

# Créer un namespace
kubectl create namespace production
kubectl create ns staging

# YAML
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    env: production
EOF

# Travailler dans un namespace
kubectl get pods -n production
kubectl apply -f app.yaml -n production

# Namespace par défaut pour la session
kubectl config set-context --current --namespace=production

# Supprimer (supprime toutes les ressources dedans)
kubectl delete namespace staging
```

---

> [!warning]
> `kubectl delete namespace` supprime TOUTES les ressources dans le namespace. Irréversible. Toujours vérifier avant d'exécuter.
