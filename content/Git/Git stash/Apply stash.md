---
title: Apply stash
tags:
  - intermediate
---

# Apply stash

---

## Définition

`git stash apply` restaure le contenu d'un stash dans le working directory **sans le supprimer** de la pile. Contrairement à `git stash pop`, le stash reste disponible après application.

---

## Pourquoi c'est important

> [!tip] Appliquer sans supprimer
> Utile pour appliquer le même stash sur plusieurs branches, ou pour tester avant de confirmer qu'on peut supprimer le stash.

---

## Commandes

```bash
# Appliquer le stash le plus récent (stash@{0})
git stash apply

# Appliquer un stash spécifique
git stash apply stash@{2}

# Après vérification, supprimer manuellement
git stash drop stash@{2}

# Voir la liste des stash disponibles
git stash list
```

---

## apply vs pop

| Commande | Comportement |
|---|---|
| `git stash apply` | Restaure le stash, **le conserve** dans la pile |
| `git stash pop` | Restaure le stash **et le supprime** de la pile |

---

## Exemple

```bash
git stash list
# stash@{0}: WIP: feature/auth
# stash@{1}: fix: CSS temporaire

# Appliquer le stash CSS sur deux branches
git checkout feature/ui
git stash apply stash@{1}
# → tester...

git checkout feature/dark-mode
git stash apply stash@{1}
# → tester...

# Une fois satisfait, supprimer le stash
git stash drop stash@{1}
```

> [!warning] Conflits possibles
> Si le working directory contient des modifications, `git stash apply` peut générer des conflits à résoudre manuellement.
