---
title: Lightweight tags
tags:
  - intermediate
---

# Lightweight tags

## Parent
- [[Git tags]]

## Concepts liés
- [[Git tags]]
- [[Annotated tags]]

---

## Définition

Un tag léger (lightweight tag) est simplement un pointeur vers un commit spécifique, sans métadonnées supplémentaires (pas de message, pas de date de tag, pas de tagger). C'est l'équivalent d'un marque-page sur un commit.

---

## Commandes

```bash
# Créer un tag léger
git tag v1.2.0-rc1

# Tagger un commit spécifique
git tag debug-point abc1234

# Lister les tags
git tag -l

# Voir où pointe le tag
git rev-parse v1.2.0-rc1

# Pousser le tag
git push origin v1.2.0-rc1

# Supprimer un tag local
git tag -d debug-point

# Supprimer un tag remote
git push origin --delete debug-point
```

---

## Quand utiliser les tags légers

> [!tip] Marquages temporaires
> Les tags légers sont utiles pour des marquages de courte durée : point de sauvegarde pendant un débogage, référence rapide à un état particulier, release candidate interne.

> [!note]
> Pour les releases officielles publiées à des utilisateurs, toujours utiliser [[Annotated tags|des tags annotés]] — ils contiennent les métadonnées nécessaires aux outils de release et à `git describe`.
