---
title: Image caching
tags:
  - intermediate
---

# Image caching

---

## Définition

[[Docker]] met en cache chaque layer d'image localement. Lors d'un `docker pull`, seuls les [[Layers]] manquants sont téléchargés. Lors d'un `docker build`, les layers non modifiés sont réutilisés depuis le cache local (ou un registry cache).

---

## Cache local

```bash
# Lister les images en cache
docker images

# Voir l'espace utilisé par le cache
docker system df

# Inspecter les layers partagés
docker image inspect nginx:alpine | grep -A5 Layers
```

---

## Cache de build

```bash
# Utiliser le cache existant (comportement par défaut)
docker build -t mon-app .

# Désactiver le cache (fresh build)
docker build --no-cache -t mon-app .

# Cache depuis un registry (CI/CD)
docker buildx build   --cache-from=type=registry,ref=ghcr.io/org/app:cache   --cache-to=type=registry,ref=ghcr.io/org/app:cache   -t ghcr.io/org/app:latest   --push .
```

---

## Nettoyage du cache

```bash
# Supprimer les images non utilisées
docker image prune

# Supprimer toutes les images non utilisées par un conteneur actif
docker image prune -a

# Nettoyage complet (images + conteneurs + volumes + réseaux)
docker system prune -a
```

> [!tip]
> En CI, utiliser le registry cache plutôt que le cache du filesystem CI — le cache survit entre les runs et entre les agents.
