---
title: Bare repository
tags:
  - advanced
---

# Bare repository

## Parent
- [[Repository]]

## Concepts liés
- [[Repository]]
- [[Local repository]]
- [[Remote repository]]

---

## Définition

Un dépôt bare est un dépôt Git **sans working directory** — il ne contient que le contenu du répertoire `.git/`. C'est le format utilisé par les serveurs Git (GitHub, GitLab). Les développeurs ne travaillent pas directement dedans : ils poussent/tirent depuis leur dépôt local.

---

## Créer un dépôt bare

```bash
# Initialiser un dépôt bare
git init --bare /srv/git/mon-projet.git

# Cloner un dépôt existant en bare (pour créer un miroir serveur)
git clone --bare https://github.com/user/repo.git
```

---

## Structure d'un bare repository

```
mon-projet.git/
├── HEAD
├── config
├── description
├── hooks/          ← server-side hooks (post-receive, etc.)
├── info/
├── objects/
└── refs/
```

Pas de `src/`, `README.md`, etc. — uniquement les métadonnées Git.

---

## Cas d'usage

```bash
# Serveur Git interne (sans GitHub)
# Sur le serveur :
git init --bare /srv/repos/mon-projet.git

# Sur les postes développeurs :
git remote add origin ssh://user@serveur/srv/repos/mon-projet.git
git push origin main
```

> [!note]
> La plupart des équipes n'ont jamais besoin de créer manuellement des bare repositories — GitHub/GitLab le font automatiquement. La notion est utile pour comprendre ce qui tourne derrière ces plateformes.
