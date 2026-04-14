---
title: Build stage
tags:
  - intermediate
---
# Build stage

## Parent
- [[Pipeline]]

## Enfants
- [[Compile]]
- [[Containerize]]
- [[Package]]

---

## Définition

Le build stage compile le code source, résout les dépendances, et produit un artefact déployable (binaire, image Docker, package). C'est la première étape d'un pipeline — si le build échoue, rien d'autre ne s'exécute.

---

## Pourquoi c'est important

> [!tip] Artefact immuable
> Le build stage produit un artefact unique (identifié par un SHA ou tag de version) qui sera promu à travers les environnements. Le même artefact va en staging et en prod — pas de rebuild entre les environnements.

---

## Exemple GitHub Actions

```yaml
build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: |
          myregistry/myapp:latest
          myregistry/myapp:${{ github.sha }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
```

---

> [!note]
> Voir [[Compile]] pour les langages compilés, [[Containerize]] pour Docker, [[Package]] pour npm/pip/maven.
