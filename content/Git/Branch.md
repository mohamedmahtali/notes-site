---
title: Branch
tags:
  - beginner
---

# Branch

---

## Définition

Une branche [[Git]] est un **pointeur léger vers un [[Commit]]**. Elle permet de travailler sur une fonctionnalité, un bug ou une expérimentation en **isolation**, sans affecter le reste du code.

Par défaut, un dépôt Git contient une branche principale appelée `main` (ou `master` dans les anciens projets).

---

## Pourquoi c'est important

> [!tip] Travailler en isolation
> Les branches permettent à plusieurs développeurs de travailler en parallèle sans se bloquer mutuellement. C'est la base de toute collaboration Git efficace.

- **Isolation** : les modifications d'une branche n'affectent pas les autres
- **Expérimentation** : tester une idée sans risquer le code stable
- **Déclencheur CI/CD** : chaque branche peut avoir son propre [[Pipeline]]

---

## Commandes essentielles

```bash
# Lister les branches locales
git branch

# Lister toutes les branches (locales + distantes)
git branch -a

# Créer une nouvelle branche
git branch ma-feature

# Créer et basculer immédiatement
git checkout -b ma-feature
# ou (syntaxe moderne)
git switch -c ma-feature

# Basculer sur une branche existante
git checkout main
git switch main

# Supprimer une branche locale (après merge)
git branch -d ma-feature

# Pousser une branche sur le dépôt distant
git push origin ma-feature

# Supprimer une branche distante
git push origin --delete ma-feature
```

---

## Types de branches

| Branche | Rôle | Durée de vie |
|---|---|---|
| [[Main branch\|main]] | Code stable en production | Permanente |
| [[Feature branch\|feature/*]] | Nouvelle fonctionnalité | Courte |
| [[Hotfix branch\|hotfix/*]] | Correction urgente en production | Très courte |
| [[Release branch\|release/*]] | Préparation d'une release | Moyenne |

---

## Exemple

```bash
# Partir de main à jour
git checkout main
git pull origin main

# Créer une branche pour une feature
git checkout -b feature/ajout-authentification

# Travailler, committer...
git add .
git commit -m "feat(auth): add user login endpoint"

# Pousser et ouvrir une Pull Request
git push origin feature/ajout-authentification
```

> [!note] Convention de nommage
> Adopte un préfixe cohérent : `feature/`, `fix/`, `hotfix/`, `release/`. C'est lisible dans le `git log` et compatible avec la plupart des [[Workflows]] CI/CD.

---

## Visualiser les branches

```bash
git log --oneline --graph --all
```

```
* a3f2c1e (HEAD -> feature/auth) feat: add login
* b7d4e2a (main) chore: update dependencies
*   c1f9a3b Merge pull request #12
|\
| * d4e5f6a fix: handle null user
|/
* e7b8c9d feat: initial project setup
```
