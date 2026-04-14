---
title: Containerize
tags:
  - intermediate
---
# Containerize

## Parent
- [[Build stage]]

---

## Définition

Containeriser = construire une image Docker à partir du code et la pousser dans un registry. L'image résultante est l'artefact qui sera déployé dans les environnements suivants.

---

## Pipeline de containerisation

```yaml
- name: Login to registry
  uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}

- name: Build and push image
  uses: docker/build-push-action@v5
  with:
    context: .
    push: ${{ github.event_name != 'pull_request' }}
    tags: |
      ghcr.io/${{ github.repository }}:latest
      ghcr.io/${{ github.repository }}:${{ github.sha }}
    labels: |
      org.opencontainers.image.revision=${{ github.sha }}
```

---

## Multi-platform

```yaml
- name: Set up QEMU
  uses: docker/setup-qemu-action@v3

- name: Build multi-platform
  uses: docker/build-push-action@v5
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: myapp:latest
```

---

> [!tip]
> Toujours taguer avec le SHA du commit en plus de `latest`. Ça permet de rollback facilement vers une version précise.
