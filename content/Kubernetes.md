---
title: Kubernetes
tags: [kubernetes, intermediate]
---

# Kubernetes

## Définition

Kubernetes (K8s) est un orchestrateur de conteneurs open-source créé par Google. Il automatise le déploiement, la mise à l'échelle et la gestion des applications conteneurisées sur un cluster de machines.

> [!tip] Pourquoi c'est important
> Gérer des dizaines de conteneurs manuellement est impossible en production. Kubernetes automatise tout : redémarrage des conteneurs crashés, scaling selon la charge, rolling updates sans downtime, routage du trafic, gestion des secrets. C'est devenu le standard de facto de l'orchestration en production.

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
- Les **Worker nodes** exécutent les workloads (pods)

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
- **[[Helm]]** — Gestionnaire de packages Kubernetes
- **[[RBAC]]** — Contrôle d'accès basé sur les rôles
- **[[HPA]]** — Autoscaling horizontal des pods
- **[[Operators]]** — Extensions Kubernetes pour apps stateful

## Workloads

- **Deployments** → apps stateless (web, API)
- **StatefulSets** → apps stateful (bases de données)
- **DaemonSets** → un pod par node (monitoring, logging)
- **Jobs / CronJobs** → tâches ponctuelles ou planifiées

## Liens

- [[Cluster]]
- [[Pods]]
- [[Services]]
- [[ConfigMaps]]
- [[Secrets]]
- [[Volumes]]
- [[Namespaces]]
- [[RBAC]]
- [[Helm]]
- [[Operators]]
- [[HPA]]
- [[kubectl]]
- [[Advanced Kubernetes]]
- [[Service Mesh]]
