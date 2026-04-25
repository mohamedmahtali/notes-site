---
title: describe
tags:
  - beginner
---
# describe

---

## Définition

`kubectl describe` affiche une description détaillée d'une ressource : métadonnées, spec, [[Status]], et surtout les **Events** — qui sont le premier endroit à regarder pour diagnostiquer un problème.

---

## Utilisation

```bash
# Describe par nom
kubectl describe pod myapp-abc12
kubectl describe deployment myapp
kubectl describe node worker-1
kubectl describe service myapp

# Describe par label
kubectl describe pods -l app=myapp

# Types de ressources à décrire souvent
kubectl describe pod myapp       # CrashLoopBackOff, OOMKilled
kubectl describe pvc my-pvc      # problèmes de provisioning
kubectl describe node worker-1   # node conditions, capacité
```

---

## Events — la section clé

```
Events:
  Type     Reason            Age    From               Message
  ----     ------            ----   ----               -------
  Warning  FailedScheduling  2m     default-scheduler  Insufficient memory
  Normal   Scheduled         90s    default-scheduler  Successfully assigned
  Normal   Pulling           88s    kubelet            Pulling image "myapp:1.0"
  Normal   Pulled            60s    kubelet            Successfully pulled
  Normal   Created           60s    kubelet            Created container app
  Normal   Started           59s    kubelet            Started container app
```

---

## Débogage courant

```bash
# Pod en Pending
kubectl describe pod myapp | grep -A 5 Events
# → FailedScheduling: 0/3 nodes available: Insufficient cpu

# Pod en CrashLoopBackOff
kubectl describe pod myapp | grep -A 3 "Last State"
# → Terminated: Reason: OOMKilled / ExitCode: 137
```
