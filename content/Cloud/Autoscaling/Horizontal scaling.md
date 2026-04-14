---
title: Horizontal scaling
tags:
  - beginner
---
# Horizontal scaling

## Parent
- [[Autoscaling]]

---

## Définition

Le scaling horizontal (scale out/in) ajoute ou retire des instances identiques pour gérer la charge. C'est la forme d'autoscaling la plus courante en cloud car elle permet une disponibilité continue sans interruption.

---

## AWS Auto Scaling — Target Tracking

```bash
# Scale automatiquement pour maintenir CPU à 70%
aws autoscaling put-scaling-policy   --auto-scaling-group-name myapp-asg   --policy-name cpu-tracking   --policy-type TargetTrackingScaling   --target-tracking-configuration '{
    "TargetValue": 70.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    },
    "ScaleInCooldown": 300,
    "ScaleOutCooldown": 60
  }'
```

---

## Avantages vs Vertical

| Aspect | Horizontal | Vertical |
|---|---|---|
| Disponibilité | Pas d'interruption | Redémarrage requis |
| Scalabilité | Quasi-illimitée | Limité par les types d'instance |
| Coût | Linéaire | Non-linéaire |
| Complexité app | Doit être stateless | Peut être stateful |
