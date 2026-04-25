---
title: Custom metrics
tags:
  - advanced
---
# Custom metrics

---

## Définition

Le [[HPA]] peut scaler sur des métriques custom applicatives (requêtes par seconde, longueur de queue, latence) via l'API Custom [[Metrics]] ou External Metrics. Nécessite un adapter ([[Prometheus]] Adapter, KEDA).

---

## Architecture

```
Application → expose métriques → Prometheus
                                      ↓
                          Prometheus Adapter
                                      ↓
                          Custom Metrics API
                                      ↓
                                    HPA
```

---

## HPA avec KEDA (Kubernetes Event-Driven Autoscaling)

KEDA est plus simple à configurer que le Prometheus Adapter :

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: myapp-scaledobject
spec:
  scaleTargetRef:
    name: myapp
  minReplicaCount: 1
  maxReplicaCount: 50
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prometheus:9090
      metricName: http_requests_per_second
      query: sum(rate(http_requests_total{app="myapp"}[2m]))
      threshold: "100"    # scale si > 100 req/s par pod
  - type: rabbitmq
    metadata:
      queueName: tasks
      queueLength: "50"   # scale si queue > 50 messages par pod
```

---

> [!tip]
> KEDA peut même scaler jusqu'à 0 réplicas (scale-to-zero) — idéal pour les workloads event-driven intermittents. L'application est démarrée uniquement quand il y a des messages/requêtes.
