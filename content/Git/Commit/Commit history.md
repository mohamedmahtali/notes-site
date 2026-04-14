---
title: Commit history
tags:
  - beginner
---

# Commit history

## Parent
- [[Commit]]

## Concepts liés
- [[Commit]]
- [[Commit message]]
- [[Amend]]
- [[Rebase]]

---

## Définition

L'historique des commits (`git log`) est la liste chronologique de tous les commits d'un dépôt. Chaque entrée contient : le hash SHA-1, l'auteur, la date, et le message. C'est la mémoire du projet.

---

## Pourquoi c'est important

> [!tip] Débogage et traçabilité
> Un bon historique permet de retrouver exactement quand et pourquoi un bug a été introduit. C'est aussi la base de `git bisect` et des `git blame`.

---

## Commandes essentielles

```bash
# Vue simple et lisible
git log --oneline

# Avec graphe des branches
git log --oneline --graph --all

# Détail complet d'un commit
git show abc1234

# Historique d'un fichier spécifique
git log --oneline -- src/api.js

# Commits d'un auteur
git log --author="Mohamed"

# Entre deux dates
git log --since="2024-01-01" --until="2024-06-30" --oneline

# Chercher dans les messages de commit
git log --grep="fix" --oneline

# Voir ce qu'un commit a changé
git show abc1234 --stat
```

---

## Lire le log

```
a3f2c1e (HEAD -> feature/auth) feat(auth): add JWT middleware
b7d4e2a (origin/main, main) fix: handle null response
c1f9a3b Merge pull request #12 from feature/ui
```

| Élément | Signification |
|---|---|
| `HEAD` | Position actuelle dans l'historique |
| `origin/main` | État de la branche distante |
| Hash court (`a3f2c1e`) | Identifiant unique du commit |

---

## Exemple – retrouver un bug

```bash
# Chercher quand une fonction a changé
git log -S "calculateTimeout" --oneline
# b7d4e2a fix: increase timeout for slow networks

# Voir le diff de ce commit
git show b7d4e2a
```
