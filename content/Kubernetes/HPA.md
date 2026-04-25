---
title: HPA
tags:
  - intermediate
---
# HPA

---

## Définition

Le Horizontal Pod Autoscaler (HPA) ajuste automatiquement le nombre de réplicas d'un Deployment en fonction de métriques (CPU, mémoire, métriques custom). Il scale out quand la charge augmente et scale in quand elle diminue.

---

## Pourquoi c'est important

> [!tip] Élasticité sans intervention manuelle
> Sans HPA : surprovisionnement coûteux en permanence, ou sous-provisionnement avec dégradation lors des pics. Avec HPA : le nombre de [[Pods]] s'adapte automatiquement à la charge réelle.

---

## Configuration rapide

```bash
# Créer un HPA sur un Deployment existant
kubectl autoscale deployment myapp   --min=2   --max=10   --cpu-percent=70

# Voir le HPA
kubectl get hpa
kubectl describe hpa myapp
```

---

## YAML complet

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

---

> [!warning]
> L'HPA nécessite que les pods aient des `resources.requests` définis — sans requests, le HPA ne peut pas calculer l'utilisation en pourcentage. Installer [[Metrics]]-server pour les métriques CPU/mémoire.
