---
title: System calls
tags:
  - advanced
---

# System calls

## Parent
- [[Kernel]]

---

## Définition

Les appels système (syscalls) sont l'interface entre les applications user-space et le kernel. Quand une application veut lire un fichier, créer un processus, ou ouvrir une socket, elle passe par un syscall — le kernel effectue l'opération en kernel-space.

---

## Syscalls fondamentaux

| Syscall | Action |
|---|---|
| `read` / `write` | Lire/écrire des données |
| `open` / `close` | Ouvrir/fermer un fichier |
| `fork` / `exec` | Créer/exécuter un processus |
| `exit` | Terminer un processus |
| `socket` / `connect` | Réseau |
| `mmap` | Mapper de la mémoire |
| `clone` | Créer un thread/processus (namespaces) |

---

## Observer les syscalls

```bash
# Tracer les syscalls d'un programme
strace ls -la
strace -p PID   # processus en cours

# Compter les syscalls
strace -c ls

# Filtrer les syscalls d'un type
strace -e read,write cat fichier.txt

# perf (kernel tracing)
perf stat ls
```

---

## Seccomp (filtrage des syscalls)

```bash
# Docker utilise seccomp pour limiter les syscalls des conteneurs
docker run --security-opt seccomp=default.json mon-app

# Voir le profil seccomp par défaut de Docker
docker info | grep seccomp
```

---

> [!note]
> En DevOps, la compréhension des syscalls est utile pour déboguer des problèmes de performance (`strace`), comprendre la sécurité des conteneurs (seccomp), et diagnostiquer des erreurs "permission denied" inattendues.
