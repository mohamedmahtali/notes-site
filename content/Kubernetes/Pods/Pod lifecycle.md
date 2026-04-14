---
title: Pod lifecycle
tags:
  - intermediate
---
# Pod lifecycle

## Parent
- [[Pods]]

---

## Définition

Le cycle de vie d'un pod suit plusieurs phases, de la création à la terminaison. Comprendre ces phases est essentiel pour déboguer les pods bloqués et configurer correctement les probes et les politiques de restart.

---

## Phases d'un pod

| Phase | Description |
|---|---|
| `Pending` | Pod accepté mais containers pas encore démarrés (scheduling en cours, image en pull) |
| `Running` | Au moins un container tourne |
| `Succeeded` | Tous les containers ont terminé avec code 0 (Jobs) |
| `Failed` | Au moins un container a terminé avec code non-0 |
| `Unknown` | État du pod non connu (problème communication node/API server) |

---

## Statuts des containers

```bash
kubectl get pod myapp -o jsonpath='{.status.containerStatuses[*].state}'

# États possibles d'un container :
# Waiting  — en attente (pull image, init containers)
# Running  — en cours d'exécution
# Terminated — terminé (avec exitCode)
```

---

## Termination gracieuse

```
1. Pod marqué Terminating (deletionTimestamp set)
2. SIGTERM envoyé au container
3. Grace period (défaut 30s) — le container peut se terminer proprement
4. Si toujours vivant après grace period → SIGKILL
5. Pod supprimé de l'API
```

```yaml
spec:
  terminationGracePeriodSeconds: 60  # personnaliser le grace period
```

---

## Débogage

```bash
# Pod en CrashLoopBackOff
kubectl describe pod myapp | grep -A 5 "Events:"
kubectl logs myapp --previous      # logs avant le crash

# Pod en Pending
kubectl describe pod myapp | grep -A 10 "Events:"
# Chercher: Insufficient cpu/memory, No nodes available, Unschedulable
```
