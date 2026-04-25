---
title: Container runtime
tags:
  - advanced
---

# Container runtime

---

## Définition

Un container runtime est le logiciel qui exécute concrètement les conteneurs sur le système d'exploitation hôte. [[Docker]] n'est pas le runtime — il délègue l'exécution à des runtimes sous-jacents : [[containerd]] (high-level) et [[runc]] (low-level).

---

## Architecture

```
Docker CLI
    ↓
Docker daemon (dockerd)
    ↓
containerd (high-level runtime)
    ↓
runc (low-level runtime, OCI compliant)
    ↓
Linux kernel (namespaces, cgroups)
```

---

## Couches du runtime

| Couche | Outil | Rôle |
|---|---|---|
| High-level runtime | containerd | Gestion images, snapshots, réseau |
| Low-level runtime | runc | Création des conteneurs ([[Namespaces]]/cgroups) |
| Spécification | [[OCI]] | Standard d'interopérabilité |

---

## Alternatives à runc

| Runtime | Avantages |
|---|---|
| `runc` | Standard, utilisé par défaut |
| `crun` | Plus léger, compatible OCI |
| `gVisor` (runsc) | Sécurité renforcée ([[Kernel]] virtuel) |
| `kata-containers` | VM légère = isolation maximale |

---

> [!note]
> [[Kubernetes]] utilise directement `containerd` (ou CRI-O) — le daemon Docker n'est plus nécessaire depuis Kubernetes 1.24 (dockershim supprimé).
