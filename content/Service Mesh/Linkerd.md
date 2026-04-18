---
title: Linkerd
tags: [kubernetes, networking, advanced]
---

# Linkerd

## Définition

Linkerd est un service mesh open-source léger pour Kubernetes, développé par Buoyant. Son proxy sidecar est écrit en Rust (ultra-performant, faible empreinte mémoire) et son installation est volontairement minimaliste — mTLS et observabilité fonctionnent out-of-the-box sans configuration.

> [!tip] Linkerd vs Istio
> Linkerd est l'option "simplicité d'abord" : installation en 5 minutes, mTLS automatique sur tous les services, overhead minimal (~2ms vs ~10ms pour Istio). Istio offre plus de fonctionnalités (WASM, ext-authz, traffic mirroring fin), mais au prix d'une complexité bien supérieure.

## Installation

```bash
# Installer linkerd CLI
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh
export PATH=$PATH:$HOME/.linkerd2/bin

# Vérifier les prérequis du cluster
linkerd check --pre

# Installer le control plane
linkerd install --crds | kubectl apply -f -
linkerd install | kubectl apply -f -

# Vérifier l'installation
linkerd check

# Installer le dashboard (optionnel)
linkerd viz install | kubectl apply -f -
linkerd viz check
```

## Injecter les sidecars

```bash
# Annoter un namespace pour injection automatique
kubectl annotate namespace production linkerd.io/inject=enabled

# Injecter manuellement sur un manifest existant
kubectl get deploy -n production -o yaml | linkerd inject - | kubectl apply -f -

# Vérifier l'injection
linkerd check --proxy -n production
```

## mTLS automatique

Contrairement à Istio, Linkerd active mTLS par défaut sur toutes les connexions entre pods injectés — aucune configuration requise.

```bash
# Vérifier que mTLS est actif entre deux services
linkerd viz edges deployment -n production

# Voir les connexions en temps réel
linkerd viz tap deployment/frontend -n production

# Statistiques de trafic
linkerd viz stat deployment -n production
```

## Observabilité intégrée

```bash
# Dashboard web
linkerd viz dashboard &

# Métriques en CLI (success rate, RPS, latence p99)
linkerd viz routes deployment/frontend -n production

# Top des routes les plus lentes
linkerd viz top deployment/frontend -n production
```

```
Exemple de sortie `linkerd viz stat` :
NAME          MESHED   SUCCESS       RPS   LATENCY_P50   LATENCY_P99
frontend         3/3   99.80%   45.2rps           2ms          18ms
payment-svc      2/2   98.50%   12.1rps           5ms          45ms
```

## Retry et timeout avec HTTPRoute

```yaml
# Linkerd utilise les Gateway API HTTPRoute standards
apiVersion: policy.linkerd.io/v1beta3
kind: HTTPRoute
metadata:
  name: payment-route
  namespace: production
spec:
  parentRefs:
  - name: payment-service
    kind: Service
    group: core
    port: 8080
  rules:
  - backendRefs:
    - name: payment-service
      port: 8080
    timeouts:
      request: 5s
      backendRequest: 3s
```

## Liens

- [[Service Mesh]]
- [[mTLS]]
- [[Traffic management]]
- [[Istio]]
