---
title: Container runtime
tags:
  - intermediate
---
# Container runtime

## Parent
- [[Node]]

---

## Définition

Le container runtime est le logiciel qui exécute les containers sur un node Kubernetes. Le kubelet communique avec lui via l'interface CRI (Container Runtime Interface). Le runtime standard est containerd.

---

## Runtimes supportés

| Runtime | Description | Défaut |
|---|---|---|
| containerd | Runtime léger, standard de facto | ✅ Depuis K8s 1.24 |
| CRI-O | Runtime minimaliste, optimisé K8s | OKD/OpenShift |
| Docker Engine | Via dockershim (supprimé K8s 1.24) | ❌ Plus supporté |

---

## Interaction avec le runtime

```bash
# Lister les containers via containerd (sur le node)
crictl ps
crictl ps -a             # tous (inclus stoppés)

# Inspecter un container
crictl inspect <container-id>

# Voir les images
crictl images

# Logs d'un container
crictl logs <container-id>

# Vérifier l'état de containerd
systemctl status containerd
```

---

## Architecture CRI

```
kubelet → CRI (gRPC) → containerd → runc → container
                     ↑
             Container Runtime Interface
```

---

> [!note]
> La suppression de dockershim dans K8s 1.24 ne signifie pas que les images Docker ne fonctionnent plus. Les images OCI (le format Docker) sont toujours supportées par containerd et CRI-O.
