---
title: Docker
tags:
  - beginner
---

# Docker

---

## Définition

Docker est une plateforme de **conteneurisation** qui permet d'empaqueter une application et toutes ses dépendances dans une unité isolée appelée conteneur. Les conteneurs sont légers, portables, et s'exécutent de manière identique sur n'importe quel système disposant du moteur Docker.

---

## Pourquoi c'est important

> [!tip] Build once, run anywhere
> Docker résout le problème classique "ça marche sur ma machine". L'image Docker garantit que l'environnement d'exécution est identique en développement, en test, et en production.

- **Isolation** : chaque conteneur a son propre filesystem, réseau, et processus
- **Légèreté** : partage le [[Kernel]] de l'hôte — démarrage en millisecondes vs minutes pour une VM
- **Portabilité** : même image sur [[Linux]], macOS, Windows, [[Cloud]]
- **CI/CD** : chaque build produit une image immutable et versionnée

---

## Concepts clés

```
Dockerfile  →  docker build  →  Image  →  docker run  →  Conteneur
                                   ↕
                            Docker Registry
                          (Docker Hub, ECR, GCR)
```

| Concept | Définition |
|---|---|
| **Image** | Template immuable en couches (read-only) |
| **Conteneur** | Instance en cours d'exécution d'une image |
| **[[Dockerfile]]** | Fichier de recette pour construire une image |
| **Registry** | Dépôt d'images ([[Docker hub]], ECR…) |
| **Volume** | Stockage persistant en dehors du conteneur |
| **Network** | Réseau virtuel entre conteneurs |

---

## Commandes essentielles

```bash
# Vérifier l'installation
docker --version
docker info

# Lancer un conteneur
docker run -d -p 8080:80 --name mon-app nginx

# Lister les conteneurs actifs
docker ps

# Lister les images
docker images

# Builder une image
docker build -t mon-app:1.0 .

# Voir les logs
docker logs mon-app

# Entrer dans un conteneur
docker exec -it mon-app bash

# Stopper et supprimer
docker stop mon-app && docker rm mon-app
```

---

## Explorer Docker

### Construire des images
- **[[Dockerfile]]** — écrire la recette de construction d'une image
- **[[Instructions]]** — référence complète (FROM, RUN, COPY, ENV, EXPOSE…)
- **[[Multi stage builds]]** — images légères pour la production
- **[[Docker build]]** — builder, tagger, gérer le cache

### Gérer les images
- **[[Images]]** — couches, tagging, base images, image caching
- **[[Docker registry]]** — [[Docker hub]], ECR, registre privé

### Gérer les conteneurs
- **[[Containers]]** — cycle de vie complet (create, start, stop, remove)
- **[[Docker run]]** — lancer avec options (ports, variables d'env, restart policy)
- **[[Resource limits]]** — limiter CPU et mémoire

### Données & Réseau
- **[[Docker volumes]]** — named volumes, bind mounts, volume drivers
- **[[Docker networks]]** — bridge, overlay, host, DNS interne

### Composition & Sécurité
- **[[Docker compose]]** — orchestrer des services multi-conteneurs en local
- **[[Docker security]]** — non-root, capability dropping, secrets handling
- **[[Container runtime]]** — containerd, runc, OCI

> [!tip] Lab pratique
> → [[Lab Docker — App Python conteneurisée]]
