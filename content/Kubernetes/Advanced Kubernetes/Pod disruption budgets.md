---
title: Pod disruption budgets
tags:
  - advanced
---
# Pod disruption budgets

---

## Définition

Un PodDisruptionBudget (PDB) limite le nombre de [[Pods]] simultanément indisponibles lors d'opérations de maintenance (drain d'un [[Node]], rolling update, [[Cluster]] upgrade). Il garantit la disponibilité minimale de l'application.

---

## Pourquoi c'est important

> [!tip] Protéger la disponibilité lors des maintenances
> Sans PDB, `kubectl drain node-1` peut supprimer tous les pods d'un Deployment si tous sont sur ce node. Le PDB garantit qu'au minimum X pods restent disponibles pendant l'opération.

---

## Manifeste

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
spec:
  selector:
    matchLabels:
      app: myapp
  # Choisir l'un ou l'autre :
  minAvailable: 2           # minimum 2 pods disponibles en permanence
  # maxUnavailable: 1       # maximum 1 pod indisponible à la fois
  # Ou en pourcentage :
  # minAvailable: "50%"
```

---

## Interaction avec kubectl drain

```bash
# drain respecte les PDB
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data

# Si le PDB n'est pas satisfait, drain attend
# Pour forcer (dangereux) :
kubectl drain node-1 --disable-eviction

# Voir les PDB
kubectl get pdb
# NAME        MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS
# myapp-pdb   2               N/A               1
```

---

> [!tip]
> Configurer un PDB pour chaque Deployment critique en production. Règle générale : `minAvailable: ceil(replicas * 0.5)` pour garantir 50% de capacité pendant les mises à jour.
