---
title: Elasticity
tags:
  - beginner
---
# Elasticity

## Parent
- [[Cloud computing]]

---

## Définition

L'élasticité est la capacité d'un système cloud à augmenter ou diminuer automatiquement ses ressources en réponse à la demande, sans intervention manuelle. Scale out lors des pics, scale in quand la demande baisse.

---

## Horizontal vs Vertical

| Type | Description | Cloud |
|---|---|---|
| Scale out (horizontal) | Ajouter plus d'instances | Auto Scaling Groups |
| Scale in | Retirer des instances | Auto Scaling Groups |
| Scale up (vertical) | Instances plus puissantes | Resize d'instance |
| Scale down | Instances moins puissantes | Resize d'instance |

---

## Auto Scaling AWS

```bash
# Créer un Auto Scaling Group
aws autoscaling create-auto-scaling-group   --auto-scaling-group-name my-asg   --min-size 2   --max-size 10   --desired-capacity 3   --launch-template LaunchTemplateId=lt-0123456789abcdef0

# Configurer une politique de scaling
aws autoscaling put-scaling-policy   --auto-scaling-group-name my-asg   --policy-name cpu-scale-out   --policy-type TargetTrackingScaling   --target-tracking-configuration '{"TargetValue": 70.0, "PredefinedMetricSpecification": {"PredefinedMetricType": "ASGAverageCPUUtilization"}}'
```

---

> [!tip]
> L'élasticité est différente de la scalabilité : scalabilité = capacité à gérer la croissance ; élasticité = capacité à s'adapter dynamiquement. Un système peut être scalable sans être élastique.
