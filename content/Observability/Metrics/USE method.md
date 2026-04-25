---
title: USE method
tags:
  - intermediate
---
# USE method

---

## Définition

La méthode USE (Utilization, Saturation, Errors) de Brendan Gregg est une framework pour analyser les performances d'un système en se concentrant sur les ressources matérielles : CPU, mémoire, réseau, disque.

---

## Les trois dimensions

| Dimension | Description | Exemples métriques |
|---|---|---|
| **U**tilization | % de temps où la ressource est occupée | CPU usage, disk I/O util |
| **S**aturation | Travail en attente (queue) | CPU run queue, disk queue depth |
| **E**rrors | Erreurs de la ressource | Network errors, disk errors |

---

## Application pratique

```bash
# CPU
# Utilization: top, htop → %CPU
# Saturation: uptime → load average (> nb CPU = saturé)
# Errors: dmesg | grep -i cpu

# Mémoire
# Utilization: free -h → used/total
# Saturation: vmstat → si → swap in/out > 0
# Errors: dmesg | grep -i "out of memory"

# Réseau
# Utilization: ifstat, iftop → bandwidth usage vs capacité
# Saturation: netstat -s → receive errors, drop packets
# Errors: ip -s link → errors, dropped

# Disque
# Utilization: iostat -xz 1 → %util
# Saturation: iostat → await (temps d'attente > 10ms = saturé)
# Errors: dmesg | grep -i "I/O error"
```

---

## Checklist USE pour un incident

```
Pour chaque ressource (CPU, mémoire, disque, réseau) :
□ Utilization > 70% ? (problème de capacité)
□ Saturation > 0 ? (workload en attente)
□ Errors > 0 ? (problème matériel ou logiciel)
```

---

> [!tip]
> Commencer par la méthode USE pour les problèmes de performance système. Si USE est normal, passer à [[RED method]] pour l'application.
