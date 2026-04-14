---
title: Docker run
tags:
  - beginner
---

# Docker run

## Parent
- [[Docker]]

## Enfants
- [[Port mapping]]
- [[Environment variables]]
- [[Detached mode]]
- [[Restart policy]]

---

## Définition

`docker run` est la commande qui crée et démarre un conteneur depuis une image. C'est la commande la plus utilisée au quotidien — elle combine `docker create` + `docker start` avec de nombreuses options de configuration.

---

## Syntaxe

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARGS...]
```

---

## Options essentielles

```bash
docker run   -d \                          # detached (arrière-plan)
  --name mon-api \              # nom du conteneur
  -p 8080:3000 \                # port mapping hôte:conteneur
  -e NODE_ENV=production \      # variable d'environnement
  -v /data:/app/data \          # volume mount
  --network mon-reseau \        # réseau Docker
  --restart=unless-stopped \    # politique de redémarrage
  --memory=512m \               # limite mémoire
  --cpus=0.5 \                  # limite CPU
  --rm \                        # auto-suppression à l'arrêt
  mon-app:1.0                   # image
```

---

## Exemples courants

```bash
# Serveur web en arrière-plan
docker run -d -p 80:80 --name nginx nginx

# Base de données avec volume persistant
docker run -d   --name postgres   -e POSTGRES_PASSWORD=secret   -v pgdata:/var/lib/postgresql/data   postgres:16

# Shell interactif temporaire
docker run --rm -it ubuntu bash

# Commande one-shot
docker run --rm python:3.12 python -c "print('hello')"
```
