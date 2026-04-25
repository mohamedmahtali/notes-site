---
title: Commit
tags:
  - intermediate
---
# Commit

---

## Définition

Un commit est un instantané (snapshot) de l'état du dépôt à un moment précis. Il contient : les modifications, l'auteur, la date, un message descriptif, et une référence vers le commit parent. Chaque commit est identifié par un hash SHA-1 unique.

---

## Pourquoi c'est important

> [!tip] L'unité atomique de [[Git]]
> Un commit doit représenter **une seule intention logique**. "Ajouter la page de connexion" est bon. "Diverses modifications" est mauvais. Des commits propres facilitent les reviews, les reverts, et le git log.

---

## Commandes essentielles

```bash
# Indexer des fichiers
git add src/auth.js
git add .              # tout le working directory

# Créer un commit
git commit -m "feat(auth): add login endpoint"

# Indexer + committer en une commande (fichiers déjà trackés)
git commit -am "fix: correct null check"

# Voir le dernier commit
git show HEAD

# Voir l'historique
git log --oneline --graph
```

---

## Anatomie d'un commit

```
commit a3f2c1e7d8b9...
Author: Mohamed Mahtali <m@example.com>
Date:   Mon Jan 15 14:32:00 2024

    feat(auth): add JWT token refresh logic

    Worker tokens expired after 1h causing user logouts.
    Implemented silent refresh with 5min buffer.

    Closes #142
```

---

> [!tip]
> Voir [[Commit message]] pour la convention Conventional Commits, [[Amend]] pour corriger le dernier commit, et [[Commit history]] pour naviguer dans l'historique.
