---
title: Docker layer cache
tags:
  - intermediate
---
# Docker layer cache

## Parent
- [[Pipeline caching]]

---

## Définition

Le Docker layer cache réutilise les couches d'image Docker déjà construites pour accélérer les builds. Une couche est reconstruite seulement si elle ou ses dépendances ont changé.

---

## Cache avec GitHub Actions Cache

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build with cache
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: myapp:${{ github.sha }}
    cache-from: type=gha          # lire depuis GitHub Actions cache
    cache-to: type=gha,mode=max   # écrire dans GitHub Actions cache
```

---

## Cache depuis un registry

```yaml
- uses: docker/build-push-action@v5
  with:
    cache-from: type=registry,ref=myapp:buildcache
    cache-to: type=registry,ref=myapp:buildcache,mode=max
```

---

## Optimiser l'ordre des layers pour le cache

```dockerfile
# MAUVAIS — COPY . copie tout avant npm install
COPY . .
RUN npm install

# BON — npm install est caché si package.json ne change pas
COPY package*.json ./
RUN npm install
COPY . .
```

---

> [!tip]
> `mode=max` met en cache toutes les couches intermédiaires (même celles des multi-stage builds). `mode=min` (défaut) ne cache que les couches finales. Utiliser `max` si les builds sont lents.
