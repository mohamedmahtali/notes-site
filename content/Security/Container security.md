---
title: Container security
tags:
  - security
  - intermediate
---

# Container security

## Définition

La sécurité des conteneurs couvre les pratiques de durcissement des images, d'isolation des processus et de protection du runtime pour minimiser la surface d'attaque dans les environnements conteneurisés.

> [!tip] Pourquoi c'est important
> Les conteneurs partagent le [[Kernel]] de l'hôte. Une mauvaise configuration peut permettre une évasion de conteneur (container escape) compromettant tout le nœud.

## Bonnes pratiques

```dockerfile
# Image minimale
FROM alpine:3.18

# Utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Read-only filesystem
# (via docker run --read-only)

# Pas de capabilities inutiles
# (via docker run --cap-drop ALL --cap-add NET_BIND_SERVICE)
```

## Scanner une image

```bash
# Trivy (scanner de vulnérabilités)
trivy image nginx:latest

# Grype
grype nginx:latest

# Docker Scout
docker scout cves nginx:latest
```

## Liens

- [[AppArmor]]
- [[Seccomp]]
- [[Namespace isolation]]
- [[Runtime security]]
- [[Image scanning]]
