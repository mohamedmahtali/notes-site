---
title: Git stash
tags:
  - intermediate
---
# Git stash

---

## Définition

`git stash` met de côté temporairement les modifications non committées (working directory et [[Staging]] area) dans une pile locale. Le working directory revient à l'état du dernier [[Commit]]. Les modifications sont récupérables à tout moment.

---

## Pourquoi c'est important

> [!tip] Changer de contexte sans créer de commit
> Tu es au milieu d'une feature quand une urgence arrive sur main. Le stash te permet de "mettre en pause" ton travail proprement, sans créer un commit de WIP.

---

## Commandes essentielles

```bash
# Mettre en stash (avec message)
git stash push -m "feat: formulaire contact en cours"

# Lister les stash
git stash list
# stash@{0}: feat: formulaire contact en cours
# stash@{1}: fix: correction CSS temporaire

# Restaurer le dernier stash (et le supprimer)
git stash pop

# Restaurer sans supprimer
git stash apply stash@{0}

# Supprimer un stash
git stash drop stash@{0}

# Vider toute la pile
git stash clear

# Inclure les fichiers non-trackés
git stash push -u -m "avec nouveaux fichiers"
```

---

## Flux typique

```bash
# 1. En cours de travail sur feature
git stash push -m "feat: dashboard WIP"

# 2. Hotfix urgent
git checkout main
git checkout -b hotfix/1.2.1
# → corriger, committer, merger

# 3. Revenir sur la feature
git checkout feature/dashboard
git stash pop
```

---

> [!note]
> Le stash est **local uniquement** — il n'est pas pushé. Ne pas l'utiliser comme sauvegarde long terme. Créer une branche `draft/` pour ça.
