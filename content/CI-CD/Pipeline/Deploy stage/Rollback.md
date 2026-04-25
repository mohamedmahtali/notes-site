---
title: Rollback
tags:
  - intermediate
---
# Rollback

---

## Définition

Un rollback est le retour à une version précédente stable après un déploiement défaillant. En CI/CD, il doit être aussi simple et rapide que le déploiement lui-même — idéalement automatisé via [[Monitoring]].

---

## Pourquoi c'est important

> [!warning] Le rollback doit être instantané
> Si un rollback prend 30 minutes, les utilisateurs subissent la panne pendant 30 minutes. L'objectif : rollback en moins de 2 minutes. C'est pour ça qu'on garde les images [[Docker]] taguées par SHA et les manifests [[Helm]] versionnés.

---

## Stratégies de rollback

```bash
# Kubernetes — rollback immédiat
kubectl rollout undo deployment/myapp
kubectl rollout undo deployment/myapp --to-revision=3
kubectl rollout status deployment/myapp    # vérifier

# Helm — rollback vers revision précédente
helm rollback myapp
helm rollback myapp 5                      # revision spécifique
helm history myapp                         # voir les revisions

# Docker Swarm
docker service update --image myapp:previous-sha myapp
```

---

## Rollback automatique en pipeline

```yaml
- name: Deploy
  run: kubectl set image deployment/myapp app=myapp:${{ github.sha }}

- name: Verify deployment
  run: |
    kubectl rollout status deployment/myapp --timeout=5m ||     (kubectl rollout undo deployment/myapp && exit 1)

- name: Check error rate
  run: |
    sleep 60
    ./scripts/check-metrics.sh ||     (kubectl rollout undo deployment/myapp && exit 1)
```

---

> [!tip]
> Blue/green deployment rend le rollback trivial : il suffit de rebasculer le load balancer vers l'ancienne version (blue) toujours en vie.
