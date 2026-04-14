---
title: Users
tags:
  - beginner
---

# Users

## Parent
- [[Linux]]

## Enfants
- [[Groups]]
- [[sudo]]
- [[Home directories]]
- [[Service accounts]]
- [[PAM]]

---

## Définition

Linux est un système multi-utilisateurs. Chaque utilisateur a un UID unique, appartient à des groupes, et a des permissions sur les fichiers. La gestion des utilisateurs est centrale pour la sécurité du système.

---

## Commandes essentielles

```bash
# Créer un utilisateur
useradd -m -s /bin/bash -c "Mohamed Mahtali" mohamed
# -m : créer le home directory
# -s : shell par défaut
# -c : commentaire

# Définir/changer le mot de passe
passwd mohamed

# Modifier un utilisateur
usermod -aG docker mohamed    # ajouter au groupe docker
usermod -s /bin/zsh mohamed   # changer le shell

# Supprimer un utilisateur
userdel -r mohamed    # -r : supprimer aussi le home

# Voir les groupes d'un utilisateur
id mohamed
groups mohamed

# Changer d'utilisateur
su - mohamed          # login shell complet
su -s /bin/bash -c "commande" www-data   # exécuter une commande
```

---

## Fichiers importants

```
/etc/passwd   → liste des utilisateurs (nom:x:UID:GID:commentaire:home:shell)
/etc/shadow   → mots de passe hashés (root only)
/etc/group    → définition des groupes
```

```bash
# Voir les infos d'un utilisateur
grep "mohamed" /etc/passwd
# mohamed:x:1001:1001:Mohamed Mahtali:/home/mohamed:/bin/bash
```
