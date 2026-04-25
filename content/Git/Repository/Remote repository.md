---
title: Remote repository
tags:
  - beginner
---

# Remote repository

---

## Définition

Un dépôt distant (remote [[Repository]]) est une version du dépôt hébergée sur un serveur (GitHub, GitLab, Bitbucket, serveur privé). Il sert de point de synchronisation entre les membres de l'équipe. Par convention, le remote principal s'appelle `origin`.

---

## Commandes

```bash
# Voir les remotes configurés
git remote -v
# origin  https://github.com/user/repo.git (fetch)
# origin  https://github.com/user/repo.git (push)

# Ajouter un remote
git remote add origin https://github.com/user/repo.git

# Ajouter un second remote (ex: fork upstream)
git remote add upstream https://github.com/org/repo.git

# Changer l'URL d'un remote
git remote set-url origin git@github.com:user/repo.git

# Supprimer un remote
git remote remove upstream

# Récupérer sans merger (safe)
git fetch origin

# Récupérer et merger
git pull origin main

# Pousser une branche
git push origin feature/auth

# Pousser et créer le tracking
git push -u origin feature/auth
```

---

## Synchronisation

```
Local Repository  ←──── git fetch ────── Remote Repository
                  ──────── git push ────→
                  ←──── git pull ─────── (= fetch + merge)
```

---

## SSH vs HTTPS

| Protocole | Format | Auth |
|---|---|---|
| HTTPS | `https://github.com/user/repo.git` | Token ou password |
| [[SSH]] | `git@github.com:user/repo.git` | Clé SSH |

> [!tip]
> Préfère SSH pour le développement quotidien : pas de saisie de token à chaque push.
