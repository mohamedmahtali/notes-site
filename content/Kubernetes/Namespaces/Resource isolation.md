---
title: Resource isolation
tags:
  - intermediate
---
# Resource isolation

## Parent
- [[Namespaces]]

---

## Définition

L'isolation des ressources par namespace permet de limiter la consommation de CPU et mémoire d'une équipe ou d'un projet via des ResourceQuotas et LimitRanges, évitant qu'une application consomme toutes les ressources du cluster.

---

## ResourceQuota

```yaml
# Limite les ressources totales dans un namespace
apiVersion: v1
kind: ResourceQuota
metadata:
  name: production-quota
  namespace: production
spec:
  hard:
    requests.cpu: "10"          # total CPU requests du namespace
    requests.memory: 20Gi       # total mémoire requests
    limits.cpu: "20"
    limits.memory: 40Gi
    pods: "50"                  # nombre max de pods
    services: "10"
    persistentvolumeclaims: "20"
```

---

## LimitRange

```yaml
# Définit des defaults et limites par container
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: production
spec:
  limits:
  - type: Container
    default:              # limits par défaut si non spécifiées
      cpu: "500m"
      memory: "256Mi"
    defaultRequest:       # requests par défaut
      cpu: "100m"
      memory: "128Mi"
    max:                  # limites maximales
      cpu: "2"
      memory: "2Gi"
```

---

```bash
# Voir les quotas consommés
kubectl describe resourcequota -n production
kubectl get limitrange -n production
```

---

> [!tip]
> Toujours configurer LimitRange sur les namespaces de dev/staging pour éviter qu'un développeur lance accidentellement un pod sans limits qui consomme tout le cluster.
