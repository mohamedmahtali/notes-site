---
title: "Kubernetes + Observability : surveiller un cluster"
tags:
  - connexion
  - kubernetes
  - observability
  - intermediate
---

# Kubernetes + Observability : surveiller un cluster

## Pourquoi cette connexion est critique

Un cluster [[Kubernetes]] sans [[Observability]], c'est une boîte noire. Quand un Pod crashe, quand la latence monte, quand un nœud sature — sans métriques, logs et traces, le diagnostic prend des heures. L'observabilité est la condition pour opérer Kubernetes en production.

```
┌──────────────────────────────────────────────────────┐
│                  Cluster Kubernetes                   │
│                                                       │
│  Pods      → métriques → Prometheus (scrape :9090)   │
│  Pods      → logs      → Loki (via Promtail/Fluentd) │
│  Pods      → traces    → Jaeger / OpenTelemetry       │
│  Nodes     → métriques → Node Exporter               │
│  K8s API   → événements → Alertmanager               │
│                                                       │
│  Toutes ces données → Grafana (dashboards unifiés)   │
└──────────────────────────────────────────────────────┘
```

## Les 3 piliers sur Kubernetes

### Métriques — Prometheus

[[Monitoring/Prometheus|Prometheus]] scrape les endpoints `/metrics` exposés par les Pods et les composants K8s :

```yaml
# Les Pods exposent leurs métriques sur :9090 (ou autre port)
# kube-state-metrics expose l'état des objets K8s
# node-exporter expose les métriques des nœuds
```

Métriques clés à monitorer :
- `container_cpu_usage_seconds_total` — CPU par conteneur
- `container_memory_usage_bytes` — RAM par conteneur
- `kube_pod_status_phase` — état des Pods (Running/Failed/Pending)
- `kube_deployment_status_replicas_unavailable` — Pods indisponibles

### Logs — Loki / ELK

Les Pods écrivent sur `stdout/stderr` → Kubernetes capture → agent collecte (Promtail, Fluent Bit) → Loki ou Elasticsearch.

```bash
# Voir les logs en temps réel
kubectl logs -f deployment/app --all-containers
kubectl logs -l app=frontend --since=1h
```

### Traces — OpenTelemetry

Le SDK [[Tracing/OpenTelemetry|OpenTelemetry]] dans l'application envoie les traces à Jaeger ou Tempo. Le service mesh ([[Service Mesh]]) peut injecter automatiquement du tracing sans modifier le code.

## Alertes utiles sur K8s

| Alerte | Condition | Action |
|--------|-----------|--------|
| `PodCrashLooping` | `restart_count > 5 en 1h` | Voir les logs du Pod |
| `NodeNotReady` | Node en état NotReady | Vérifier kubelet, réseau |
| `PodPending > 15min` | Pod bloqué en Pending | Vérifier resources, PVC |
| `HighMemoryUsage` | RAM > 90% d'une node | Scale horizontal ou vertical |
| `DeploymentReplicasMismatch` | Replicas demandés ≠ disponibles | Vérifier les events |

## Stack complète recommandée

```
kube-prometheus-stack (Helm chart)
├── Prometheus          ← collecte métriques
├── Alertmanager        ← routage des alertes
├── Grafana             ← dashboards (K8s built-in)
├── node-exporter       ← métriques nœuds
└── kube-state-metrics  ← état des objets K8s

+ Loki + Promtail       ← logs centralisés
+ Tempo ou Jaeger       ← traces distribuées
```

> [!tip] Dashboards Grafana préconstruits
> Le chart `kube-prometheus-stack` inclut des dashboards Kubernetes prêts à l'emploi (ID Grafana : 315, 6417, 13332). Pas besoin de tout créer from scratch.

## Points d'attention

> [!warning] Observabilité = overhead
> Prometheus, Loki et les agents de collecte consomment des ressources. Dimensionner les `requests/limits` de la stack d'observabilité, sinon elle devient elle-même une source d'incidents.

> [!tip] Labels Kubernetes = dimensions métriques
> Les labels K8s (`app`, `namespace`, `env`) se retrouvent dans les métriques Prometheus. Des labels bien choisis permettent de filtrer et agréger les métriques par équipe, service ou environnement.

## Pour aller plus loin

- [[Monitoring/Prometheus|Prometheus]] — scraping, PromQL, règles d'alerte
- [[Grafana]] — dashboards, panels, alerting
- [[SLO SLA SLI]] — définir la fiabilité du cluster et des apps
- [[Kubernetes]] — Deployments, Pods, ressources
- [[Observability/Monitoring/Alertmanager|Alertmanager]] — routage et silences
