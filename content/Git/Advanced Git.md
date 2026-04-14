---
title: Advanced Git
tags:
  - intermediate
---
# Advanced Git

## Parent
- [[Git]]

## Enfants
- [[cherry-pick]]
- [[bisect]]
- [[reflog]]
- [[reset]]

## Concepts liés
- [[cherry-pick]]
- [[bisect]]
- [[reflog]]
- [[reset]]

---

## Définition

Au-delà des commandes quotidiennes (`add`, `commit`, `push`), Git offre des outils puissants pour manipuler l'historique, déboguer, et récupérer des états perdus. Ces commandes avancées sont utilisées pour résoudre des situations complexes.

---

## Outils avancés

| Commande | Usage |
|---|---|
| [[cherry-pick]] | Copier un commit précis vers une autre branche |
| [[bisect]] | Trouver le commit qui a introduit un bug (recherche binaire) |
| [[reflog]] | Journal de tous les mouvements de HEAD — filet de sécurité |
| [[reset]] | Déplacer HEAD et modifier staging/working dir |

---

## Quand les utiliser

> [!tip] cherry-pick
> Porter un correctif sur plusieurs branches de release sans merger toute une branche.

> [!tip] bisect
> Identifier en quelques minutes quel commit parmi 1000 a cassé un comportement.

> [!tip] reflog
> Récupérer des commits perdus après un `reset --hard` ou un rebase raté.

> [!tip] reset
> Défaire des commits locaux, désindexer des fichiers, nettoyer le working directory.

---

## Commandes de diagnostic

```bash
# Voir tout ce qui s'est passé sur HEAD (même les resets)
git reflog

# Trouver un bug par recherche binaire
git bisect start
git bisect bad HEAD
git bisect good v1.0.0

# Copier un commit sur la branche courante
git cherry-pick abc1234

# Revenir N commits en arrière (garder les modifs)
git reset --soft HEAD~N
```

---

> [!warning]
> Ces commandes modifient ou réécrivent l'historique. Toujours s'assurer de travailler sur des commits **non encore poussés** sur des branches partagées avant d'utiliser `reset --hard` ou `rebase -i`.
