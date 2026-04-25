---
title: Update submodule
tags:
  - advanced
---

# Update submodule

---

## Définition

Mettre à jour un sous-module signifie pointer le dépôt parent vers un [[Commit]] plus récent du sous-module. Le sous-module est un dépôt [[Git]] indépendant : il faut explicitement aller y puller les nouveautés.

---

## Commandes

```bash
# Mettre à jour tous les sous-modules vers leur remote
git submodule update --remote

# Mettre à jour un sous-module spécifique
git submodule update --remote libs/library

# Pull récursif (sous-modules de sous-modules)
git submodule update --init --recursive --remote

# Voir les différences de version des sous-modules
git submodule status
```

---

## Workflow

```bash
# 1. Aller dans le sous-module et puller
cd libs/library
git pull origin main
cd ../..

# 2. Le dépôt parent voit maintenant une modification
git status
# modified: libs/library (new commits)

# 3. Committer le nouveau pointeur
git add libs/library
git commit -m "chore: update shared-utils to v2.3.1"
git push
```

> [!tip]
> Chaque collaborateur doit lancer `git submodule update --init --recursive` après un `git pull` qui change les pointeurs de sous-[[Modules]].
