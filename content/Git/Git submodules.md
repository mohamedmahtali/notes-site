---
title: Git submodules
tags:
  - intermediate
---
# Git submodules

## Parent
- [[Git]]

## Enfants
- [[Add submodule]]
- [[Update submodule]]
- [[Nested repositories]]

## Concepts liés
- [[Add submodule]]
- [[Update submodule]]
- [[Nested repositories]]
- [[Repository]]

---

## Définition

Les submodules Git permettent d'inclure un dépôt Git à l'intérieur d'un autre. Le dépôt parent enregistre un pointeur vers un **commit précis** du sous-module — pas une copie du code. C'est utile pour partager des bibliothèques internes entre projets.

---

## Pourquoi c'est important

> [!warning] Choisir avec soin
> Les submodules ajoutent de la complexité (clone, update, sync). Évalue d'abord si un gestionnaire de paquets (npm, pip, go mod) ne résout pas mieux le besoin.

---

## Commandes essentielles

```bash
# Ajouter un sous-module
git submodule add https://github.com/org/shared-lib.git libs/shared

# Cloner un projet avec ses sous-modules
git clone --recurse-submodules https://github.com/org/projet.git

# Initialiser les sous-modules après un clone normal
git submodule update --init --recursive

# Mettre à jour les sous-modules vers le remote
git submodule update --remote

# Voir l'état des sous-modules
git submodule status
```

---

## Fichier .gitmodules

```ini
[submodule "libs/shared"]
    path = libs/shared
    url = https://github.com/org/shared-lib.git
    branch = main
```

---

## Pièges courants

> [!warning]
> - Clone sans `--recurse-submodules` → dossier vide
> - Modifier le code dans le sous-module sans committer → perte de changements
> - Push du parent sans push du sous-module → CI cassée

---

> [!tip]
> Après chaque `git pull` qui change les pointeurs de sous-modules, lancer `git submodule update --init --recursive`.
