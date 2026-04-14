---
title: Merge
tags:
  - intermediate
---
# Merge

## Parent
- [[Git]]

## Enfants
- [[Fast forward merge]]
- [[Three way merge]]
- [[Merge conflicts]]

## Concepts liés
- [[Fast forward merge]]
- [[Three way merge]]
- [[Merge conflicts]]
- [[Pull request]]

---

## Définition

`git merge` intègre les modifications d'une branche dans une autre. Selon si la branche cible a avancé ou non depuis la divergence, Git choisit automatiquement entre un [[Fast forward merge|fast-forward]] (sans commit de merge) ou un [[Three way merge|three-way merge]] (avec commit de merge).

---

## Types de merge

| Type | Quand | Résultat |
|---|---|---|
| [[Fast forward merge\|Fast-forward]] | main n'a pas avancé | Historique linéaire |
| [[Three way merge\|Three-way]] | Les deux branches ont avancé | Commit de merge créé |
| Conflictuel | Même zone modifiée des deux côtés | Résolution manuelle requise |

---

## Commandes

```bash
# Merger feature dans main
git checkout main
git merge feature/auth

# Forcer un commit de merge (même si fast-forward possible)
git merge --no-ff feature/auth

# Merger en squash (tous les commits → 1 seul, pas de commit de merge)
git merge --squash feature/auth
git commit -m "feat: add authentication"

# Annuler un merge en cours
git merge --abort

# Voir les branches déjà mergées dans main
git branch --merged main

# Voir les branches non encore mergées
git branch --no-merged main
```

---

## Résoudre un conflit

```bash
git merge feature/auth
# CONFLICT (content): Merge conflict in src/config.js

# Ouvrir le fichier, résoudre les marqueurs <<<<< / ===== / >>>>>
git add src/config.js
git commit -m "merge: resolve conflict on config timeout"
```

---

> [!tip]
> Voir [[Merge conflicts]] pour le détail complet de la résolution de conflits.
