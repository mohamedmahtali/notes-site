---
title: Controller manager
tags:
  - advanced
---
# Controller manager

## Parent
- [[Control plane]]

---

## Définition

Le kube-controller-manager exécute une collection de controllers en boucle continue. Chaque controller surveille l'état du cluster via l'API server et prend des actions pour aligner l'état réel sur l'état désiré.

---

## Controllers intégrés

| Controller | Rôle |
|---|---|
| Node controller | Détecte et gère les nodes défaillants |
| ReplicaSet controller | Maintient le nombre de pods requis |
| Deployment controller | Orchestre les rolling updates |
| Service Account controller | Crée les SA par défaut |
| Namespace controller | Nettoie les ressources quand un NS est supprimé |
| Job controller | Gère les jobs run-to-completion |

---

## Boucle de réconciliation

```
Watch API server pour les changements
    ↓
Comparer état actuel vs état désiré
    ↓
Si divergence → agir (créer/modifier/supprimer)
    ↓
Retourner en attente du prochain événement
```

---

```bash
# Vérifier le controller manager
kubectl get pods -n kube-system | grep controller-manager
kubectl logs -n kube-system kube-controller-manager-$(hostname) | tail -20

# Observer une réconciliation en action
kubectl scale deployment myapp --replicas=5
# Le ReplicaSet controller crée immédiatement les pods manquants
kubectl get pods -w
```

---

> [!note]
> Le controller manager incarne le pattern "reconciliation loop" — la philosophie fondamentale de Kubernetes : déclarer l'état désiré et laisser les controllers le réaliser.
