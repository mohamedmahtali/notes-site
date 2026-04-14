---
title: exec
tags:
  - beginner
---
# exec

## Parent
- [[kubectl]]

---

## Définition

`kubectl exec` exécute une commande dans un container en cours d'exécution, similaire à `docker exec`. Permet d'obtenir un shell interactif pour déboguer un pod depuis l'intérieur.

---

## Utilisation

```bash
# Shell interactif
kubectl exec -it myapp-abc12 -- /bin/bash
kubectl exec -it myapp-abc12 -- /bin/sh    # si pas de bash

# Container spécifique
kubectl exec -it myapp-abc12 -c sidecar -- /bin/sh

# Commande non-interactive
kubectl exec myapp-abc12 -- env
kubectl exec myapp-abc12 -- cat /etc/hosts
kubectl exec myapp-abc12 -- ls /var/log

# Copier des fichiers (kubectl cp)
kubectl cp myapp-abc12:/var/log/app.log ./app.log
kubectl cp ./config.yaml myapp-abc12:/etc/app/config.yaml
```

---

## Debug sans shell dans l'image

```bash
# Si l'image n'a pas de shell (distroless)
kubectl debug -it myapp-abc12 --image=busybox --target=app

# Ephemeral container (K8s 1.23+)
kubectl debug -it myapp-abc12   --image=nicolaka/netshoot   --target=app
```

---

> [!warning]
> `kubectl exec` en production doit être une opération exceptionnelle et auditée. Préférer les logs et les métriques pour le débogage quotidien. L'accès exec contourne les contrôles de l'application.
