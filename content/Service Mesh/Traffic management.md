---
title: Traffic management
tags:
  - kubernetes
  - networking
  - advanced
---

# Traffic management

## Définition

Le traffic management dans un service mesh permet de contrôler précisément comment les requêtes sont routées entre les [[Services]] : canary [[Deployments]], A/B testing, traffic mirroring, fault injection — sans modifier le code ou les Deployments.

## Canary deployment avec Istio

Envoyer 10% du trafic vers la nouvelle version, 90% vers la version stable.

```yaml
# 1. Deux Deployments K8s : v1 et v2
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: frontend
      version: v1
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-v2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
      version: v2
```

```yaml
# 2. DestinationRule — définit les subsets par version
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: frontend
spec:
  host: frontend
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

```yaml
# 3. VirtualService — 90% v1, 10% v2
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: frontend
spec:
  hosts:
  - frontend
  http:
  - route:
    - destination:
        host: frontend
        subset: v1
      weight: 90
    - destination:
        host: frontend
        subset: v2
      weight: 10
```

## Routage par header (A/B testing)

```yaml
# Envoyer vers v2 uniquement les requêtes avec X-Canary: true
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: frontend
spec:
  hosts:
  - frontend
  http:
  - match:
    - headers:
        x-canary:
          exact: "true"
    route:
    - destination:
        host: frontend
        subset: v2
  - route:
    - destination:
        host: frontend
        subset: v1
```

## Traffic mirroring (shadow testing)

Dupliquer le trafic de production vers la nouvelle version sans impact utilisateur.

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: payment-service
spec:
  hosts:
  - payment-service
  http:
  - route:
    - destination:
        host: payment-service
        subset: v1
      weight: 100
    mirror:
      host: payment-service
      subset: v2
    mirrorPercentage:
      value: 100.0  # Copier 100% du trafic vers v2
```

> [!note] Mirror = trafic fantôme
> Les réponses du miroir sont ignorées. Permet de tester v2 sur du vrai trafic sans risque pour les utilisateurs.

## Fault injection (tests de résilience)

```yaml
# Injecter 5% d'erreurs 500 et 10% de délai sur le service
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: payment-service
spec:
  hosts:
  - payment-service
  http:
  - fault:
      abort:
        percentage:
          value: 5.0
        httpStatus: 500
      delay:
        percentage:
          value: 10.0
        fixedDelay: 3s
    route:
    - destination:
        host: payment-service
```

## Liens

- [[Service Mesh]]
- [[Istio]]
- [[Circuit breaker]]
- [[Kubernetes]]
