---
title: Paging
tags:
  - advanced
---

# Paging

---

## Définition

La pagination divise la mémoire en pages de taille fixe (généralement 4 KB). Le [[Kernel]] maintient des tables de pages qui mapent les adresses virtuelles vers les adresses physiques. Les pages peuvent être en RAM ou sur disque ([[Swap]]).

---

## Fonctionnement

```
Adresse virtuelle → MMU (Memory Management Unit) → Adresse physique
                    ↓ (table de pages)
                   Page en RAM → accès direct
                   Page sur disque (swap) → page fault → charger la page
```

---

## Page faults

```bash
# Un page fault se produit quand le processus accède à une page non chargée en RAM
# C'est normal (chargement paresseux des bibliothèques)
# Un trop grand nombre de major page faults = problème de mémoire insuffisante

# Observer les page faults
perf stat -e page-faults ./mon-programme

# Via /proc
cat /proc/PID/stat | awk '{print "Minor faults:", $10, "Major faults:", $12}'
```

---

## Huge Pages

```bash
# Les Huge Pages (2MB) réduisent le TLB miss pour les applications nécessitant beaucoup de mémoire
# (PostgreSQL, JVM, bases de données)

# Configurer
echo 1024 > /proc/sys/vm/nr_hugepages
# Permanent : vm.nr_hugepages = 1024

# Voir
cat /proc/meminfo | grep Huge
```
