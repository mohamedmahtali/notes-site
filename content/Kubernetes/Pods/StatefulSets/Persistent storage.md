---
title: Persistent storage
tags:
  - intermediate
---
# Persistent storage

## Parent
- [[StatefulSets]]

---

## Définition

Les StatefulSets créent automatiquement un PersistentVolumeClaim dédié pour chaque pod via les `volumeClaimTemplates`. Ce PVC persiste même si le pod est supprimé ou redémarré — les données survivent au pod.

---

## volumeClaimTemplates

```yaml
spec:
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ReadWriteOnce]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 50Gi
```

Ce template crée :
- `data-postgres-0` (PVC pour postgres-0)
- `data-postgres-1` (PVC pour postgres-1)
- `data-postgres-2` (PVC pour postgres-2)

---

## Cycle de vie des PVC

```bash
# Voir les PVC créés par le StatefulSet
kubectl get pvc -l app=postgres

# Supprimer le StatefulSet NE supprime PAS les PVC
kubectl delete statefulset postgres
kubectl get pvc     # toujours là

# Supprimer les PVC manuellement si nécessaire
kubectl delete pvc data-postgres-0 data-postgres-1 data-postgres-2
```

---

> [!warning]
> La suppression d'un StatefulSet ne supprime pas les PVC — c'est intentionnel pour éviter la perte de données accidentelle. Supprimer les PVC manuellement si les données ne sont plus nécessaires.
