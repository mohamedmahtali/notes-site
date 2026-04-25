---
title: Kernel
tags:
  - advanced
---
# Kernel

---

## Définition

Le kernel [[Linux]] est le cœur du système d'exploitation. Il gère les ressources matérielles (CPU, mémoire, périphériques), fournit des abstractions aux processus (fichiers, sockets, mémoire virtuelle), et arbitre l'accès concurrent entre les applications.

---

## Pourquoi c'est important

> [!note] La couche invisible qui orchestre tout
> Chaque appel système (`read()`, `write()`, `fork()`) passe par le kernel. Comprendre le kernel explique pourquoi certaines opérations sont lentes (context switches, page faults), pourquoi les [[Permissions]] fonctionnent, et comment les conteneurs s'isolent.

---

## Architecture

```
Applications (espace utilisateur)
    ↓ appels système (syscalls)
Kernel (espace noyau)
    ├── Gestion des processus (scheduler)
    ├── Gestion mémoire (MM)
    ├── Système de fichiers virtuel (VFS)
    ├── Réseau (TCP/IP stack)
    └── Pilotes de périphériques
    ↓
Matériel (CPU, RAM, disques, réseau)
```

---

## Commandes essentielles

```bash
# Version du kernel
uname -r
uname -a

# Informations détaillées
cat /proc/version
cat /proc/cpuinfo | grep "model name" | head -1
cat /proc/meminfo | head -5

# Logs kernel (messages de démarrage + runtime)
dmesg | tail -50
dmesg -H                     # format humain avec timestamps
journalctl -k                # logs kernel via journald

# Paramètres kernel runtime
sysctl -a | grep net.ipv4.ip_forward
sysctl net.core.somaxconn
sysctl -w net.ipv4.ip_forward=1   # modifier à chaud
```

---

> [!tip]
> Voir [[Modules]] pour charger/décharger des pilotes, [[System calls]] pour l'interface kernel/userspace, [[Memory management]] pour la gestion de la mémoire virtuelle.
