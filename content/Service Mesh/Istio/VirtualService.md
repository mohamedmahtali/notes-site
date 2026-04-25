---
title: VirtualService
tags:
  - kubernetes
  - networking
  - advanced
---

# VirtualService

## Définition

Un `VirtualService` Istio définit les **règles de routage** du trafic vers un service. Il remplace le routage basique de [[Kubernetes]] (round-robin sur les [[Pods]]) par un routage fin basé sur les headers, le poids, le chemin, etc.

> [!note] VirtualService ≠ Service K8s
> Le VirtualService est une couche au-dessus du Service Kubernetes. Il dit "comment router le trafic" ; le Service dit "où aller". Les deux coexistent.

## Structure

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-service
  namespace: production
spec:
  hosts:
  - my-service          # Service K8s cible (ou nom externe)
  gateways:             # Optionnel : si le trafic vient d'une Gateway
  - my-gateway
  http:
  - match:              # Conditions de match (optionnel)
    - uri:
        prefix: /api/v2
    route:
    - destination:
        host: my-service
        subset: v2
        port:
          number: 8080
  - route:              # Route par défaut
    - destination:
        host: my-service
        subset: v1
```

## Retries et timeouts

```yaml
http:
- timeout: 10s
  retries:
    attempts: 3
    perTryTimeout: 3s
    retryOn: "5xx,reset,connect-failure,retriable-4xx"
  route:
  - destination:
      host: my-service
```

## Fault injection

```yaml
http:
- fault:
    delay:
      percentage:
        value: 5.0
      fixedDelay: 2s
    abort:
      percentage:
        value: 1.0
      httpStatus: 503
  route:
  - destination:
      host: my-service
```

## Redirect et rewrite

```yaml
http:
# Redirect HTTP → HTTPS
- match:
  - port: 80
  redirect:
    uri: /
    scheme: https
    redirectCode: 301

# Rewrite le chemin avant de forwarder
- match:
  - uri:
      prefix: /v1
  rewrite:
    uri: /api
  route:
  - destination:
      host: legacy-service
```

## Liens

- [[Istio]]
- [[DestinationRule]]
- [[Gateway]]
- [[Traffic management]]
