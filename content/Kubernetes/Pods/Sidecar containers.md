---
title: Sidecar containers
tags:
  - intermediate
---
# Sidecar containers

## Parent
- [[Pods]]

---

## Définition

Un sidecar container est un container secondaire dans le même pod que le container applicatif principal. Il partage le réseau et les volumes du pod, et enrichit ou étend le comportement de l'application sans modifier son code.

---

## Pattern sidecar

```
Pod:
├── Container principal (app)     — logique métier
├── Sidecar: proxy (Envoy)        — gestion TLS, retry, circuit breaking
├── Sidecar: log collector        — collecte et forward les logs
└── Sidecar: metrics exporter     — expose les métriques
```

---

## Exemples concrets

### Envoy proxy (service mesh)
```yaml
containers:
- name: app
  image: myapp:1.0
- name: envoy-proxy
  image: envoyproxy/envoy:v1.28
  ports:
  - containerPort: 9901
```

### Log shipper
```yaml
containers:
- name: app
  image: myapp:1.0
  volumeMounts:
  - name: logs
    mountPath: /var/log/app
- name: log-shipper
  image: fluent/fluent-bit:2.1
  volumeMounts:
  - name: logs
    mountPath: /var/log/app
    readOnly: true
volumes:
- name: logs
  emptyDir: {}
```

---

## Sidecar natif (K8s 1.29+)

```yaml
initContainers:
- name: log-shipper
  image: fluent/fluent-bit:2.1
  restartPolicy: Always    # le rend "sidecar natif" — tourne en continu
```

---

> [!tip]
> Le service mesh Istio injecte automatiquement un sidecar Envoy dans chaque pod du namespace configuré — sans modifier les manifests applicatifs.
