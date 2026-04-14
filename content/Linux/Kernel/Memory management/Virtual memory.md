---
title: Virtual memory
tags:
  - advanced
---

# Virtual memory

## Parent
- [[Memory management]]

---

## Définition

La mémoire virtuelle donne à chaque processus l'illusion d'avoir un espace d'adressage privé et continu, quelle que soit la RAM physique disponible. Le kernel mappe les adresses virtuelles vers des adresses physiques via les tables de pages.

---

## Avantages

```
Isolation : chaque processus a son propre espace → pas d'accès mémoire croisé
Flexibilité : les processus peuvent utiliser plus de mémoire que la RAM (via swap)
Sécurité : impossible pour un processus d'accéder directement à la RAM d'un autre
Partage : plusieurs processus peuvent partager les mêmes pages physiques (bibliothèques)
```

---

## Espaces d'adressage

```
Processus 64 bits :
0x0000000000000000  → 0x00007FFFFFFFFFFF  : user space (128 TB)
0xFFFF800000000000  → 0xFFFFFFFFFFFFFFFF  : kernel space

Sections dans l'espace user :
  code (text)    : instructions du programme
  data           : variables globales initialisées
  bss            : variables globales non-initialisées
  heap           : malloc/new (croît vers le haut)
  mmap region    : bibliothèques partagées
  stack          : variables locales, appels (croît vers le bas)
```

---

## Observer

```bash
# Mémoire virtuelle d'un processus
cat /proc/PID/maps     # toutes les zones mappées
cat /proc/PID/status | grep -i vm
# VmSize:  total virtual memory
# VmRSS:   RAM physique utilisée (resident)
# VmSwap:  en swap
```
