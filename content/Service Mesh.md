---
title: Service Mesh
tags:
  - kubernetes
  - networking
  - advanced
---

# Service Mesh

## Définition

Un service mesh est une couche d'infrastructure dédiée à la gestion de la communication entre microservices. Il prend en charge le chiffrement (mTLS), l'observabilité, le routage avancé et la résilience — sans modifier le code applicatif.

> [!tip] Pourquoi c'est important
> En microservices, chaque service communique avec des dizaines d'autres. Sans service mesh, chaque équipe doit implémenter retry, timeout, circuit breaker, [[TLS]] dans son propre code. Le service mesh externalise tout ça dans un proxy sidecar transparent.

## Architecture : le pattern sidecar

```
Pod A                              Pod B
┌─────────────────────┐            ┌─────────────────────┐
│  App container      │            │  App container      │
│  (localhost:8080)   │            │  (localhost:8080)   │
│         ↕           │            │         ↕           │
│  Envoy proxy        │───mTLS────►│  Envoy proxy        │
│  (sidecar)          │            │  (sidecar)          │
└─────────────────────┘            └─────────────────────┘
          ↑                                  ↑
          └─────────── Control Plane ────────┘
                    (Istio / Linkerd)
```

Le sidecar intercepte tout le trafic entrant et sortant du pod. L'application ne sait pas qu'il existe.

## Fonctionnalités clés

| Fonctionnalité | Description |
|---------------|-------------|
| **[[mTLS]]** | Chiffrement et authentification mutuelle entre tous les [[Services]] |
| **[[Traffic management]]** | Canary [[Releases]], A/B testing, traffic splitting, retries |
| **[[Circuit breaker]]** | Coupure automatique si un service répond trop lentement |
| **Observabilité** | Métriques, traces distribuées et logs automatiques sans code |
| **Fault injection** | Simuler des erreurs et latences pour tester la résilience |

## Istio vs Linkerd

| Critère | [[Istio]] | [[Linkerd]] |
|---------|-----------|-------------|
| Proxy | Envoy (puissant, complexe) | Linkerd2-proxy (léger, Rust) |
| Complexité | Élevée | Faible |
| Fonctionnalités | Complètes (WASM, ext-authz...) | Essentielles bien faites |
| Performance | Overhead ~5-10ms | Overhead ~1-2ms |
| Cas d'usage | Gros [[Cluster]], besoins avancés | Simplicité et performance |

> [!note] Choisir son service mesh
> Pour commencer : **Linkerd** (moins de configuration, mTLS automatique out-of-the-box). Pour des besoins avancés (traffic [[Policies]] complexes, ext-authz, WASM) : **Istio**.

## Prérequis

Avant Service Mesh, maîtriser : [[Kubernetes]] (pods, namespaces, sidecars), [[Networking]] (TLS, DNS, load balancing), [[Security]] (certificats, mTLS).

## Explorer Service Mesh

### Concepts clés
- **[[mTLS]]** — authentification mutuelle, chiffrement automatique entre services
- **[[Traffic management]]** — canary releases, A/B testing, traffic splitting
- **[[Circuit breaker]]** — coupure automatique sur service défaillant

### Implémentations
- **[[Istio]]** — control plane complet, VirtualService, DestinationRule, Gateway
- **[[Linkerd]]** — léger, Rust, mTLS out-of-the-box, moins de configuration
