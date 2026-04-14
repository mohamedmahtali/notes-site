---
title: Squash
tags:
  - intermediate
---

# Squash

## Parent
- [[Rebase]]

## Concepts liés
- [[Rebase]]
- [[Interactive rebase]]
- [[Rewrite history]]
- [[Pull request]]

---

## Définition

Le squash consiste à **fusionner plusieurs commits en un seul**. Cela produit un historique plus propre sur `main` en remplaçant une série de commits de développement (WIP, fix typo, add test) par un commit unique et cohérent.

---

## Méthodes

### 1. Via le rebase interactif

```bash
git rebase -i HEAD~3

# Dans l'éditeur :
pick   a3f2c1e feat: add user auth
squash b7d4e2a wip: almost working
squash c1f9a3b fix: handle edge case
# → demande un nouveau message de commit
```

### 2. Via GitHub (option "Squash and merge")

Sur GitHub, au moment du merge d'une PR :
- **Merge commit** : conserve tous les commits + 1 commit de merge
- **Squash and merge** : ✅ tous les commits → 1 seul commit dans `main`
- **Rebase and merge** : rejoue les commits sans commit de merge

### 3. En ligne de commande

```bash
# Squash des 3 derniers commits sans rebase interactif
git reset --soft HEAD~3
git commit -m "feat: add user authentication"
```

---

## Quand squasher ?

| Situation | Recommandation |
|---|---|
| Branch de feature | ✅ Squash before merge → 1 commit = 1 feature |
| Historique de debug | ✅ Squash les WIP/fix/typo |
| Commits importants à tracer | ❌ Garder séparés pour le blame |

> [!tip]
> Configurer GitHub pour "Squash and merge" par défaut sur les PRs de feature branches.
