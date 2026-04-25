---
title: Groups
tags:
  - beginner
---

# Groups

---

## Définition

Les groupes [[Linux]] permettent de donner les mêmes [[Permissions]] à plusieurs utilisateurs. Chaque utilisateur a un groupe primaire (dans /etc/passwd) et peut appartenir à plusieurs groupes secondaires.

---

## Commandes

```bash
# Créer un groupe
groupadd developers

# Ajouter un utilisateur à un groupe
usermod -aG developers mohamed    # -a : append (conserver les groupes existants)
gpasswd -a mohamed developers     # alternative

# Supprimer un utilisateur d'un groupe
gpasswd -d mohamed developers

# Supprimer un groupe
groupdel developers

# Voir les groupes
groups                  # groupes de l'utilisateur courant
groups mohamed          # groupes d'un utilisateur
id                      # UID, GID, et tous les groupes
cat /etc/group          # tous les groupes du système

# Changer de groupe actif
newgrp docker           # activer le groupe docker pour la session
```

---

## Groupes système courants

| Groupe | Accès |
|---|---|
| `sudo` / `wheel` | Commandes [[sudo]] |
| `docker` | Gérer [[Docker]] sans sudo |
| `www-data` | Fichiers web [[Nginx]]/apache |
| `ssh` | Connexion [[SSH]] (si configuré) |
| `adm` | Lecture des logs système |
