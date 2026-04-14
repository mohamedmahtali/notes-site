---
title: Image pull and push
tags:
  - beginner
---

# Image pull and push

## Parent
- [[Docker registry]]

---

## Définition

`docker pull` télécharge une image depuis un registry vers le cache local. `docker push` envoie une image locale vers un registry. Ces opérations transfèrent uniquement les layers manquants grâce au contenu adressé par hash.

---

## Pull

```bash
# Pull de l'image "latest" (déconseillé en prod)
docker pull nginx

# Pull d'une version précise (recommandé)
docker pull nginx:1.25.3-alpine

# Pull depuis un registry privé
docker pull ghcr.io/org/mon-app:1.2.0
docker pull 123456789.dkr.ecr.eu-west-1.amazonaws.com/mon-app:1.2.0

# Forcer le repull (même si déjà local)
docker pull --no-cache nginx:latest
```

---

## Push

```bash
# 1. Taguer avec le chemin du registry
docker tag mon-app:1.0 ghcr.io/mohamedmahtali/mon-app:1.0

# 2. Se connecter
docker login ghcr.io

# 3. Pousser
docker push ghcr.io/mohamedmahtali/mon-app:1.0

# Pousser plusieurs tags
docker push ghcr.io/mohamedmahtali/mon-app:1.0
docker push ghcr.io/mohamedmahtali/mon-app:latest
```

---

## Optimisation des transferts

```bash
# Voir quels layers sont uploadés vs mis en cache
docker push ghcr.io/org/app:1.0
# Layer already exists → déjà présent dans le registry
# Pushed → nouveau layer uploadé
```

> [!tip]
> Les layers déjà présents dans le registry ne sont pas retransférés. Si tu partages la même image de base entre services, les layers communs ne sont uploadés qu'une fois.
