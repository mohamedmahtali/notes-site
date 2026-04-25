---
title: CPU scaling
tags:
  - intermediate
---
# CPU scaling

---

## Définition

Le CPU scaling avec [[HPA]] augmente le nombre de [[Pods]] quand l'utilisation CPU moyenne dépasse un seuil cible, et les diminue quand elle redescend.

---

## Configuration

```yaml
metrics:
- type: Resource
  resource:
    name: cpu
    target:
      type: Utilization
      averageUtilization: 70    # 70% du CPU request en moyenne
```

---

## Algorithme HPA

```
replicas_désirés = ceil(replicas_actuels × (utilisation_actuelle / cible))

Exemple :
- 5 pods, utilisation CPU à 90%, cible 70%
- replicas = ceil(5 × 90/70) = ceil(6.43) = 7 pods

- 7 pods, utilisation CPU à 40%, cible 70%
- replicas = ceil(7 × 40/70) = ceil(4.0) = 4 pods (scale down)
```

---

## Cooldown

```yaml
spec:
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300   # attendre 5min avant scale down
      policies:
      - type: Percent
        value: 10                         # max 10% de pods en moins à la fois
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0     # scale up immédiat
      policies:
      - type: Percent
        value: 100                        # peut doubler en 15s
        periodSeconds: 15
```

---

> [!tip]
> Configurer `scaleDown.stabilizationWindowSeconds` à 5-10 minutes pour éviter le "flapping" (scale up/down répété). Le scale up doit être rapide, le scale down prudent.
