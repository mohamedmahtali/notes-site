---
title: soft
tags:
  - advanced
---

# soft

## Parent
- [[reset]]

## Concepts liés
- [[reset]]
- [[mixed]]
- [[hard]]
- [[Amend]]

---

## Définition

`git reset --soft` déplace HEAD vers un commit précédent tout en laissant **le staging area et le working directory intacts**. Les modifications des commits annulés se retrouvent en staging, prêtes à être recommittées.

---

## Comportement

```
Avant :
  Working dir : [A]  Staging : [A]  HEAD → commit C

git reset --soft HEAD~2

Après :
  Working dir : [A]  Staging : [A]  HEAD → commit A
  (les modifs de B et C sont dans staging)
```

---

## Cas d'usage

```bash
# Fusionner les 3 derniers commits en 1 seul
git reset --soft HEAD~3
git commit -m "feat: fonctionnalité complète"

# Corriger un commit (alternative à --amend)
git reset --soft HEAD~1
# → modifier les fichiers si besoin
git commit -m "feat: message corrigé avec fichiers complets"
```

> [!tip]
> `--soft` est le mode "annuler sans rien perdre". Idéal pour réorganiser ou nettoyer l'historique local avant de pusher.
