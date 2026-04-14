---
title: Hotfix branch
tags:
  - intermediate
---

# Hotfix branch

## Parent
- [[Branch]]

## Concepts liés
- [[Branch]]
- [[Main branch]]
- [[Release branch]]
- [[Git flow]]

---

## Définition

Une hotfix branch est créée directement depuis `main` pour corriger un bug critique en production. C'est la seule branche qui ne part pas de `develop`. Elle doit être mergée **à la fois dans `main` et dans `develop`** pour que le fix ne soit pas perdu à la prochaine release.

---

## Pourquoi c'est important

> [!danger] Bug critique en production
> Pas le temps d'attendre la prochaine release. La hotfix branch permet d'injecter un correctif directement en production en quelques minutes, sans interférer avec le développement en cours sur `develop`.

---

## Workflow

```bash
# 1. Partir de main (état production)
git checkout main
git pull origin main
git checkout -b hotfix/1.2.1

# 2. Corriger le bug
# → modifier le code
git add .
git commit -m "fix: correct null pointer in payment processing"
git commit -m "chore: bump version to 1.2.1"

# 3. Merger dans main + tag
git checkout main
git merge --no-ff hotfix/1.2.1
git tag -a v1.2.1 -m "Hotfix: correct null pointer in payment"
git push origin main --tags

# 4. Merger dans develop (synchronisation critique !)
git checkout develop
git merge --no-ff hotfix/1.2.1
git push origin develop

# 5. Supprimer la hotfix branch
git branch -d hotfix/1.2.1
```

---

## Convention de nommage

```
hotfix/1.2.1
hotfix/fix-payment-null-pointer
hotfix/PROD-567-critical-auth-bypass
```

> [!warning] Merger dans develop aussi
> Oublier de merger le hotfix dans `develop` est une erreur classique. Le bug sera de retour à la prochaine release. Certaines équipes automatisent ce step via des scripts.
