---
title: Docker build
tags:
  - beginner
---

# Docker build

---

## Définition

`docker build` est la commande qui lit un [[Dockerfile]] et construit une image [[Docker]]. Elle envoie le contexte de build au daemon Docker, exécute chaque instruction, et produit une image immutable taguée.

---

## Commandes

```bash
# Build de base (contexte = répertoire courant)
docker build -t mon-app:1.0 .

# Spécifier un Dockerfile différent
docker build -f docker/Dockerfile.prod -t mon-app:prod .

# Sans cache
docker build --no-cache -t mon-app:latest .

# Avec build args
docker build --build-arg APP_VERSION=2.0 -t mon-app:2.0 .

# Multi-plateforme
docker buildx build --platform linux/amd64,linux/arm64 -t mon-app:latest .

# Build + push directement
docker build -t registry.example.com/mon-app:latest --push .
```

---

## Processus de build

```
docker build -t mon-app:1.0 .
        ↓
1. Envoyer le contexte de build au daemon
2. Lire le Dockerfile instruction par instruction
3. Pour chaque instruction :
   → Vérifier le cache (hash du layer parent + instruction)
   → Si cache hit : utiliser le layer en cache ✅
   → Si cache miss : exécuter et créer un nouveau layer
4. Tagger l'image finale
```

---

## Optimiser le build

> [!tip] Ordre des [[Instructions]] = ordre du cache
> Mettre les instructions qui changent rarement en haut, celles qui changent souvent en bas. Un cache miss invalide tout ce qui suit.
