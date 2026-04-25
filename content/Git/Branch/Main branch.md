---
title: Main branch
tags:
  - beginner
---

# Main branch

---

## Définition

`main` (anciennement `master`) est la branche principale d'un dépôt [[Git]]. Dans tous les [[Workflows]] modernes, elle représente le code **stable et déployable** en production. C'est la source de vérité du projet.

---

## Règle fondamentale

> [!warning] main doit toujours être déployable
> Aucun [[Commit]] cassé, aucun test en échec. Si `main` est cassée, c'est une urgence. Tout le workflow CI/CD repose sur cette invariant.

---

## Protection de main

```
GitHub → Settings → Branches → Add rule pour "main" :

☑ Require pull request before merging
  ☑ Require 1 approval minimum
☑ Require status checks to pass (CI)
☑ Do not allow force pushes
☑ Do not allow deletions
```

---

## Commandes courantes

```bash
# Récupérer les dernières modifications
git checkout main
git pull origin main

# Voir les commits récents
git log --oneline -10

# Voir qui a modifié un fichier
git log --oneline -- src/api.js

# Créer une branche depuis main à jour
git checkout -b feature/ma-feature
```

---

## Historical note

```bash
# Renommer master en main (migration)
git branch -m master main
git push -u origin main
git push origin --delete master

# Configurer main comme défaut pour les nouveaux dépôts
git config --global init.defaultBranch main
```
