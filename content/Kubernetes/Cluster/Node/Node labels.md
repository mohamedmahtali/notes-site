---
title: Node labels
tags:
  - intermediate
---
# Node labels

---

## Définition

Les [[Node]] labels sont des paires clé-valeur attachées aux nodes [[Kubernetes]]. Ils permettent de cibler des nodes spécifiques pour le scheduling (nodeSelector, nodeAffinity) et sont utilisés par le [[Scheduler]] pour placer les [[Pods]].

---

## Labels standards

```bash
# Labels automatiquement ajoutés par Kubernetes/cloud provider
kubernetes.io/hostname=worker-1
kubernetes.io/os=linux
kubernetes.io/arch=amd64
topology.kubernetes.io/zone=eu-west-1a
topology.kubernetes.io/region=eu-west-1
node.kubernetes.io/instance-type=t3.medium
```

---

## Gérer les labels

```bash
# Ajouter un label
kubectl label node worker-1 disktype=ssd

# Modifier un label
kubectl label node worker-1 env=production --overwrite

# Supprimer un label
kubectl label node worker-1 disktype-

# Voir les labels d'un node
kubectl get node worker-1 --show-labels
kubectl describe node worker-1 | grep Labels -A 10
```

---

## Utiliser dans un pod

```yaml
# nodeSelector — simple
spec:
  nodeSelector:
    disktype: ssd
    env: production

# Node Affinity — plus expressif
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values: [ssd, nvme]
```

---

> [!tip]
> Utiliser les labels de zone (`topology.kubernetes.io/zone`) pour configurer la répartition des pods entre zones via `topologySpreadConstraints` — essentiel pour la haute disponibilité.
