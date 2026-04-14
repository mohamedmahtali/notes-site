---
title: Release branch
tags:
  - intermediate
---

# Release branch

## Parent
- [[Branch]]

## Concepts liés
- [[Branch]]
- [[Main branch]]
- [[Hotfix branch]]
- [[Git flow]]

---

## Définition

Une release branch est une branche créée à partir de `develop` (dans Git flow) ou `main` pour préparer une release. Elle accueille uniquement des corrections de bugs, la mise à jour des numéros de version, et la documentation — aucune nouvelle feature.

---

## Workflow (Git flow)

```bash
# 1. Créer la release branch depuis develop
git checkout develop
git checkout -b release/1.3.0

# 2. Activités sur la release branch
# - Correction de bugs mineurs découverts en QA
# - Bump de version
echo "1.3.0" > VERSION
git commit -m "chore: bump version to 1.3.0"

# 3. Merger dans main → deploy en production
git checkout main
git merge --no-ff release/1.3.0
git tag -a v1.3.0 -m "Release 1.3.0"

# 4. Merger dans develop pour garder les corrections
git checkout develop
git merge --no-ff release/1.3.0

# 5. Supprimer la release branch
git branch -d release/1.3.0
```

---

## Contenu d'une release branch

| Autorisé | Interdit |
|---|---|
| Corrections de bugs QA | Nouvelles fonctionnalités |
| Bump de version | Refactoring |
| Mise à jour CHANGELOG | Changements de dépendances |
| Documentation | Toute autre modification |

> [!note]
> Les release branches n'existent que dans Git flow. Dans GitHub flow et TBD, on déploie directement depuis `main`.
