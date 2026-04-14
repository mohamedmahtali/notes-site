---
title: Scaling policies
tags:
  - intermediate
---
# Scaling policies

## Parent
- [[Autoscaling]]

---

## Définition

Les scaling policies définissent quand et comment l'autoscaling doit ajouter ou retirer des instances. Trois types principaux : Target Tracking (le plus simple), Step Scaling, et Scheduled Actions.

---

## Target Tracking

```bash
# Maintenir la métrique à la valeur cible
# Exemple : CPU à 70%, ALB requests à 1000/cible
aws autoscaling put-scaling-policy   --policy-type TargetTrackingScaling   --target-tracking-configuration '{
    "TargetValue": 1000.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ALBRequestCountPerTarget",
      "ResourceLabel": "app/my-alb/abc/targetgroup/my-tg/def"
    }
  }'
```

---

## Step Scaling

```bash
# Échelle par paliers basée sur des alarmes CloudWatch
# +2 instances si CPU > 80%, +4 si CPU > 90%
aws autoscaling put-scaling-policy   --policy-type StepScaling   --adjustment-type ChangeInCapacity   --step-adjustments '[
    {"MetricIntervalLowerBound": 0, "MetricIntervalUpperBound": 10, "ScalingAdjustment": 2},
    {"MetricIntervalLowerBound": 10, "ScalingAdjustment": 4}
  ]'
```

---

## Scheduled Actions

```bash
# Scale up avant le pic quotidien
aws autoscaling put-scheduled-update-group-action   --auto-scaling-group-name myapp-asg   --scheduled-action-name morning-scale-up   --recurrence "0 8 * * MON-FRI"   --desired-capacity 10 --min-size 5

# Scale down le soir
aws autoscaling put-scheduled-update-group-action   --auto-scaling-group-name myapp-asg   --scheduled-action-name evening-scale-down   --recurrence "0 20 * * MON-FRI"   --desired-capacity 3 --min-size 2
```

---

> [!tip]
> Combiner Scheduled Actions (pour les pics prévisibles) + Target Tracking (pour les variations imprévues). Le Scheduled Action pré-chauffe le pool, le Target Tracking gère les variations.
