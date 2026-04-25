---
title: Feature branch
tags:
  - beginner
---

# Feature branch

---

## Définition

Une feature [[Branch]] est une branche courte créée pour développer une fonctionnalité spécifique en isolation. Elle diverge de `main`, accueille les [[Commit]] de la feature, puis est mergée via une [[Pull request]] avant d'être supprimée.

---

## Convention de nommage

```bash
feature/nom-de-la-fonctionnalite
feature/ajout-authentification
feature/dashboard-analytics
feat/user-profile-edit

# Avec ticket
feature/JIRA-142-login-page
feature/GH-87-dark-mode
```

---

## Workflow

```bash
# 1. Créer depuis main à jour
git checkout main
git pull origin main
git checkout -b feature/ajout-authentification

# 2. Développer
git add .
git commit -m "feat(auth): add JWT token generation"
git commit -m "feat(auth): add login endpoint"
git commit -m "test(auth): add unit tests for JWT"

# 3. Pousser et ouvrir une PR
git push -u origin feature/ajout-authentification
# → Ouvrir la PR sur GitHub

# 4. Après merge
git checkout main
git pull origin main
git branch -d feature/ajout-authentification
git push origin --delete feature/ajout-authentification
```

---

## Bonnes pratiques

> [!tip]
> - **Courte durée** : idéalement < 2-3 jours. Plus elle dure, plus le [[Merge]] est difficile.
> - **Focalisée** : 1 branche = 1 feature. Ne pas mélanger plusieurs changements.
> - **Nommage descriptif** : lisible dans `git branch -a` et dans les notifications CI.

> [!warning]
> Puller régulièrement `main` dans ta feature branch pour rester synchronisé :
> ```[[Bash]]
> [[Git]] fetch origin
> git [[Rebase]] origin/main
> ```
