---
title: Circuit breaker
tags: [reliability, networking, advanced]
---

# Circuit breaker

## Définition

Le circuit breaker est un pattern de résilience qui coupe automatiquement les appels vers un service défaillant. Quand un service commence à répondre lentement ou avec des erreurs, le circuit breaker "s'ouvre" et retourne immédiatement une erreur sans attendre le timeout — protégeant ainsi tout le système d'une cascade de défaillances.

> [!tip] Analogie électrique
> Comme un disjoncteur électrique : si un appareil consomme trop (= service lent/en erreur), il coupe le circuit avant que l'incendie ne se propage.

## États du circuit breaker

```
          ┌─────────────────────────────────────────────────┐
          │                                                   │
       CLOSED ──── trop d'erreurs ────→ OPEN                 │
       (normal)                        (rejette tout)         │
          ↑                              │                    │
          │                              │ timeout écoulé     │
          │                              ↓                    │
          └──── succès ────────── HALF-OPEN                   │
                                  (teste 1 requête)           │
          └─────────────────────────────────────────────────┘
```

| État | Comportement |
|------|-------------|
| **CLOSED** | Trafic normal, erreurs comptabilisées |
| **OPEN** | Toutes les requêtes échouent immédiatement (fail fast) |
| **HALF-OPEN** | Une requête de test passe — succès → CLOSED, échec → OPEN |

## Configuration Istio (DestinationRule)

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: payment-service-cb
  namespace: production
spec:
  host: payment-service
  trafficPolicy:
    outlierDetection:
      # Circuit breaker basé sur les erreurs consécutives
      consecutive5xxErrors: 5       # 5 erreurs 5xx consécutives
      interval: 30s                  # Fenêtre d'analyse
      baseEjectionTime: 30s          # Durée d'éjection du pool
      maxEjectionPercent: 50         # Max 50% des instances éjectées
    connectionPool:
      http:
        http1MaxPendingRequests: 100  # File d'attente max
        http2MaxRequests: 1000
      tcp:
        maxConnections: 100
        connectTimeout: 3s
```

## Retry et timeout associés

```yaml
# VirtualService — retry + timeout complémentaires au circuit breaker
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: payment-service
spec:
  hosts:
  - payment-service
  http:
  - timeout: 5s
    retries:
      attempts: 3
      perTryTimeout: 2s
      retryOn: "5xx,reset,connect-failure"
    route:
    - destination:
        host: payment-service
```

## Tester le circuit breaker

```bash
# Fortio — outil de test de charge et de résilience
kubectl run fortio --image=fortio/fortio -- load \
  -c 3 -qps 0 -n 30 \
  http://payment-service:8080/api/pay

# Voir les métriques Envoy (connexions rejetées)
kubectl exec -it payment-pod -c istio-proxy -- \
  pilot-agent request GET stats | grep upstream_rq_pending_overflow
```

> [!note] Circuit breaker vs Retry
> Les deux sont complémentaires mais distincts. Le **retry** réessaie une requête échouée (utile pour les erreurs transitoires). Le **circuit breaker** arrête d'essayer quand un service est manifestement défaillant. Utiliser les deux ensemble.

## Liens

- [[Service Mesh]]
- [[Istio]]
- [[Traffic management]]
