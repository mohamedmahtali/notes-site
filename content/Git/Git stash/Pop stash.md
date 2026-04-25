---
title: Pop stash
tags:
  - intermediate
---

# Pop stash

---

## Définition

`git stash pop` est la commande la plus courante pour restaurer un stash : elle applique le stash le plus récent (ou un stash ciblé) **et le retire** immédiatement de la pile. C'est l'équivalent d'un `apply` + `drop` en une seule opération.

---

## Commandes

```bash
# Pop le stash le plus récent
git stash pop

# Pop un stash spécifique
git stash pop stash@{1}
```

---

## Exemple

```bash
# Revenir sur sa branche après le hotfix
git checkout feature/contact-form
git stash pop
# → les modifications sont de retour dans le working directory
# → le stash est supprimé de la liste
```

---

## Gérer les conflits au pop

```bash
git stash pop
# CONFLICT (content): Merge conflict in src/config.js

# Résoudre le conflit dans le fichier, puis :
git add src/config.js
# Note : git stash pop ne crée PAS de commit automatiquement
# Le stash est déjà retiré de la pile même en cas de conflit
```

> [!warning]
> En cas de conflit, `pop` retire quand même le stash de la pile. Si tu n'arrives pas à résoudre, utilise `git stash apply` + `git stash drop` manuellement pour garder le contrôle.
