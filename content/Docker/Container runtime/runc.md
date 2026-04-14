---
title: runc
tags:
  - advanced
---

# runc

## Parent
- [[Container runtime]]

---

## Définition

runc est le low-level container runtime de référence, conforme à la spécification OCI. Il est responsable de la création effective des conteneurs via les primitives Linux : namespaces (isolation), cgroups (ressources), et seccomp (filtrage des syscalls).

---

## Primitives Linux utilisées

| Primitive | Rôle |
|---|---|
| `namespaces` | Isolation (PID, réseau, FS, utilisateur…) |
| `cgroups` | Limitation des ressources (CPU, mémoire) |
| `seccomp` | Filtrage des appels système |
| `capabilities` | Réduction des privilèges root |
| `chroot` / `pivot_root` | Isolation du filesystem |

---

## Utiliser runc directement

```bash
# runc est rarement utilisé directement
# mais voici comment ça fonctionne :

# Créer un bundle OCI
mkdir -p /mycontainer/rootfs
docker export $(docker create busybox) | tar -C /mycontainer/rootfs -xvf -
cd /mycontainer
runc spec   # génère config.json

# Lancer le conteneur
runc run mycontainer
```

---

> [!note]
> En tant que développeur ou DevOps, tu n'interagis jamais directement avec runc. Comprendre son rôle aide à déboguer des problèmes bas niveau (permissions, cgroups, seccomp profiles) mais Docker/containerd l'abstrait complètement.
