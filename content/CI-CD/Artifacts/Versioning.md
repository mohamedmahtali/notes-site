---
title: Versioning
tags:
  - intermediate
---
# Versioning

---

## Définition

Le versioning des artefacts attribue un identifiant unique à chaque build pour permettre le tracking, le [[Rollback]], et la traçabilité. Les stratégies courantes : SemVer, SHA du [[Commit]], numéro de build séquentiel.

---

## Stratégies

```bash
# SemVer (1.2.3) — pour les releases publiques
npm version patch    # 1.2.3 → 1.2.4
npm version minor    # 1.2.3 → 1.3.0
npm version major    # 1.2.3 → 2.0.0

# SHA du commit — pour le tracking précis
docker tag myapp:latest myapp:$(git rev-parse --short HEAD)

# Numéro de build — pour les pipelines CI
docker tag myapp myapp:${BUILD_NUMBER}

# Combiné (recommandé)
VERSION="1.2.3-${GITHUB_SHA:0:8}"
docker tag myapp myapp:${VERSION}
```

---

## Versioning sémantique automatique

```bash
# semantic-release analyse les commits Conventional Commits
# feat: → minor bump (1.0.0 → 1.1.0)
# fix:  → patch bump (1.0.0 → 1.0.1)
# BREAKING CHANGE: → major bump (1.0.0 → 2.0.0)
npx semantic-release
```

---

## Tags Git

```bash
git tag -a v1.2.3 -m "Release 1.2.3"
git push origin v1.2.3

# Pipeline déclenché par un tag
on:
  push:
    tags: ['v*']
```

---

> [!tip]
> Utiliser le SHA court du commit pour les images [[Docker]] internes (non-publiques). Utiliser SemVer pour les [[Package]] publics et les [[Releases]].
