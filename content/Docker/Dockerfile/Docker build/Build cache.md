---
title: Build cache
tags:
  - intermediate
---

# Build cache

---

## Définition

Le build cache de [[Docker]] évite de réexécuter les [[Instructions]] [[Dockerfile]] dont les inputs n'ont pas changé. Chaque layer est identifié par un hash basé sur l'instruction et le contenu des fichiers copiés. Un cache hit accélère les builds de quelques secondes à quelques minutes.

---

## Fonctionnement

```
Layer 1 : FROM node:20-alpine         → hash stable → CACHE HIT ✅
Layer 2 : WORKDIR /app                → hash stable → CACHE HIT ✅
Layer 3 : COPY package.json ./        → si package.json changé → CACHE MISS ❌
Layer 4 : RUN npm ci                  → recalculé car dépend de layer 3
Layer 5 : COPY . .                    → recalculé
```

---

## Maximiser l'utilisation du cache

```dockerfile
# ✅ Structure optimale pour Node.js
FROM node:20-alpine
WORKDIR /app

# Séparer les dépendances du code source
COPY package.json package-lock.json ./    # change rarement
RUN npm ci                                # en cache si package.json stable

COPY . .                                  # change souvent → invalide seulement ici

RUN npm run build
```

---

## Gérer le cache en CI

```bash
# Désactiver le cache (full build)
docker build --no-cache -t mon-app .

# Utiliser le cache d'une registry (GitHub Actions)
docker buildx build   --cache-from type=registry,ref=ghcr.io/user/app:cache   --cache-to type=registry,ref=ghcr.io/user/app:cache,mode=max   -t ghcr.io/user/app:latest .
```
