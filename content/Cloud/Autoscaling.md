---
title: Autoscaling
tags:
  - intermediate
---
# Autoscaling

---

## Définition

L'autoscaling ajuste automatiquement le nombre d'instances (horizontal) ou la capacité d'une instance (vertical) en réponse à la demande. C'est la concrétisation de l'élasticité du [[Cloud]].

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
aws ec2 create-launch-template \
  --launch-template-name myapp-lt \
  --launch-template-data '{
    "ImageId": "ami-abc123",
    "InstanceType": "t3.medium",
    "SecurityGroupIds": ["sg-abc123"],
    "UserData": "'$(base64 -w0 startup.sh)'"
  }'

# Auto Scaling Group multi-AZ
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name myapp-asg \
  --launch-template LaunchTemplateName=myapp-lt,Version='$Latest' \
  --min-size 2 --max-size 10 --desired-capacity 3 \
  --vpc-zone-identifier "subnet-abc123,subnet-def456" \
  --target-group-arns arn:aws:elasticloadbalancing:... \
  --health-check-type ELB \
  --health-check-grace-period 60
```

## Lifecycle hooks — actions au scale out/in

```bash
# Hook au scale-in : attendre 5 min avant de terminer l'instance
# (pour drainer les connexions, sauvegarder l'état...)
aws autoscaling put-lifecycle-hook \
  --auto-scaling-group-name myapp-asg \
  --lifecycle-hook-name scale-in-hook \
  --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING \
  --default-result CONTINUE \
  --heartbeat-timeout 300

# Signaler que l'instance est prête (depuis le script de l'instance)
aws autoscaling complete-lifecycle-action \
  --lifecycle-hook-name scale-in-hook \
  --auto-scaling-group-name myapp-asg \
  --lifecycle-action-result CONTINUE \
  --instance-id $INSTANCE_ID
```

## Warm pools — réduire la latence de scale-out

```bash
# Garder 2 instances "chaudes" (arrêtées mais prêtes à démarrer)
aws autoscaling put-warm-pool \
  --auto-scaling-group-name myapp-asg \
  --min-size 2 \
  --pool-state Stopped
```

> [!tip] Scale-in protection
> Protéger une instance spécifique de la terminaison pendant un traitement critique : `aws autoscaling set-instance-protection --instance-ids i-abc --auto-scaling-group-name myapp-asg --protected-from-scale-in`
