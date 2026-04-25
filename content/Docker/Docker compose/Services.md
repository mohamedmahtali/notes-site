---
title: Services
tags:
  - beginner
---

# Services

---

## Définition

Dans [[Docker compose]], un service est la définition d'un conteneur — son image, sa configuration, ses [[Ports]], ses [[Volumes]]. Plusieurs services forment une application. Compose peut lancer plusieurs réplicas du même service.

---

## Configuration d'un service

```yaml
services:
  api:
    # Source de l'image
    build: .          # builder depuis Dockerfile local
    image: nginx:1.25 # ou utiliser une image existante

    # Ports
    ports:
      - "8080:80"     # hôte:conteneur
      - "443:443"

    # Variables d'environnement
    environment:
      - NODE_ENV=production
      - PORT=3000

    # Fichier .env
    env_file: .env

    # Volumes
    volumes:
      - ./data:/app/data
      - logvol:/var/log/app

    # Dépendances de démarrage
    depends_on:
      - db
      - redis

    # Politique de redémarrage
    restart: unless-stopped

    # Ressources
    deploy:
      resources:
        limits:
          memory: 512m
          cpus: '0.5'
```

---

## depends_on avec healthcheck

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy   # attendre que db soit healthy

  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 5s
      retries: 5
```
