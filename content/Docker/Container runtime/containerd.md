---
title: containerd
tags:
  - advanced
---

# containerd

## Parent
- [[Container runtime]]

---

## Définition

containerd est un high-level container runtime, maintenu par la CNCF. Il gère le cycle de vie complet des conteneurs : pull des images, création des snapshots filesystem, exécution via runc, et gestion du réseau. C'est le runtime standard utilisé par Docker et Kubernetes.

---

## Rôle dans l'écosystème

```
Docker daemon → containerd → runc → conteneur
Kubernetes    → containerd → runc → conteneur
               (via CRI)
```

---

## Utiliser containerd directement

```bash
# Interface CLI de containerd
ctr containers list
ctr images list
ctr images pull docker.io/library/nginx:alpine
ctr run docker.io/library/nginx:alpine mon-nginx

# Interface plus user-friendly (nerdctl)
nerdctl run -d -p 8080:80 nginx
nerdctl ps
```

---

## Configuration

```toml
# /etc/containerd/config.toml
[plugins."io.containerd.grpc.v1.cri"]
  sandbox_image = "registry.k8s.io/pause:3.9"

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  runtime_type = "io.containerd.runc.v2"
```

---

> [!note]
> En production Kubernetes, containerd est configuré et géré par le cluster. Tu n'interagis généralement pas directement avec lui sauf pour le débogage bas niveau.
