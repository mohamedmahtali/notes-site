---
title: Image tagging
tags:
  - beginner
---

# Image tagging

## Parent
- [[Images]]

---

## Définition

Le tag d'une image est le suffixe après `:` dans le nom (`mon-app:1.2.0`). Il identifie une version spécifique d'une image. Si omis, Docker utilise `latest` par convention — mais `latest` n'est qu'un tag comme un autre, pas automatiquement la dernière version.

---

## Commandes

```bash
# Tagger une image existante
docker tag mon-app:latest registry.example.com/mon-app:1.2.0
docker tag mon-app:latest registry.example.com/mon-app:latest

# Tagger lors du build
docker build -t mon-app:1.2.0 -t mon-app:latest .

# Tagger avec le commit Git
docker build -t mon-app:$(git rev-parse --short HEAD) .
```

---

## Convention de tagging

```
mon-app:latest         ← tag mutable (déconseillé en prod)
mon-app:1.2.0          ← version sémantique (stable)
mon-app:1.2            ← minor (pointe vers le dernier patch)
mon-app:1              ← major (pointe vers le dernier minor)
mon-app:20240115-abc1234  ← date + commit hash
mon-app:main-abc1234   ← branche + commit
```

---

## En CI/CD

```bash
VERSION=$(git describe --tags --always)
COMMIT=$(git rev-parse --short HEAD)

docker build   -t ghcr.io/org/app:${VERSION}   -t ghcr.io/org/app:${COMMIT}   -t ghcr.io/org/app:latest   .
```

> [!warning]
> Ne jamais déployer `:latest` en production — le tag peut pointer vers une image différente selon l'hôte. Utiliser un tag de version ou de commit immuable.
