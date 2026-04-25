---
title: DestinationRule
tags:
  - kubernetes
  - networking
  - advanced
---

# DestinationRule

## Définition

Une `DestinationRule` définit les **politiques appliquées côté destination** : comment se connecter au service ([[TLS]], [[Load balancing]]), quelles versions existent (subsets), et les limites de connexion (circuit breaker).

> [!note] VirtualService + DestinationRule = tandem
> Le VirtualService dit "où envoyer le trafic". La DestinationRule dit "comment se comporter une fois arrivé". Ils fonctionnent toujours en pair.

## Subsets (versions)

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: frontend
  namespace: production
spec:
  host: frontend
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
  - name: canary
    labels:
      version: v3
      track: canary
```

## Load balancing

```yaml
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      simple: LEAST_CONN    # ROUND_ROBIN | LEAST_CONN | RANDOM | PASSTHROUGH
```

## Circuit breaker (outlier detection)

```yaml
spec:
  host: my-service
  trafficPolicy:
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 10s
      baseEjectionTime: 30s
      maxEjectionPercent: 100
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 50
        http2MaxRequests: 200
        idleTimeout: 90s
```

## TLS vers le backend

```yaml
spec:
  host: external-db.example.com
  trafficPolicy:
    tls:
      mode: MUTUAL           # DISABLE | SIMPLE | MUTUAL | ISTIO_MUTUAL
      clientCertificate: /etc/certs/client.pem
      privateKey: /etc/certs/key.pem
      caCertificates: /etc/certs/rootcacerts.pem
```

## Policy par subset

```yaml
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN    # Policy par défaut
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
    trafficPolicy:            # Override pour v2 uniquement
      loadBalancer:
        simple: LEAST_CONN
```

## Liens

- [[Istio]]
- [[VirtualService]]
- [[Circuit breaker]]
- [[Traffic management]]
