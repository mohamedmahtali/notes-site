---
title: create
tags:
  - beginner
---

# create

## Parent
- [[Container lifecycle]]

---

## Définition

`docker create` crée un conteneur à partir d'une image sans le démarrer. Le conteneur est dans l'état `created`. Utile pour préparer un conteneur avant son démarrage, ou pour inspecter sa configuration.

---

## Commandes

```bash
# Créer sans démarrer
docker create --name mon-app -p 8080:80 nginx

# Voir le conteneur créé (état = Created)
docker ps -a
# CONTAINER ID  IMAGE  STATUS   NAMES
# abc123        nginx  Created  mon-app

# Démarrer le conteneur créé
docker start mon-app
```

---

> [!note]
> En pratique, `docker run` (= `docker create` + `docker start`) est utilisé dans la plupart des cas. `docker create` est utile pour des scripts d'initialisation ou pour inspecter la configuration d'un conteneur avant de le lancer.
