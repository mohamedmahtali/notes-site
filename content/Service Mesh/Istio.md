---
title: Istio
tags:
  - kubernetes
  - networking
  - advanced
---

# Istio

## Définition

Istio est le service mesh open-source le plus utilisé en production. Il s'appuie sur **Envoy** comme sidecar proxy et [[EXPOSE]] ses propres [[CRD]] [[Kubernetes]] pour configurer le routage, la sécurité et l'observabilité des microservices.

> [!tip] Istio = [[Control plane]] + Envoy sidecars
> Istio ne touche pas ton code. Il injecte automatiquement un conteneur Envoy dans chaque pod (si le namespace est annoté), et expose des ressources Kubernetes (VirtualService, DestinationRule...) pour tout configurer.

## Installation

```bash
# Télécharger istioctl
curl -L https://istio.io/downloadIstio | sh -
export PATH=$PWD/bin:$PATH

# Installer Istio sur le cluster (profil production)
istioctl install --set profile=production -y

# Vérifier l'installation
istioctl verify-install
kubectl get pods -n istio-system
```

## Activer l'injection automatique des sidecars

```bash
# Annoter le namespace pour injection automatique
kubectl label namespace production istio-injection=enabled

# Vérifier qu'un pod a bien son sidecar
kubectl get pod payment-xxx -o jsonpath='{.spec.containers[*].name}'
# → payment-service istio-proxy
```

## Ressources Istio essentielles

| Ressource | Rôle |
|-----------|------|
| **[[VirtualService]]** | Règles de routage (canary, retries, timeouts, fault injection) |
| **[[DestinationRule]]** | Politique côté destination (circuit breaker, [[TLS]], subsets) |
| **[[Gateway]]** | Point d'entrée du trafic externe vers le mesh |
| **PeerAuthentication** | Politique mTLS par namespace |
| **AuthorizationPolicy** | Contrôle d'accès entre [[Services]] |

## Observabilité automatique

Istio collecte automatiquement métriques, traces et logs de tout le trafic mesh.

```bash
# Démarrer les dashboards intégrés
istioctl dashboard grafana    # Métriques mesh
istioctl dashboard kiali      # Visualisation du mesh et des flows
istioctl dashboard jaeger     # Traces distribuées
istioctl dashboard prometheus # Métriques brutes
```

```bash
# Inspecter le trafic en temps réel
istioctl proxy-status                          # État de sync de tous les proxies
istioctl analyze -n production                  # Détecter les misconfigurations
istioctl x describe pod payment-xxx            # Config appliquée sur un pod
```

## Commandes de debug

```bash
# Voir les logs du proxy sidecar
kubectl logs payment-xxx -c istio-proxy

# Voir la config Envoy d'un pod
istioctl proxy-config clusters payment-xxx
istioctl proxy-config routes payment-xxx
istioctl proxy-config listeners payment-xxx

# Voir les certificats mTLS d'un pod
istioctl proxy-config secret payment-xxx
```

## Liens

- [[Service Mesh]]
- [[VirtualService]]
- [[DestinationRule]]
- [[Gateway]]
- [[mTLS]]
- [[Traffic management]]
- [[Circuit breaker]]
