---
title: Interactive rebase
tags:
  - advanced
---

# Interactive rebase

---

## Définition

Le [[Rebase]] interactif (`git rebase -i`) permet de réécrire l'historique d'une branche [[Commit]] par commit : modifier des messages, fusionner des commits, réordonner, supprimer ou diviser des commits. C'est l'outil de nettoyage d'historique le plus puissant de [[Git]].

---

## Pourquoi c'est important

> [!warning] Jamais sur des commits déjà poussés sur main
> Le rebase interactif réécrit les hashes SHA-1. L'utiliser sur une branche partagée casse l'historique des autres.

> [!tip] Nettoyer avant de [[Merge]]
> Un historique propre sur la PR ([[Squash]] des "WIP", correction des typos) facilite les reviews et rend le `git log` de `main` lisible.

---

## Commandes

```bash
# Rebase interactif sur les 4 derniers commits
git rebase -i HEAD~4

# Rebase interactif depuis la divergence avec main
git rebase -i main
```

---

## Actions disponibles dans l'éditeur

```
pick   a3f2c1e feat: add login page
pick   b7d4e2a wip: styling
pick   c1f9a3b fix typo
pick   d4e5f6a feat: add validation

# Commandes :
# p, pick   → garder le commit tel quel
# r, reword → garder mais modifier le message
# e, edit   → modifier le contenu du commit
# s, squash → fusionner avec le commit précédent (garde les 2 messages)
# f, fixup  → fusionner avec le commit précédent (supprime ce message)
# d, drop   → supprimer ce commit
```

---

## Exemple – nettoyer une branche avant PR

```
Avant :
- feat: add login page
- wip: not working
- fix: really fix it now
- fix typo
- test: add tests for login

Après rebase -i (squash/fixup) :
- feat: add login page with validation and tests
```

```bash
git rebase -i HEAD~5

# Dans l'éditeur :
pick   a3f2c1e feat: add login page
fixup  b7d4e2a wip: not working
fixup  c1f9a3b fix: really fix it now
fixup  d4e5f6a fix typo
fixup  e7b8c9d test: add tests for login

# → résultat : 1 seul commit propre
```
