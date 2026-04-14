---
title: SSH config
tags:
  - intermediate
---

# SSH config

## Parent
- [[SSH]]

---

## Définition

Le fichier `~/.ssh/config` permet de définir des raccourcis et configurations pour les connexions SSH. Au lieu de mémoriser IP, port, clé, et utilisateur pour chaque serveur, on définit un alias.

---

## Syntaxe

```bash
# ~/.ssh/config

# Serveur de production
Host prod
    HostName 203.0.113.10
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519_prod
    Port 22

# Serveur de développement
Host dev
    HostName 192.168.1.50
    User devuser
    IdentityFile ~/.ssh/id_ed25519_dev
    Port 2222
    ServerAliveInterval 60

# Jump server (bastion)
Host bastion
    HostName bastion.example.com
    User ec2-user
    IdentityFile ~/.ssh/id_ed25519

# Accès via le bastion
Host internal-*
    ProxyJump bastion
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519

# GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
```

---

## Utilisation

```bash
# Avec config → connexion simple
ssh prod
ssh dev
ssh internal-web-server   # passe automatiquement par bastion

# Les permissions doivent être strictes
chmod 600 ~/.ssh/config
```
