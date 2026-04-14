---
title: Git tags
tags:
  - intermediate
---
# Git tags

## Parent
- [[Git]]

## Enfants
- [[Lightweight tags]]
- [[Annotated tags]]

## Concepts liés
- [[Lightweight tags]]
- [[Annotated tags]]
- [[Versioning]]

---

## Définition

Un tag Git est un pointeur nommé et **immuable** vers un commit spécifique. Contrairement aux branches qui avancent à chaque commit, un tag reste fixé. Les tags servent principalement à marquer les **versions et releases** d'un projet.

---

## Types de tags

| Type | Commande | Usage |
|---|---|---|
| [[Annotated tags\|Annoté]] | `git tag -a v1.0.0 -m "..."` | Releases officielles |
| [[Lightweight tags\|Léger]] | `git tag v1.0.0-rc1` | Marquages temporaires |

---

## Commandes essentielles

```bash
# Créer un tag annoté (recommandé pour les releases)
git tag -a v1.2.0 -m "Release v1.2.0 – ajout authentification"

# Lister les tags
git tag -l
git tag -l "v1.*"   # filtrer par pattern

# Voir les détails d'un tag
git show v1.2.0

# Pousser un tag vers le remote
git push origin v1.2.0

# Pousser tous les tags
git push origin --tags

# Supprimer un tag
git tag -d v1.2.0-beta         # local
git push origin --delete v1.2.0-beta  # distant

# Générer une version basée sur le dernier tag
git describe --tags
# v1.2.0-3-gabc1234
```

---

## Versioning sémantique

```
v<MAJOR>.<MINOR>.<PATCH>[-pre-release]

v2.0.0      → breaking change
v1.3.0      → nouvelle fonctionnalité rétrocompatible
v1.2.1      → bug fix
v1.3.0-rc1  → release candidate
```

---

## Tags en CI/CD

```yaml
# GitHub Actions – déclencher un deploy sur tag
on:
  push:
    tags:
      - 'v*'
```

> [!tip]
> Utilise toujours les [[Annotated tags|tags annotés]] pour les releases publiées — ils contiennent les métadonnées (auteur, date, message) utilisées par les outils de changelog et de release automatique.
