---
title: sudo
tags:
  - beginner
---

# sudo

---

## Définition

`sudo` (superuser do) permet d'exécuter des commandes avec les privilèges d'un autre utilisateur (généralement root), après authentification. C'est le mécanisme standard pour l'élévation de privilèges sur [[Linux]], plus sûr qu'un accès root direct.

---

## Utilisation

```bash
# Exécuter une commande en root
sudo apt-get update
sudo systemctl restart nginx

# Ouvrir un shell root
sudo -i        # login shell root
sudo -s        # shell root (environment courant)
sudo su -      # alternative

# Exécuter en tant qu'un autre utilisateur
sudo -u www-data ls /var/www

# Voir les droits sudo de l'utilisateur courant
sudo -l
```

---

## Configuration /etc/sudoers

```bash
# Éditer de manière sécurisée (vérifie la syntaxe)
visudo

# Donnes tout les droits sudo à un utilisateur
mohamed  ALL=(ALL:ALL) ALL

# Permettre des commandes spécifiques sans mot de passe
deploy   ALL=(ALL) NOPASSWD: /bin/systemctl restart app

# Autoriser un groupe
%developers ALL=(ALL) /usr/bin/git, /usr/bin/npm

# Fichiers d'override par service
# /etc/sudoers.d/nginx (permissions limitées)
www-data ALL=(ALL) NOPASSWD: /bin/systemctl reload nginx
```

---

> [!warning]
> Ne jamais utiliser `sudo` avec des scripts ou programmes non vérifiés. Préférer le principe du moindre privilège : accorder seulement les commandes nécessaires, pas `ALL`.
