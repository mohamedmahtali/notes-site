---
title: Autoscaling
tags:
  - intermediate
---
# Autoscaling

## Parent
- [[Cloud]]

## Enfants
- [[Horizontal scaling]]
- [[Vertical scaling]]
- [[Scaling policies]]

---

## Définition

L'autoscaling ajuste automatiquement le nombre d'instances (horizontal) ou la capacité d'une instance (vertical) en réponse à la demande. C'est la concrétisation de l'élasticité du cloud.

---

## Composants AWS Auto Scaling

```
Auto Scaling Group (ASG)
├── Launch Template — quelle instance créer
├── Min/Desired/Max capacities
├── Health checks — supprimer les instances unhealthy
└── Scaling Policies
    ├── Target Tracking — maintenir une métrique à une valeur cible
    ├── Step Scaling — augmenter/diminuer par paliers
    └── Scheduled Actions — scaling planifié
```

---

## Créer un ASG

```bash
# Launch Template
aws ec2 create-launch-template   --launch-template-name myapp-lt   --launch-template-data '{"ImageId":"ami-abc","InstanceType":"t3.medium"}'

# Auto Scaling Group
aws autoscaling create-auto-scaling-group   --auto-scaling-group-name myapp-asg   --launch-template LaunchTemplateName=myapp-lt   --min-size 2 --max-size 10 --desired-capacity 3   --vpc-zone-identifier "subnet-abc123,subnet-def456"   --target-group-arns arn:aws:elasticloadbalancing:...
```
