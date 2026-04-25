---
title: Docker registry
tags:
  - intermediate
---

# Docker registry

---

## Définition

Un registry [[Docker]] est un serveur de stockage et de distribution d'images Docker. Il fonctionne comme un dépôt de [[Package]] mais pour des images de conteneurs. Les images y sont poussées après le build et tirées lors du déploiement.

---

## Registries populaires

| Registry | Type | Avantages |
|---|---|---|
| [[Docker hub\|Docker Hub]] | Public/privé | Le plus connu, images officielles |
| GitHub Container Registry (ghcr.io) | Public/privé | Intégré à GitHub |
| [[AWS]] ECR | Privé [[Cloud]] | Intégré à AWS [[IAM]] |
| GCR (gcr.io) | Privé cloud | Intégré à GCP |
| [[Azure]] Container Registry | Privé cloud | Intégré à Azure |
| Harbor | Self-hosted | Open source, features avancées |

---

## Commandes

```bash
# Se connecter
docker login docker.io
docker login ghcr.io -u USERNAME --password-stdin <<< $GITHUB_TOKEN

# Tagger une image pour un registry
docker tag mon-app:1.0 ghcr.io/org/mon-app:1.0

# Pousser
docker push ghcr.io/org/mon-app:1.0

# Tirer
docker pull ghcr.io/org/mon-app:1.0
```

---

## En CI/CD (GitHub Actions)

```yaml
- name: Login to GHCR
  uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}

- name: Build and push
  uses: docker/build-push-action@v5
  with:
    push: true
    tags: ghcr.io/${{ github.repository }}:latest
```
