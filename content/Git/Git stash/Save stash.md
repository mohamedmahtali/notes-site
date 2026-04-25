---
title: Save stash
tags:
  - intermediate
---

# Save stash

---

## Définition

`git stash push` (ou `git stash save` dans les anciennes versions) met de côté les modifications non committées — fichiers trackés modifiés et fichiers en [[Staging]] — dans une pile de stash. Le working directory revient à l'état du dernier [[Commit]], propre.

---

## Pourquoi c'est important

> [!tip] Changer de contexte sans perdre son travail
> Tu travailles sur une feature et tu dois urgement corriger un bug sur `main`. Le stash te permet de mettre en pause proprement sans créer un commit de "WIP".

---

## Commandes

```bash
# Stash basique (fichiers trackés uniquement)
git stash

# Stash avec un message descriptif (recommandé)
git stash push -m "feat: ajout formulaire contact en cours"

# Inclure les fichiers non-trackés (nouveaux fichiers)
git stash push -u -m "feat: nouvelle page dashboard"

# Inclure les fichiers ignorés aussi
git stash push -a -m "backup complet"

# Stash sélectif – seulement certains fichiers
git stash push -m "fix partiel" src/config.js src/api.js
```

---

## Voir les stash enregistrés

```bash
git stash list
# stash@{0}: On feature/auth: feat: ajout formulaire contact en cours
# stash@{1}: On main: fix: correction temporaire CSS
```

---

## Exemple complet

```bash
# En plein travail sur une feature
git status
# Modified: src/components/Form.tsx
# Modified: src/api/auth.ts

# Urgence : basculer sur main pour un hotfix
git stash push -m "feat: formulaire contact WIP"

git checkout main
# → corriger le bug, committer

# Revenir sur sa feature
git checkout feature/contact-form
git stash pop
```

> [!note] Convention
> Toujours mettre un message sur le stash. `git stash list` avec 5 entrées sans message est illisible.
