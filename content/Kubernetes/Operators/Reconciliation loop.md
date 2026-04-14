---
title: Reconciliation loop
tags:
  - advanced
---
# Reconciliation loop

## Parent
- [[Operators]]

---

## Définition

La reconciliation loop est le pattern fondamental des controllers Kubernetes. Elle compare continuellement l'état désiré (spec) avec l'état réel (status) et prend les actions nécessaires pour les aligner. C'est le cœur de la philosophie Kubernetes "desired state".

---

## Le pattern

```
┌──────────────────────────────────────────────┐
│              Reconciliation Loop             │
│                                              │
│  Watch API  →  Observe  →  Diff  →  Act      │
│      ↑                               │       │
│      └───────────────────────────────┘       │
└──────────────────────────────────────────────┘

Observe : lire l'état actuel du cluster
Diff    : comparer avec l'état désiré (spec)
Act     : créer/modifier/supprimer des ressources
```

---

## Idempotence

```go
// Une reconciliation doit être idempotente
// Exécuter 100 fois avec le même état → même résultat

func Reconcile(desired State, actual State) {
    if desired == actual {
        return  // rien à faire
    }
    applyChanges(desired)  // converger vers l'état désiré
}
```

---

## Gestion des erreurs

```go
func (r *Reconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    // Erreur transiente → réessayer dans 30s
    if err := someTransientOperation(); err != nil {
        return ctrl.Result{RequeueAfter: 30 * time.Second}, err
    }

    // Succès → réessayer dans 5min (pour drift detection)
    return ctrl.Result{RequeueAfter: 5 * time.Minute}, nil
}
```

---

> [!tip]
> Concevoir les controllers pour être idempotents et tolérants aux pannes. Une reconciliation peut être interrompue à n'importe quel moment et doit reprendre proprement.
