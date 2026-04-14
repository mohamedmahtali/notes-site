---
title: Namespace isolation
tags: [security, intermediate]
---

# Namespace isolation

## Définition

Les namespaces Linux isolent les ressources entre processus : PID, réseau, système de fichiers, utilisateurs, etc. Les conteneurs reposent sur ces namespaces pour leur isolation.

> [!note] Limite de l'isolation
> Les conteneurs partagent le kernel. L'isolation par namespace n'est pas aussi forte que la virtualisation complète. Un exploit kernel peut briser cette isolation.

## Types de namespaces

| Namespace | Isole |
|-----------|-------|
| `pid` | Arbre de processus |
| `net` | Interfaces réseau, routes |
| `mnt` | Points de montage |
| `uts` | Hostname, domainname |
| `ipc` | IPC, sémaphores |
| `user` | UIDs/GIDs |
| `cgroup` | Vues cgroup |

## Inspecter les namespaces

```bash
# Namespaces d'un processus
ls -la /proc/<pid>/ns/

# Entrer dans le namespace réseau d'un conteneur
nsenter --target <pid> --net -- ip addr

# Voir les namespaces d'un conteneur Docker
docker inspect container_name | grep -i pid
nsenter --target <pid> --pid --mount --net -- bash
```

## User namespace (rootless containers)

```bash
# Podman en mode rootless (utilise user namespaces)
podman run --rm nginx

# L'UID 0 dans le conteneur est mappé sur un UID non-privilégié
cat /proc/self/uid_map
```

## Liens

- [[Container security]]
- [[AppArmor]]
- [[Seccomp]]
