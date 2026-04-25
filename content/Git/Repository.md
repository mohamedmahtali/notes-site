---
title: Repository
tags:
  - intermediate
---
# Repository

---

## Définition

Un dépôt [[Git]] (repository) est un répertoire versionné qui contient l'intégralité de l'historique d'un projet sous forme d'objets Git. Il existe en deux formes : **local** (sur ta machine, avec working directory) et **distant** (sur un serveur, point de synchronisation).

---

## Types de dépôts

| Type | Description |
|---|---|
| [[Local repository\|Local]] | Copie complète sur ta machine, avec working directory |
| [[Remote repository\|Distant]] | Hébergé sur GitHub/GitLab, point de synchronisation |
| [[Bare repository\|Bare]] | Sans working directory — format serveur |

---

## Structure interne

```
mon-projet/
├── .git/              ← dépôt Git (tout l'historique)
│   ├── HEAD           ← position actuelle
│   ├── objects/       ← commits, blobs, trees
│   ├── refs/heads/    ← branches locales
│   └── refs/remotes/  ← branches distantes en cache
├── src/
├── README.md
└── ...
```

---

## Commandes essentielles

```bash
# Créer un dépôt local
git init mon-projet

# Cloner un dépôt distant
git clone https://github.com/org/repo.git

# Voir les remotes configurés
git remote -v

# Ajouter un remote
git remote add origin https://github.com/org/repo.git

# Synchronisation
git fetch origin      # récupérer sans merger
git pull origin main  # récupérer et merger
git push origin main  # envoyer
```

---

> [!tip] Distribué par nature
> Chaque clone est un dépôt complet — tu as tout l'historique en local, tu peux committer, brancher, et naviguer dans le log sans connexion réseau.
