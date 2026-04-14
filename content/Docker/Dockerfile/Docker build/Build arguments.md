---
title: Build arguments
tags:
  - intermediate
---

# Build arguments

## Parent
- [[Docker build]]

---

## Définition

Les build arguments (`ARG`) sont des variables disponibles uniquement pendant la construction de l'image (phase build). Contrairement à `ENV`, ils ne sont pas persistés dans l'image finale ni disponibles dans les conteneurs.

---

## Syntaxe

```dockerfile
# Déclarer avec valeur par défaut
ARG NODE_VERSION=20
ARG APP_VERSION

FROM node:${NODE_VERSION}-alpine

ARG BUILD_DATE
ARG GIT_COMMIT

LABEL build-date=$BUILD_DATE       git-commit=$GIT_COMMIT
```

```bash
# Passer les valeurs au build
docker build   --build-arg APP_VERSION=2.1.0   --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ)   --build-arg GIT_COMMIT=$(git rev-parse --short HEAD)   -t mon-app:2.1.0 .
```

---

## ARG avant FROM

```dockerfile
# ARG avant FROM permet de paramétrer l'image de base
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim
```

---

## ARG vs ENV

| | Disponible build | Disponible runtime | Secret safe |
|---|---|---|---|
| `ARG` | ✅ | ❌ | ⚠️ Visible dans history |
| `ENV` | ✅ | ✅ | ❌ Visible dans inspect |

> [!warning]
> `ARG` n'est pas sécurisé pour les secrets — visible dans `docker history`. Utiliser les secrets de build : `docker build --secret`.
