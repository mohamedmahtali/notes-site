---
title: Infrastructure metrics
tags:
  - intermediate
---
# Infrastructure metrics

---

## Définition

Les métriques d'infrastructure mesurent l'état des serveurs, [[Containers]], et [[Cluster]] : CPU, mémoire, disque, réseau. Elles permettent de détecter les problèmes de capacité et de performance système.

---

## Métriques clés par composant

### CPU
```promql
# Utilisation CPU
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Load average (> nombre de CPU = saturé)
node_load1 > 4   # charge 1min > 4 CPUs
```

### Mémoire
```promql
# % mémoire utilisée
(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

# Swap utilisé (mauvais signe)
node_memory_SwapTotal_bytes - node_memory_SwapFree_bytes
```

### Disque
```promql
# % espace disque utilisé
100 - (node_filesystem_avail_bytes / node_filesystem_size_bytes * 100)

# I/O utilization
rate(node_disk_io_time_seconds_total[5m]) * 100
```

### Réseau
```promql
# Trafic entrant/sortant
rate(node_network_receive_bytes_total{device!="lo"}[5m])
rate(node_network_transmit_bytes_total{device!="lo"}[5m])
```

---

## Kubernetes

```promql
# CPU par namespace
sum(rate(container_cpu_usage_seconds_total[5m])) by (namespace)

# Mémoire par pod
container_memory_working_set_bytes{container!=""}

# Pods en erreur
kube_pod_status_phase{phase=~"Failed|Unknown"} > 0
```
