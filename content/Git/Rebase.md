---
title: Rebase
tags:
  - intermediate
---

# Rebase

---

## Définition

`git rebase` déplace ou "rejoue" une série de [[Commit]] sur une nouvelle base. Au lieu de créer un commit de [[Merge]], il reconstruit l'historique comme si les commits avaient été créés directement depuis la nouvelle base. Le résultat est un historique **linéaire et propre**.

---

## Rebase vs Merge

```
Merge :
  main:    A → B → C → M   (commit de merge)
                       ↗
  feature: A → D → E

Rebase :
  main:    A → B → C → D' → E'   (linéaire)
  feature: (rejoué sur C)
```

| Critère | Merge | Rebase |
|---|---|---|
| Historique | Préserve les branches | Linéaire |
| Commit de merge | Oui | Non |
| Réécriture | Non | Oui (nouveaux hashes) |
| Sur branche partagée | ✅ Sûr | ⚠️ Dangereux |

---

## Commandes

```bash
# Rebaser feature sur main
git checkout feature/auth
git rebase main

# Rebase interactif (nettoyer les commits)
git rebase -i HEAD~5

# Continuer après résolution de conflit
git rebase --continue

# Annuler le rebase
git rebase --abort
```

---

## Règle d'or

> [!danger] Ne jamais rebaser des commits déjà poussés sur main
> Le rebase réécrit les hashes SHA-1. Rebaser sur une branche partagée force les autres à diverger et peut causer des pertes de travail.

---

## Exemple – synchro avec main avant PR

```bash
# feature/auth a été créée il y a 3 jours, main a avancé
git fetch origin
git rebase origin/main

# Si conflit :
# Ouvrir les fichiers, résoudre, puis :
git add src/auth.js
git rebase --continue

# Forcer le push de la branche rebasée
git push origin feature/auth --force-with-lease
```

> [!tip]
> Préfère `--force-with-lease` à `--force` : il vérifie que personne d'autre n'a pushé sur ta branche entre-temps.
