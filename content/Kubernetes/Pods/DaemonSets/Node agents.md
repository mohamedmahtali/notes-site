---
title: Node agents
tags:
  - intermediate
---
# Node agents

---

## Définition

Les [[Node]] agents sont des processus qui doivent tourner sur chaque node pour collecter des métriques, des logs, ou appliquer des politiques de sécurité. Ils sont déployés via [[DaemonSets]].

---

## Exemples d'agents par catégorie

### Logging
```yaml
# Fluentd — collecte et forward les logs
- name: fluentd
  image: fluent/fluentd-kubernetes-daemonset:v1-debian-elasticsearch
  volumeMounts:
  - name: varlog
    mountPath: /var/log
  - name: varlibdockercontainers
    mountPath: /var/lib/docker/containers
    readOnly: true
```

### Monitoring
```yaml
# Datadog agent
- name: datadog-agent
  image: datadog/agent:latest
  env:
  - name: DD_API_KEY
    valueFrom:
      secretKeyRef:
        name: datadog
        key: api-key
  - name: DD_COLLECT_KUBERNETES_EVENTS
    value: "true"
```

### Réseau
```bash
# Cilium (CNI) est déployé comme DaemonSet
kubectl get daemonset -n kube-system cilium
```

---

## Accès au système hôte

```yaml
spec:
  hostNetwork: true    # utilise le namespace réseau du host
  hostPID: true        # accès aux PIDs du host
  hostIPC: true        # accès à l'IPC du host
  volumes:
  - name: host-root
    hostPath:
      path: /
```

---

> [!warning]
> Les agents avec accès `hostNetwork: true` ou `hostPath` ont un impact de sécurité important. Limiter ces privilèges au strict nécessaire.
