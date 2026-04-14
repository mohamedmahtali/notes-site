---
title: Pods
tags:
  - beginner
---
# Pods

## Parent
- [[Kubernetes]]

## Enfants
- [[Pod lifecycle]]
- [[Deployments]]
- [[StatefulSets]]
- [[DaemonSets]]
- [[Init containers]]
- [[Sidecar containers]]

---

## Définition

Un pod est l'unité de déploiement la plus petite dans Kubernetes. Il encapsule un ou plusieurs containers qui partagent le même namespace réseau (même IP) et les mêmes volumes. Les pods sont éphémères — ils peuvent être recréés à tout moment.

---

## Pourquoi c'est important

> [!note] Ne pas déployer des pods directement
> Les pods "nus" ne se redémarrent pas en cas d'échec. En production, toujours utiliser [[Deployments]], [[StatefulSets]] ou [[DaemonSets]] qui gèrent le cycle de vie des pods.

---

## Manifeste pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  labels:
    app: myapp
    version: v1
spec:
  containers:
  - name: app
    image: myapp:1.0
    ports:
    - containerPort: 8080
    resources:
      requests:
        memory: "128Mi"
        cpu: "100m"
      limits:
        memory: "256Mi"
        cpu: "500m"
    env:
    - name: ENV
      value: production
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 30
```

---

## Commandes essentielles

```bash
# Voir les pods
kubectl get pods
kubectl get pods -n kube-system
kubectl get pods -o wide          # avec node et IP

# Détails d'un pod
kubectl describe pod myapp

# Logs
kubectl logs myapp
kubectl logs myapp -f             # follow
kubectl logs myapp -c sidecar     # container spécifique

# Shell dans un pod
kubectl exec -it myapp -- /bin/sh

# Supprimer
kubectl delete pod myapp
```

---

> [!tip]
> Toujours définir `resources.requests` pour aider le scheduler, et `resources.limits` pour éviter qu'un pod consomme toute la mémoire du node (OOM).
