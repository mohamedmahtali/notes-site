---
title: hard
tags:
  - advanced
---

# hard

## Parent
- [[reset]]

## Concepts liés
- [[reset]]
- [[soft]]
- [[mixed]]
- [[reflog]]

---

## Définition

`git reset --hard` déplace HEAD et réinitialise **à la fois le staging area et le working directory** vers l'état du commit cible. Toutes les modifications non committées sont **définitivement supprimées**.

---

## Comportement

```
Avant :
  Working dir : [modifs]  Staging : [stagé]  HEAD → commit C

git reset --hard HEAD~1

Après :
  Working dir : [propre]  Staging : [vide]  HEAD → commit B
  Les modifs de C et les modifs locales sont PERDUES
```

---

## Cas d'usage

```bash
# Annuler tout et revenir à un état propre
git reset --hard HEAD

# Revenir à un commit précis (ex: avant un merge raté)
git reset --hard HEAD~1

# Synchroniser avec le remote (écraser les modifications locales)
git fetch origin
git reset --hard origin/main
```

---

## Récupérer après un --hard accidentel

```bash
# Le commit existe encore dans le reflog
git reflog
# abc1234 HEAD@{1}: commit: feat: the thing I lost

git reset --hard abc1234   # ou git checkout -b recovery abc1234
```

> [!danger] Irréversible sans reflog
> `git reset --hard` est l'une des rares commandes Git qui peut causer une vraie perte de données — uniquement pour les modifications **jamais committées**. Les commits eux-mêmes sont récupérables via `git reflog` pendant ~90 jours.
