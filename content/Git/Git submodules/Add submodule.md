---
title: Add submodule
tags:
  - advanced
---

# Add submodule

---

## Définition

`git submodule add` intègre un dépôt [[Git]] externe comme sous-répertoire d'un dépôt parent. Le dépôt parent enregistre un pointeur vers un [[Commit]] précis du sous-module, pas une copie du code.

---

## Commandes

```bash
# Ajouter un sous-module
git submodule add https://github.com/org/library.git libs/library

# Ajouter sur une branche spécifique
git submodule add -b main https://github.com/org/theme.git themes/default

# Cloner un dépôt qui contient des sous-modules
git clone --recurse-submodules https://github.com/org/projet.git

# Initialiser les sous-modules après un clone normal
git submodule update --init --recursive
```

---

## Ce que ça crée

```
.gitmodules          ← fichier de config des sous-modules
libs/library/        ← dossier du sous-module (dépôt Git imbriqué)
```

```ini
# .gitmodules
[submodule "libs/library"]
    path = libs/library
    url = https://github.com/org/library.git
```

---

## Exemple

```bash
# Projet principal qui dépend d'une lib partagée
git submodule add https://github.com/mon-org/shared-utils.git shared

# Committer les fichiers créés
git add .gitmodules shared
git commit -m "chore: add shared-utils as submodule"
```

> [!warning] Complexité accrue
> Les sous-[[Modules]] ajoutent de la friction (clone, update, sync). Évalue si une dépendance de [[Package]] manager (npm, pip, go mod) ne ferait pas mieux le travail.
