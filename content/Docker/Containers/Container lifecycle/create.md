---
title: create
tags:
  - beginner
---

# create

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

## Cas d'usage concrets

```bash
# Pré-populer un volume depuis un conteneur (init pattern)
docker create --name data-init -v mydata:/data busybox
docker cp ./seed-data/ data-init:/data/
docker start data-init
# Les données sont maintenant dans le volume "mydata"

# Inspecter la config avant de lancer
docker create --name test-app \
  -e DATABASE_URL=postgres://... \
  -p 8080:80 \
  myapp:latest

docker inspect test-app    # Vérifier env, ports, volumes
docker start test-app       # Lancer seulement si config OK

# Créer plusieurs conteneurs d'un coup, les démarrer simultanément
for i in 1 2 3; do
  docker create --name worker-$i myworker:latest
done
docker start worker-1 worker-2 worker-3
```

> [!note]
> En pratique, `docker run` (= `docker create` + `docker start`) est utilisé dans la plupart des cas. `docker create` est utile pour des scripts d'initialisation ou pour inspecter la configuration d'un conteneur avant de le lancer.
