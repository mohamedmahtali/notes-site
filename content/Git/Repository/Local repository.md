---
title: Local repository
tags:
  - beginner
---

# Local repository

## Parent
- [[Repository]]

## Concepts liés
- [[Repository]]
- [[Remote repository]]
- [[Commit]]
- [[Branch]]

---

## Définition

Un dépôt local est la copie complète du dépôt Git sur ta machine. Il contient tout l'historique des commits, toutes les branches, et le répertoire `.git/` qui stocke les métadonnées Git. Tu travailles toujours en local, même sans connexion internet.

---

## Structure du répertoire .git/

```
.git/
├── HEAD          ← commit/branche actuel
├── config        ← configuration locale du dépôt
├── objects/      ← tous les objets Git (commits, blobs, trees)
├── refs/
│   ├── heads/    ← branches locales
│   └── remotes/  ← branches distantes en cache
├── index         ← staging area
└── COMMIT_EDITMSG ← dernier message de commit
```

---

## Commandes essentielles

```bash
# Initialiser un nouveau dépôt local
git init mon-projet
cd mon-projet

# Cloner un dépôt distant en local
git clone https://github.com/org/repo.git

# Voir la configuration locale
git config --local --list

# Voir l'état du dépôt local
git status
git log --oneline --graph

# Travailler hors ligne – tout est disponible localement
git log           # ✅ fonctionne sans internet
git branch        # ✅ fonctionne sans internet
git diff          # ✅ fonctionne sans internet
git commit        # ✅ fonctionne sans internet
git push          # ❌ nécessite le réseau
```

---

## Avantage distribué

> [!tip] Tout l'historique en local
> Contrairement à SVN (centralisé), Git stocke l'intégralité de l'historique sur chaque machine. Tu peux brancher, committer, tagger, et inspecter le log sans aucune connexion réseau. Le push vers le remote est la seule opération qui nécessite internet.
