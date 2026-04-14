---
title: Reclaim policies
tags:
  - intermediate
---
# Reclaim policies

## Parent
- [[Persistent volumes]]

---

## Définition

La reclaim policy définit ce qui arrive au PersistentVolume quand le PVC qui l'utilise est supprimé. Elle détermine si les données sont conservées ou supprimées.

---

## Politiques disponibles

| Politique | Description | Usage |
|---|---|---|
| `Delete` | PV et stockage sous-jacent supprimés | Environnements éphémères |
| `Retain` | PV reste (status Released), données intactes | Production, données critiques |
| `Recycle` | Efface les données et rend le PV disponible | Déprécié |

---

## Modifier la reclaim policy

```bash
# Sur un PV existant
kubectl patch pv pv-data-1   -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'

# Dans la StorageClass
spec:
  reclaimPolicy: Retain   # tous les PVs créés auront cette politique
```

---

## Récupérer un PV Retained

```bash
# Après suppression du PVC, le PV est en "Released"
kubectl get pv    # STATUS: Released

# Pour réutiliser manuellement :
# 1. Supprimer le claimRef du PV
kubectl patch pv pv-data-1 --type=json   -p='[{"op":"remove","path":"/spec/claimRef"}]'
# → STATUS: Available

# 2. Créer un nouveau PVC qui pointe vers ce PV
spec:
  volumeName: pv-data-1   # lier au PV spécifique
```

---

> [!warning]
> `Delete` est pratique mais dangereux pour les données de production. Toujours utiliser `Retain` pour les bases de données et les données critiques.
