---
title: Three way merge
tags:
  - intermediate
---

# Three way merge

## Parent
- [[Merge]]

## Concepts liés
- [[Merge]]
- [[Fast forward merge]]
- [[Merge conflicts]]

---

## Définition

Un merge à trois points (three-way merge) est utilisé quand les deux branches ont avancé depuis leur point de divergence. Git compare **trois commits** : l'ancêtre commun, le dernier commit de la branche source, et le dernier commit de la branche cible — puis crée un nouveau **commit de merge**.

---

## Schéma

```
Ancêtre commun :    C
main :              C → D → E
feature :           C → F → G

Résultat :
main :    C → D → E → M (commit de merge)
                  ↗
feature : C → F → G
```

Le commit M a deux parents : E et G.

---

## Algorithme

```
1. Trouver l'ancêtre commun (C)
2. Calculer les différences : C→E (main) et C→G (feature)
3. Pour chaque fichier :
   - Si modifié dans une seule branche → appliquer automatiquement
   - Si modifié dans les deux → conflit à résoudre manuellement
4. Créer le commit de merge M
```

---

## Exemple

```bash
# main a avancé depuis la création de feature/auth
git checkout main
git merge feature/auth

# Si pas de conflit :
# → Merge commit créé automatiquement
# "Merge branch 'feature/auth' into main"

# Si conflit :
# CONFLICT (content): Merge conflict in src/config.js
# → Résoudre, git add, git commit
```

---

## Inspecter un commit de merge

```bash
# Voir les deux parents du commit de merge
git log --oneline --graph -5
# *   a3f2c1e Merge branch 'feature/auth'
# |# | * b7d4e2a feat: add JWT middleware
# * | c1f9a3b chore: update deps
# |/
# * d4e5f6a feat: initial project setup
```
