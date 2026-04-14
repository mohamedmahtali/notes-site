---
title: FROM
tags:
  - beginner
---

# FROM

## Parent
- [[Instructions]]

---

## Définition

`FROM` est la première instruction de tout Dockerfile. Elle définit l'image de base à partir de laquelle l'image sera construite. Tout ce qui suit est appliqué par-dessus cette base.

---

## Syntaxe

```dockerfile
FROM <image>[:<tag>] [AS <name>]

# Exemples
FROM ubuntu:22.04
FROM node:20-alpine
FROM python:3.12-slim
FROM scratch        # image vide — pour des binaires statiques
FROM node:20 AS builder   # multi-stage build
```

---

## Choisir la bonne image de base

| Base | Taille | Usage |
|---|---|---|
| `ubuntu:22.04` | ~77MB | Usage général, outils disponibles |
| `debian:bookworm-slim` | ~74MB | Slim, APT disponible |
| `alpine:3.19` | ~7MB | Ultra-léger, musl libc |
| `distroless` | ~20MB | Sécurité maximale, pas de shell |
| `scratch` | 0MB | Binaires Go/Rust statiques |

---

## Multi-stage

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM nginx:alpine AS production
COPY --from=builder /app/dist /usr/share/nginx/html
```

> [!tip] Images slim vs alpine
> `slim` = Debian allégé (compatibilité maximale). `alpine` = plus léger mais musl libc peut causer des incompatibilités avec certaines libs natives.
