---
title: reset
tags:
  - advanced
---

# reset

## Parent
- [[Advanced Git]]

## Enfants
- [[soft]]
- [[mixed]]
- [[hard]]

## Concepts liés
- [[Advanced Git]]
- [[reflog]]
- [[Amend]]

---

## Définition

`git reset` déplace le pointeur HEAD (et optionnellement la branche) vers un commit précédent. Selon le mode utilisé (`--soft`, `--mixed`, `--hard`), il affecte différemment le staging area et le working directory.

---

## Les trois modes en résumé

| Mode | HEAD | Index (staging) | Working directory |
|---|---|---|---|
| `--soft` | Déplacé | Inchangé | Inchangé |
| `--mixed` (défaut) | Déplacé | Réinitialisé | Inchangé |
| `--hard` | Déplacé | Réinitialisé | Réinitialisé |

---

## Commandes

```bash
# Défaire le dernier commit (garder les modifs en staging)
git reset --soft HEAD~1

# Défaire le dernier commit (garder les modifs non-stagées)
git reset HEAD~1       # --mixed par défaut

# Défaire le dernier commit et SUPPRIMER les modifications
git reset --hard HEAD~1   # ⚠️ irréversible sans reflog

# Revenir à un commit précis
git reset --hard abc1234

# Désindexer un fichier (retirer du staging)
git reset HEAD src/fichier.js
# ou (syntaxe moderne)
git restore --staged src/fichier.js
```

---

## Utilisation typique

```bash
# Défaire 3 commits mais garder le code pour les recommitter proprement
git reset --soft HEAD~3
git commit -m "feat: fonctionnalité complète et propre"
```

> [!warning] Uniquement sur des commits locaux
> `git reset` sur des commits déjà pushés force les autres à diverger. Utilise `git revert` pour annuler des commits publics de manière non destructive.

> [!tip]
> Voir [[soft]], [[mixed]], [[hard]] pour les détails de chaque mode.
