---
title: Horizontal scaling
tags:
  - beginner
---
# Horizontal scaling

---

## Définition

Le scaling horizontal (scale out/in) ajoute ou retire des instances identiques pour gérer la charge. C'est la forme d'[[Autoscaling]] la plus courante en [[Cloud]] car elle permet une disponibilité continue sans interruption.

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

## Kubernetes — HPA (Horizontal Pod Autoscaler)

```yaml
# Scale entre 2 et 20 pods selon CPU + RPS custom metric
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp
  namespace: production
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
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60    # Attendre 60s avant de re-scaler UP
      policies:
      - type: Pods
        value: 4                          # Ajouter max 4 pods à la fois
        periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300   # Attendre 5min avant de scale DOWN
```

```bash
# Voir l'état du HPA en temps réel
kubectl get hpa myapp -w

# Déclencher manuellement pour tester
kubectl scale deployment myapp --replicas=5
```

## KEDA — scaling sur métriques externes

KEDA ([[Kubernetes]] Event Driven Autoscaler) permet de scaler sur des sources externes : longueur d'une queue SQS, nombre de messages Kafka, requêtes en attente...

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: worker-scaler
spec:
  scaleTargetRef:
    name: message-worker
  minReplicaCount: 0          # Scale to zero quand queue vide
  maxReplicaCount: 50
  triggers:
  - type: aws-sqs-queue
    metadata:
      queueURL: https://sqs.eu-west-1.amazonaws.com/123456/my-queue
      queueLength: "10"       # 1 pod par tranche de 10 messages
      awsRegion: eu-west-1
```

## Avantages vs Vertical

| Aspect | Horizontal | Vertical |
|---|---|---|
| Disponibilité | Pas d'interruption | Redémarrage requis |
| Scalabilité | Quasi-illimitée | Limité par les [[Types]] d'instance |
| Coût | Linéaire | Non-linéaire |
| Complexité app | Doit être stateless | Peut être stateful |
