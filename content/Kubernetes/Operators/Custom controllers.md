---
title: Custom controllers
tags:
  - advanced
---
# Custom controllers

## Parent
- [[Operators]]

---

## Définition

Un custom controller surveille des ressources Kubernetes (natives ou CRDs) et prend des actions pour aligner l'état réel sur l'état désiré. C'est le composant actif d'un Operator.

---

## Pattern de base

```go
// Un controller Kubernetes en Go avec controller-runtime
func (r *DatabaseReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    // 1. Récupérer la ressource
    db := &myv1.Database{}
    if err := r.Get(ctx, req.NamespacedName, db); err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }

    // 2. Calculer l'état désiré
    desired := buildPostgresStatefulSet(db)

    // 3. Appliquer si nécessaire
    existing := &appsv1.StatefulSet{}
    if err := r.Get(ctx, req.NamespacedName, existing); err != nil {
        if errors.IsNotFound(err) {
            return ctrl.Result{}, r.Create(ctx, desired)
        }
        return ctrl.Result{}, err
    }

    // 4. Mettre à jour si divergence
    if !reflect.DeepEqual(existing.Spec, desired.Spec) {
        existing.Spec = desired.Spec
        return ctrl.Result{}, r.Update(ctx, existing)
    }

    return ctrl.Result{RequeueAfter: 30 * time.Second}, nil
}
```

---

## Frameworks

```bash
# Kubebuilder (officiel)
kubebuilder init --domain mycompany.com
kubebuilder create api --group mygroup --version v1 --kind Database

# Operator SDK
operator-sdk init --domain mycompany.com
operator-sdk create api --kind Database --version v1
```
