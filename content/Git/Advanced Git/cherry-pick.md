---
title: cherry-pick
tags:
  - advanced
---

# cherry-pick

---

## Définition

`git cherry-pick` copie un ou plusieurs [[Commit]] spécifiques d'une branche vers une autre, en créant de nouveaux commits avec le même diff mais un nouveau hash SHA-1. C'est un "couper-coller" de commits.

---

## Pourquoi c'est important

> [!tip] Portage ciblé de correctifs
> Idéal pour appliquer un hotfix sur plusieurs versions maintenues en parallèle, ou pour récupérer un commit utile sans merger toute une branche.

---

## Commandes

```bash
# Cherry-pick d'un commit unique
git cherry-pick abc1234

# Cherry-pick avec message original
git cherry-pick abc1234 --no-commit   # applique sans committer
git cherry-pick abc1234 -e            # éditer le message

# Cherry-pick d'une plage de commits
git cherry-pick abc1234..def5678      # de abc (exclu) à def (inclus)
git cherry-pick abc1234^..def5678     # de abc (inclus) à def (inclus)

# Cherry-pick de plusieurs commits non consécutifs
git cherry-pick abc1234 def5678 ghi9012
```

---

## Exemple – porter un fix sur plusieurs branches

```bash
# Bug fix commité sur develop : commit abc1234
# → Porter sur main (v2) et release/1.x (v1)

git checkout main
git cherry-pick abc1234
git push origin main

git checkout release/1.x
git cherry-pick abc1234
git push origin release/1.x
```

---

## Gérer les conflits

```bash
git cherry-pick abc1234
# CONFLICT (content): Merge conflict in src/api.js

# Résoudre le conflit
git add src/api.js
git cherry-pick --continue

# Ou annuler
git cherry-pick --abort
```

> [!warning]
> Cherry-pick duplique les commits (nouveau hash). Si la branche source est plus tard mergée, [[Git]] peut voir les mêmes changements deux fois. Préférer le [[Merge]] ou le [[Rebase]] quand c'est possible.
