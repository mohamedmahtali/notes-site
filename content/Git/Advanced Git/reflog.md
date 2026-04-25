---
title: reflog
tags:
  - advanced
---

# reflog

---

## Définition

`git reflog` (reference log) est un journal local de tous les mouvements de HEAD : chaque checkout, [[Commit]], [[reset]], [[Merge]], [[Rebase]] y est enregistré. C'est le **filet de sécurité ultime** de [[Git]] — il permet de récupérer des commits "perdus" après un reset --[[hard]] ou un rebase mal tourné.

---

## Pourquoi c'est important

> [!tip] Rien n'est vraiment perdu dans Git
> Un commit existe dans les objets Git tant qu'il n'a pas été garbage collecté (~90 jours). Le reflog te donne son hash pour le récupérer.

---

## Commandes

```bash
# Voir le reflog de HEAD
git reflog

# Reflog d'une branche spécifique
git reflog show feature/auth

# Voir les N dernières entrées
git reflog -10
```

---

## Lire le reflog

```
a3f2c1e HEAD@{0}: commit: feat: add login
b7d4e2a HEAD@{1}: reset: moving to HEAD~2
c1f9a3b HEAD@{2}: commit: fix: handle null
d4e5f6a HEAD@{3}: commit: feat: add dashboard
e7b8c9d HEAD@{4}: checkout: moving from main to feature/auth
```

---

## Récupérer un commit perdu

```bash
# Après un reset --hard accidentel
git reset --hard HEAD~3   # Oups !

# Trouver le commit dans le reflog
git reflog
# a3f2c1e HEAD@{0}: reset: moving to HEAD~3
# d4e5f6a HEAD@{1}: commit: feat: the thing I lost

# Récupérer le commit
git checkout d4e5f6a      # inspecter en détached HEAD
git checkout -b recovery/lost-commits   # créer une branche pour sauvegarder

# Ou directement reset vers l'état d'avant
git reset --hard HEAD@{1}
```

> [!warning]
> Le reflog est **local uniquement** — il n'est pas pushé sur le remote. Si tu as perdu un commit sur une autre machine, il n'est pas dans ton reflog.
