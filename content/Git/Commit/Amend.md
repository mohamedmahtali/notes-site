---
title: Amend
tags:
  - intermediate
---

# Amend

---

## Définition

`git commit --amend` modifie le **dernier [[Commit]]** : il permet de corriger le message, d'ajouter des fichiers oubliés, ou de modifier des changements, sans créer un nouveau commit. Il réécrit l'historique local.

---

## Pourquoi c'est important

> [!warning] Uniquement sur des commits non poussés
> `--amend` réécrit le hash du commit. Sur un commit déjà pushé sur le remote, ça crée une divergence d'historique et force les autres contributeurs à [[Rebase]].

---

## Commandes

```bash
# Corriger uniquement le message du dernier commit
git commit --amend -m "feat(auth): add JWT validation middleware"

# Ajouter un fichier oublié au dernier commit
git add fichier-oublié.js
git commit --amend --no-edit   # garde le même message

# Amend interactif (ouvre l'éditeur)
git commit --amend
```

---

## Exemple typique

```bash
git commit -m "fet: add login page"   # typo dans le message

git commit --amend -m "feat: add login page"
# ✅ message corrigé, aucun nouveau commit créé
```

```bash
# Oublier un fichier dans le commit
git add .
git commit -m "feat: add dashboard"
# → Oups, j'ai oublié src/dashboard.css

git add src/dashboard.css
git commit --amend --no-edit
# ✅ dashboard.css est maintenant inclus dans le commit précédent
```

> [!tip]
> Pour modifier des commits plus anciens (pas seulement le dernier), utilise [[Interactive rebase|git rebase -i]].
