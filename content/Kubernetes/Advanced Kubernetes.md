---
title: Advanced Kubernetes
tags:
  - advanced
---
# Advanced Kubernetes

## Définition

Les fonctionnalités avancées de [[Kubernetes]] permettent de contrôler finement le placement des [[Pods]], l'isolation réseau, la disponibilité lors des maintenances, et la validation des ressources à la création.

## Vue d'ensemble

| Fonctionnalité | Objectif |
|---|---|
| [[Taints and tolerations]] | Réserver des [[Node]] pour certains workloads |
| [[Affinity and anti-affinity]] | Colocaliser ou séparer les pods |
| [[Network policies]] | Micro-segmentation réseau |
| [[Pod disruption budgets]] | Garantir la disponibilité lors des maintenances |
| [[Admission controllers]] | Valider/muter les ressources à la création |

## Quand utiliser quoi

```
"Ce node est réservé aux GPU"                        → Taint + Toleration
"Ces 3 pods doivent être sur des nodes différents"   → Anti-affinity
"Ce service ne peut pas parler à cet autre"          → NetworkPolicy
"Jamais moins de 2 pods lors d'une mise à jour"      → PodDisruptionBudget
"Toutes les images doivent venir de notre registry"  → AdmissionController
```

## Taints & Tolerations

Un taint sur un node empêche les pods de s'y scheduler — sauf ceux qui ont la toleration correspondante.

```bash
# Réserver un node pour les workloads GPU
kubectl taint nodes gpu-node-1 dedicated=gpu:NoSchedule

# Voir les taints d'un node
kubectl describe node gpu-node-1 | grep Taint
```

```yaml
# Pod qui tolère ce taint (peut être schedulé sur gpu-node-1)
spec:
  tolerations:
    - key: "dedicated"
      operator: "Equal"
      value: "gpu"
      effect: "NoSchedule"
  containers:
    - name: ml-job
      resources:
        limits:
          nvidia.com/gpu: 1
```

Effets disponibles : `NoSchedule` (bloque le scheduling), `PreferNoSchedule` (évite si possible), `NoExecute` (expulse les pods existants).

## Affinity & Anti-affinity

```yaml
spec:
  affinity:
    # Forcer la séparation des replicas (haute dispo)
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              app: frontend
          topologyKey: kubernetes.io/hostname   # 1 pod max par node

    # Coloquer avec la BDD (latence réseau)
    podAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 100
          podAffinityTerm:
            labelSelector:
              matchLabels:
                app: postgres
            topologyKey: kubernetes.io/hostname
```

`required` = dur (pod non schedulé si impossible), `preferred` = souple (best effort).

## Network Policies

Par défaut, tous les pods d'un cluster peuvent se parler. Les NetworkPolicies ajoutent de la micro-segmentation.

```yaml
# Isoler le namespace : seul le frontend peut appeler le backend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-only
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

> [!warning] Prérequis CNI
> Les NetworkPolicies nécessitent un CNI qui les supporte : Calico, Cilium, Weave. Flannel seul ne les applique pas.

## Pod Disruption Budgets

Garantit qu'un nombre minimum de pods reste disponible lors d'opérations de maintenance (drain de node, rolling update).

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: frontend-pdb
spec:
  minAvailable: 2        # ou maxUnavailable: 1
  selector:
    matchLabels:
      app: frontend
```

```bash
# Drain un node (respecte les PDBs)
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data

# Si le PDB bloque, vérifier
kubectl get pdb
kubectl describe pdb frontend-pdb
```

## Admission Controllers

Webhooks qui interceptent les appels API avant création/modification des ressources.

```
kubectl apply → API Server → Admission Controllers → etcd
                                    │
                          MutatingAdmissionWebhook   (modifie la ressource)
                          ValidatingAdmissionWebhook (accepte ou rejette)
```

Exemples courants :
- **OPA/Gatekeeper** — politiques custom (ex : images depuis registry interne uniquement)
- **Kyverno** — politiques en YAML (plus simple qu'OPA)
- **PodSecurity** — remplaçant de PodSecurityPolicy (intégré depuis K8s 1.25)

```yaml
# Kyverno : forcer le tag d'image (pas de "latest")
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: disallow-latest-tag
spec:
  rules:
    - name: require-image-tag
      match:
        resources:
          kinds: [Pod]
      validate:
        message: "L'image doit avoir un tag explicite, pas 'latest'"
        pattern:
          spec:
            containers:
              - image: "!*:latest"
```

## Explorer

- **[[Taints and tolerations]]** — réservation de nodes, effets NoSchedule/NoExecute
- **[[Affinity and anti-affinity]]** — placement conditionnel, topologyKey
- **[[Network policies]]** — isolation par namespace, ingress/egress rules
- **[[Pod disruption budgets]]** — disponibilité lors des drains et rolling updates
- **[[Admission controllers]]** — OPA, Kyverno, webhooks de validation
