---
title: mixed
tags:
  - advanced
---

# mixed

---

## Définition

`git reset --mixed` (mode par défaut) déplace HEAD et réinitialise le [[Staging]] area, mais **laisse le working directory intact**. Les modifications des [[Commit]] annulés reviennent à l'état "modifié non-stagé".

---

## Comportement

```
Avant :
  Working dir : [A]  Staging : [A]  HEAD → commit C

git reset HEAD~2   (ou --mixed)

Après :
  Working dir : [A]  Staging : []  HEAD → commit A
  (les modifs de B et C sont dans le working dir, non stagées)
```

---

## Cas d'usage

```bash
# Désindexer tous les fichiers stagés
git reset HEAD
# ou
git reset

# Annuler un commit et choisir manuellement ce qu'on recommit
git reset HEAD~1
git status
# → on voit les modifications
git add src/feature.js   # indexer seulement ce qu'on veut
git commit -m "feat: version propre"
```

> [!note]
> C'est le mode par défaut de `git reset`. `git reset HEAD fichier.js` est la façon traditionnelle de désindexer un fichier (équivalent moderne : `git restore --staged fichier.js`).
