---
title: Base images
tags:
  - beginner
---

# Base images

---

## Définition

Une image de base est l'image de départ référencée dans `FROM`. Elle définit l'OS, les outils disponibles, et le point de départ des [[Layers]] de ton application.

---

## Images de base courantes

| Image | Taille | Avantages | Inconvénients |
|---|---|---|---|
| `ubuntu:22.04` | 77MB | Familier, apt, outils courants | Lourd |
| `debian:bookworm-slim` | 74MB | Slim, APT, bonne compat | Moyen |
| `alpine:3.19` | 7MB | Ultra léger | musl libc, ash par défaut |
| `distroless/base` | ~20MB | Sécurisé, pas de [[Shell]] | Debug difficile |
| `scratch` | 0MB | Minimal absolu | Binaires statiques seulement |

---

## Images officielles par runtime

```dockerfile
FROM node:20-alpine          # Node.js léger
FROM node:20-bookworm-slim   # Node.js Debian slim

FROM python:3.12-slim        # Python slim
FROM python:3.12-alpine      # Python alpine

FROM golang:1.22-alpine      # Go (pour multi-stage)

FROM nginx:1.25-alpine       # Nginx léger
FROM nginx:1.25              # Nginx Debian

FROM openjdk:21-slim         # Java
```

---

## Bonnes pratiques

> [!tip] Toujours pin la version
> `FROM node:latest` cassera ton build au prochain breaking change.
> `FROM node:20.11.0-alpine3.19` est reproductible.

> [!warning]
> `alpine` peut causer des problèmes de compatibilité avec des [[Package]] Python qui nécessitent glibc (ex: `numpy`, `scipy`). Préférer `slim` pour les apps Python.
