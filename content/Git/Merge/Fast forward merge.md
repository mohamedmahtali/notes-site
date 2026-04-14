---
title: Fast forward merge
tags:
  - beginner
---

# Fast forward merge

## Parent
- [[Merge]]

## Concepts liés
- [[Merge]]
- [[Three way merge]]
- [[Merge conflicts]]
- [[Rebase]]

---

## Définition

Un merge fast-forward se produit quand la branche cible (`main`) n'a pas avancé depuis la création de la branche source. Git peut simplement **déplacer le pointeur** de `main` vers le dernier commit de la branche — aucun commit de merge n'est créé.

---

## Schéma

```
Avant :
main:    A → B → C
                  ↘
feature:           D → E → F (HEAD)

Après fast-forward merge :
main:    A → B → C → D → E → F (HEAD, main)
```

Il n'y a pas de "fourche" dans l'historique — c'est une ligne droite.

---

## Quand ça se produit

```bash
git checkout main
git merge feature/login
# Fast-forward
# → Pas de commit de merge créé
```

Git choisit automatiquement le fast-forward si la condition est remplie (main n'a pas bougé).

---

## Forcer ou interdire le fast-forward

```bash
# Interdire le fast-forward → toujours créer un commit de merge
git merge --no-ff feature/login

# Forcer le fast-forward (échoue si pas possible)
git merge --ff-only feature/login
```

---

## Fast-forward vs Three-way merge

| Critère | Fast-forward | Three-way |
|---|---|---|
| Commit de merge | ❌ Non | ✅ Oui |
| Historique | Linéaire | Avec branches visibles |
| Quand possible | main n'a pas avancé | main a avancé |

> [!tip] Choix selon le workflow
> **GitHub flow** préfère souvent `--no-ff` pour garder la trace des PRs dans le log. **Trunk-based development** préfère le fast-forward pour un historique linéaire.
