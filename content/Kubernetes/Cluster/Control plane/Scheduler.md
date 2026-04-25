---
title: Scheduler
tags:
  - advanced
---
# Scheduler

---

## Définition

Le kube-scheduler est le composant qui décide sur quel [[Node]] placer chaque pod. Il observe les [[Pods]] non schedulés et sélectionne le node optimal selon des contraintes (ressources, affinité, taints, topologie).

---

## Comment le scheduler choisit

```
Pod non schedulé (nodeName vide)
    ↓
Filtering — éliminer les nodes inadaptés :
    - resources insuffisantes
    - taints non tolérées
    - node selectors non matchés
    - ports déjà utilisés
    ↓
Scoring — noter les nodes restants :
    - équilibrage de charge
    - affinité pod/node
    - spread topology
    ↓
Node sélectionné → binding (nodeName = node choisi)
```

---

## Influencer le scheduling

```yaml
# Node selector (simple)
spec:
  nodeSelector:
    disktype: ssd

# Resource requests (obligatoires pour le scheduling)
spec:
  containers:
  - resources:
      requests:
        memory: "256Mi"
        cpu: "500m"

# Affinity (avancé)
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values: [eu-west-1a]
```

---

> [!warning]
> Sans `requests` définis, le scheduler ne peut pas évaluer correctement la capacité des nodes. Toujours définir des requests pour les workloads de production.
