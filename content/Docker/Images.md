---
title: Images
tags:
  - beginner
---

# Images

## Parent
- [[Docker]]

## Enfants
- [[Layers]]
- [[Base images]]
- [[Image tagging]]
- [[Image caching]]

---

## Définition

Une image Docker est un **template immuable en lecture seule** composé de couches (layers) superposées. Chaque couche représente un ensemble de modifications filesystem. Une image est le plan de construction d'un conteneur.

---

## Commandes essentielles

```bash
# Lister les images locales
docker images
docker image ls

# Télécharger une image
docker pull nginx:1.25
docker pull python:3.12-slim

# Inspecter une image
docker inspect nginx:1.25

# Voir les layers
docker image history nginx:1.25

# Supprimer une image
docker rmi nginx:1.25
docker image rm nginx:1.25

# Supprimer les images non utilisées
docker image prune

# Tagger une image
docker tag mon-app:latest registry.example.com/mon-app:1.0

# Builder une image
docker build -t mon-app:1.0 .
```

---

## Anatomie d'un nom d'image

```
registry.example.com/namespace/nom-image:tag

docker.io/library/nginx:1.25-alpine
│          │       │     │
│          │       │     └── tag (version)
│          │       └── nom de l'image
│          └── namespace (user ou org)
└── registry (docker.io par défaut)
```
