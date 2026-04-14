---
title: API server
tags:
  - advanced
---
# API server

## Parent
- [[Control plane]]

---

## Définition

Le kube-apiserver est le point d'entrée central du cluster Kubernetes. Il expose l'API REST Kubernetes et traite toutes les requêtes (kubectl, controllers, kubelet). Toutes les opérations passent par lui — c'est le seul composant qui parle directement à etcd.

---

## Pourquoi c'est important

> [!note] Le cerveau du cluster
> Tout passe par l'API server : création de pods, mise à jour de ConfigMaps, requêtes des controllers. Il authentifie, autorise (RBAC), et valide chaque requête avant de la persister dans etcd.

---

## Architecture

```
kubectl → API Server → etcd (persistance)
                     ← Controllers (watch)
                     ← kubelet (node status)
                     ← Scheduler (pod binding)
```

---

## Commandes utiles

```bash
# Vérifier la version de l'API server
kubectl version --short

# Lister toutes les ressources API disponibles
kubectl api-resources

# Lister toutes les versions d'API
kubectl api-versions

# Accès direct à l'API (avec proxy)
kubectl proxy &
curl http://localhost:8001/api/v1/namespaces

# Voir les logs de l'API server (cluster kubeadm)
kubectl logs -n kube-system kube-apiserver-$(hostname)

# Audit logs
# configurés via --audit-log-path dans les flags de l'API server
```

---

> [!tip]
> L'API server supporte le watch — les controllers n'interrogent pas en boucle mais souscrivent aux changements. C'est ce qui rend Kubernetes réactif sans polling constant.
