---
title: Affinity and anti-affinity
tags:
  - advanced
---
# Affinity and anti-affinity

---

## Définition

L'affinity permet de [[Scheduler]] des [[Pods]] proches d'autres pods ou sur des [[Node]] spécifiques. L'anti-affinity fait l'inverse : garantit que certains pods sont sur des nodes ou zones différents pour la haute disponibilité.

---

## Node Affinity

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:  # hard
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values: [eu-west-1a, eu-west-1b]
      preferredDuringSchedulingIgnoredDuringExecution:  # soft
      - weight: 1
        preference:
          matchExpressions:
          - key: disktype
            operator: In
            values: [ssd]
```

---

## Pod Anti-affinity (haute disponibilité)

```yaml
# Garantir que les replicas d'un même Deployment
# ne sont jamais sur le même node
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values: [myapp]
        topologyKey: kubernetes.io/hostname   # un pod par node

# Préférer des zones différentes (soft)
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchLabels:
              app: myapp
          topologyKey: topology.kubernetes.io/zone
```

---

> [!tip]
> Pour la HA en production : anti-affinity [[hard]] sur `kubernetes.io/hostname` (jamais 2 pods sur le même node) + [[soft]] sur `topology.kubernetes.io/zone` (préférer des zones différentes).
