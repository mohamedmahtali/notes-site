---
title: get
tags:
  - beginner
---
# get

## Parent
- [[kubectl]]

---

## Définition

`kubectl get` liste les ressources Kubernetes avec leur statut. C'est la commande la plus utilisée pour observer l'état du cluster.

---

## Syntaxe et exemples

```bash
# Ressource unique
kubectl get pods
kubectl get pod myapp-abc12
kubectl get svc,deploy,pods       # plusieurs types

# Namespace
kubectl get pods -n kube-system
kubectl get pods --all-namespaces
kubectl get pods -A               # raccourci

# Formats de sortie
kubectl get pods -o wide          # colonnes supplémentaires (IP, node)
kubectl get pod myapp -o yaml     # YAML complet
kubectl get pod myapp -o json     # JSON
kubectl get pod myapp -o jsonpath='{.status.podIP}'

# Labels et filtres
kubectl get pods -l app=myapp
kubectl get pods -l 'env in (prod,staging)'
kubectl get pods --field-selector status.phase=Running

# Watch (mise à jour en temps réel)
kubectl get pods -w
kubectl get pods --watch

# Tri
kubectl get pods --sort-by='.metadata.creationTimestamp'
```

---

## Abréviations utiles

```bash
kubectl get po    # pods
kubectl get svc   # services
kubectl get deploy # deployments
kubectl get rs    # replicasets
kubectl get cm    # configmaps
kubectl get pvc   # persistentvolumeclaims
kubectl get ns    # namespaces
```
