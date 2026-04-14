---
title: logs
tags:
  - beginner
---
# logs

## Parent
- [[kubectl]]

---

## Définition

`kubectl logs` récupère les logs stdout/stderr d'un container dans un pod. C'est le premier outil de débogage pour comprendre pourquoi une application échoue.

---

## Utilisation

```bash
# Logs d'un pod (container unique)
kubectl logs myapp-abc12

# Follow (streaming en temps réel)
kubectl logs myapp-abc12 -f

# Dernières N lignes
kubectl logs myapp-abc12 --tail=100

# Logs depuis X temps
kubectl logs myapp-abc12 --since=1h
kubectl logs myapp-abc12 --since-time='2024-01-15T10:00:00Z'

# Container spécifique (pod multi-container)
kubectl logs myapp-abc12 -c sidecar

# Logs du container précédent (après un crash)
kubectl logs myapp-abc12 --previous
kubectl logs myapp-abc12 -p          # raccourci

# Tous les pods d'un Deployment
kubectl logs deployment/myapp
kubectl logs -l app=myapp --all-containers

# Timestamps
kubectl logs myapp-abc12 --timestamps
```

---

## Rétention des logs

Les logs kubectl ne sont disponibles que si le pod existe encore. Pour un historique long terme, utiliser un stack de logging centralisé : EFK (Elasticsearch + Fluentd + Kibana) ou Loki + Grafana.

---

> [!tip]
> `kubectl logs -p` (previous) est crucial pour diagnostiquer un CrashLoopBackOff — il montre les logs du container avant qu'il ne crashe.
