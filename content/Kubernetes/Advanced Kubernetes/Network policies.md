---
title: Network policies
tags:
  - advanced
---
# Network policies

## Parent
- [[Advanced Kubernetes]]

---

## Définition

Les NetworkPolicies définissent des règles de pare-feu au niveau des pods Kubernetes. Par défaut, tous les pods peuvent communiquer entre eux. Les NetworkPolicies permettent de restreindre ce trafic (micro-segmentation).

---

## Pourquoi c'est important

> [!warning] Par défaut, tout est ouvert
> Sans NetworkPolicy, un pod compromis peut contacter n'importe quel autre pod du cluster. Les NetworkPolicies implémentent le principe du moindre privilège au niveau réseau.

---

## Bloquer tout par défaut

```yaml
# Deny-all ingress dans un namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: production
spec:
  podSelector: {}       # s'applique à tous les pods
  policyTypes:
  - Ingress
  - Egress
  # pas de règles = tout bloqué
```

---

## Autoriser le trafic spécifique

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-api
spec:
  podSelector:
    matchLabels:
      app: api-service    # s'applique aux pods api-service
  policyTypes: [Ingress]
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend   # seulement depuis frontend
    ports:
    - port: 8080
```

---

> [!warning]
> Les NetworkPolicies nécessitent un CNI qui les supporte (Calico, Cilium, Weave). Flannel ne les supporte pas. Vérifier la compatibilité avant de déployer des NetworkPolicies.
