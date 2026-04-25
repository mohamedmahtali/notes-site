---
title: Taints and tolerations
tags:
  - advanced
---
# Taints and tolerations

---

## Définition

Les taints sont des marqueurs sur les [[Node]] qui repoussent les [[Pods]]. Les tolerations sont des marqueurs sur les pods qui leur permettent d'être schedulés sur des nodes avec certains taints. Ensemble, ils permettent de réserver des nodes pour des workloads spécifiques.

---

## Cas d'usage

- Réserver des nodes GPU pour les workloads ML
- Dédier des nodes aux composants système (ne pas placer d'applis)
- Isoler des nodes pour des tenants différents
- Nodes en maintenance : taint pour empêcher de nouveaux pods

---

## Taints sur les nodes

```bash
# Ajouter un taint
kubectl taint node gpu-node-1 gpu=true:NoSchedule
# NoSchedule : pods sans toleration ne seront pas schedulés
# PreferNoSchedule : éviter si possible
# NoExecute : expulse aussi les pods déjà là

# Voir les taints d'un node
kubectl describe node gpu-node-1 | grep Taint

# Supprimer un taint (suffixe -)
kubectl taint node gpu-node-1 gpu=true:NoSchedule-
```

---

## Tolerations dans les pods

```yaml
spec:
  tolerations:
  - key: "gpu"
    operator: "Equal"
    value: "true"
    effect: "NoSchedule"
  # ou
  - key: "dedicated"
    operator: "Exists"    # match n'importe quelle valeur
    effect: "NoSchedule"
  nodeSelector:
    gpu: "true"           # cibler ces nodes après avoir toléré
```

---

> [!note]
> Les taints `node-role.kubernetes.io/control-plane:NoSchedule` sont automatiquement ajoutés aux [[Control plane]] nodes pour qu'aucun pod applicatif ne s'y place. Les [[DaemonSets]] système ont des tolerations pour tout.
