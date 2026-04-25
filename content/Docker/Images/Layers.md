---
title: Layers
tags:
  - intermediate
---

# Layers

---

## Définition

Une image [[Docker]] est composée de **couches (layers)** empilées, chacune représentant un diff filesystem par rapport à la couche précédente. Les layers sont immuables, partagés entre images, et mis en cache. Un conteneur ajoute une couche d'écriture temporaire au-dessus des layers de l'image.

---

## Visualiser les layers

```bash
docker image history nginx:alpine
# IMAGE       CREATED       SIZE    COMMENT
# abc123      2 weeks ago   7.5MB   ADD alpine-minirootfs
# def456      2 weeks ago   0B      CMD ["/bin/sh"]
# ghi789      3 days ago    1.1MB   RUN apk add nginx
# ...
```

---

## Comment ça fonctionne

```
Layer 5 (RW) : Conteneur (écriture temporaire)
Layer 4 (RO) : COPY . /app          ← invalidé si code change
Layer 3 (RO) : RUN npm install      ← cache si package.json stable
Layer 2 (RO) : COPY package.json .  ← cache si fichier stable
Layer 1 (RO) : FROM node:20-alpine  ← toujours en cache
```

---

## Union filesystem

Docker utilise un union filesystem (overlay2) pour présenter les layers comme un seul filesystem cohérent. Le conteneur voit tout en un seul arbre de répertoires.

```bash
# Voir le driver de storage utilisé
docker info | grep "Storage Driver"
# Storage Driver: overlay2
```

---

## Partage des layers

Deux images partageant les mêmes layers de base ne téléchargent/stockent ces layers qu'une seule fois.

```
nginx:alpine     python:alpine
     │                │
     └──── alpine:3.19 (partagé, 7MB stocké une fois)
```

> [!tip]
> Utiliser la même image de base pour plusieurs [[Services]] maximise le partage des layers et réduit le stockage/transfert.
