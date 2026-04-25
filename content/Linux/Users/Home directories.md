---
title: Home directories
tags:
  - beginner
---

# Home directories

---

## Définition

Le home directory est le répertoire personnel de chaque utilisateur, généralement `/home/utilisateur`. C'est là où sont stockés les fichiers personnels, les configurations (dotfiles), et les clés [[SSH]].

---

## Structure typique

```
/home/mohamed/
├── .bashrc          # config bash (non-login shell)
├── .bash_profile    # config bash (login shell)
├── .profile         # config shell générique (POSIX)
├── .ssh/
│   ├── authorized_keys  # clés publiques autorisées
│   ├── config           # config client SSH
│   ├── id_ed25519        # clé privée
│   └── id_ed25519.pub    # clé publique
├── .gitconfig       # config Git
└── Documents/
```

---

## Commandes

```bash
# Aller dans son home
cd
cd ~
cd $HOME

# Voir le home d'un utilisateur
echo ~mohamed
grep "mohamed" /etc/passwd | cut -d: -f6

# Créer un home pour un utilisateur existant
mkdir -p /home/nouveau-user
cp -r /etc/skel/. /home/nouveau-user/
chown -R nouveau-user:nouveau-user /home/nouveau-user

# /etc/skel contient les fichiers copiés dans chaque nouveau home
ls /etc/skel/
```
