---
title: Kubernetes
tags:
  - kubernetes
  - intermediate
---

# Kubernetes

## Prérequis

Avant Kubernetes, maîtriser : [[Docker]] (conteneurs, images, registres), [[Linux]] (processus, réseau), [[Networking]] (DNS, load balancing, TCP/IP).

---

## Définition

Kubernetes (K8s) est un orchestrateur de conteneurs open-source créé par Google. Il automatise le déploiement, la mise à l'échelle et la gestion des applications conteneurisées sur un cluster de machines.

> [!tip] Pourquoi c'est important
> Gérer des dizaines de conteneurs manuellement est impossible en production. Kubernetes automatise tout : redémarrage des conteneurs crashés, scaling selon la charge, [[Rolling updates]] sans downtime, routage du trafic, gestion des secrets. C'est devenu le standard de facto de l'orchestration en production.

## Architecture

```
Control Plane                    Worker Nodes
┌────────────────────┐           ┌─────────────────────┐
│ API Server          │ ←──────→ │ kubelet             │
│ Scheduler           │           │ kube-proxy          │
│ Controller Manager  │           │ Container runtime   │
│ etcd               │           │                     │
└────────────────────┘           └─────────────────────┘
```

- Le **[[Control plane]]** décide de l'état désiré du cluster
- Les **Worker [[Node]]** exécutent les workloads (pods)

## Objets fondamentaux

| Objet | Rôle |
|-------|------|
| [[Pods]] | Unité de base — 1 ou plusieurs conteneurs |
| [[Services]] | Exposition réseau stable des pods |
| [[ConfigMaps]] | Configuration non-sensible |
| [[Secrets]] | Données sensibles chiffrées |
| [[Volumes]] | Persistance des données |
| [[Namespaces]] | Isolation logique du cluster |

## Gestion & opérations

- **[[kubectl]]** — CLI pour interagir avec le cluster
- **[[Helm]]** — Gestionnaire de [[Package]] Kubernetes
- **[[RBAC]]** — Contrôle d'accès basé sur les rôles
- **[[HPA]]** — [[Autoscaling]] horizontal des pods
- **[[Operators]]** — Extensions Kubernetes pour apps stateful

## Workloads

- **[[Deployments]]** → apps stateless (web, API)
- **[[StatefulSets]]** → apps stateful (bases de données)
- **[[DaemonSets]]** → un pod par node ([[Monitoring]], [[Logging]])
- **Jobs / CronJobs** → tâches ponctuelles ou planifiées

## Explorer Kubernetes

### Le cluster
- **[[Cluster]]** — architecture générale, composants
- **[[Control plane]]** — API server, scheduler, etcd, controller manager
- **[[Node]]** — kubelet, kube-proxy, container runtime

### Workloads
- **[[Pods]]** — unité de base, multi-conteneurs, lifecycle
- **[[Deployments]]** — apps stateless, rolling updates, rollback
- **[[StatefulSets]]** — apps stateful (bases de données, caches)
- **[[DaemonSets]]** — un pod par node (monitoring, logging)

### Réseau & Exposition
- **[[Services]]** — ClusterIP, NodePort, LoadBalancer
- **[[Ingress]]** — reverse proxy HTTP/HTTPS, TLS termination
- **[[Namespaces]]** — isolation logique, quotas

### Configuration & Stockage
- **[[ConfigMaps]]** — configuration non-sensible injectée dans les pods
- **[[Secrets]]** — données sensibles chiffrées
- **[[Volumes]]** — stockage persistant (PVC, PV, StorageClass)

### Opérations & Avancé
- **[[kubectl]]** — CLI : get, describe, apply, exec, logs, port-forward
- **[[Helm]]** — package manager, charts, releases
- **[[RBAC]]** — contrôle d'accès, roles, bindings
- **[[HPA]]** — autoscaling horizontal basé sur les métriques
- **[[Operators]]** — extensions pour applications stateful complexes
- **[[Advanced Kubernetes]]** — admission controllers, affinity, taints

> [!tip] Lab pratique
> → [[Lab Kubernetes — App avec HPA et Ingress]]

> [!note] Connexions
> → [[Docker → Kubernetes]] — images Docker comme unité de déploiement K8s
> → [[Kubernetes + Observability]] — surveiller et alerter sur le cluster
