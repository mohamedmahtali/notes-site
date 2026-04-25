---
title: DaemonSets
tags:
  - intermediate
---
# DaemonSets

---

## Définition

Un DaemonSet garantit qu'une copie d'un pod tourne sur chaque [[Node]] du [[Cluster]] (ou sur un sous-ensemble de nodes). Quand un node rejoint le cluster, le pod est automatiquement ajouté. Utilisé pour les agents système.

---

## Cas d'usage

> [!tip] Pour les agents système
> Les DaemonSets sont faits pour les composants qui doivent exister sur chaque node : agents de [[Logging]] (Fluentd, Filebeat), agents de [[Monitoring]] ([[Prometheus]] Node Exporter, Datadog), plugins réseau (Cilium, Calico), agents de sécurité.

---

## Manifeste

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        effect: NoSchedule               # aussi sur les control plane nodes
      hostNetwork: true                  # accès réseau du host
      hostPID: true                      # accès aux processus du host
      containers:
      - name: node-exporter
        image: prom/node-exporter:latest
        ports:
        - containerPort: 9100
          hostPort: 9100
        volumeMounts:
        - name: proc
          mountPath: /host/proc
          readOnly: true
      volumes:
      - name: proc
        hostPath:
          path: /proc
```

---

```bash
kubectl get daemonsets -A
kubectl describe daemonset node-exporter -n monitoring
```
