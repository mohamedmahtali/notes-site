---
title: Docker hub
tags:
  - beginner
---

# Docker hub

## Parent
- [[Docker registry]]

---

## Définition

Docker Hub est le registry public officiel de Docker. Il héberge les **images officielles** (nginx, postgres, python, node…), les images vérifiées des éditeurs, et les images publiques de la communauté. Chaque compte gratuit peut avoir un repository privé.

---

## Utiliser Docker Hub

```bash
# Connexion
docker login
# → Username: mohamedmahtali
# → Password:

# Pull d'une image officielle
docker pull nginx:latest
docker pull node:20-alpine

# Push d'une image perso
docker tag mon-app:1.0 mohamedmahtali/mon-app:1.0
docker push mohamedmahtali/mon-app:1.0
```

---

## Nomenclature

```
docker.io/library/nginx:latest       ← image officielle
docker.io/mohamedmahtali/mon-app:1.0 ← image utilisateur
          │               │       │
          namespace        nom   tag
```

---

## Limites du plan gratuit

- 1 repository privé
- Pull rate limit : 100 pulls/6h (anonyme) / 200 pulls/6h (connecté)

---

> [!tip]
> Pour les projets open source ou les images publiques, Docker Hub est idéal. Pour les images privées en production, préférer GitHub Container Registry (gratuit et intégré à GitHub Actions) ou le registry du cloud provider.
