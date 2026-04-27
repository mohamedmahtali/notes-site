---
title: SSH keys
tags:
  - beginner
---

# SSH keys

## Définition

L'authentification par clé SSH utilise la cryptographie asymétrique : une **clé privée** (secrète, sur ta machine) et une **clé publique** (déposée sur les serveurs). Le serveur chiffre un challenge avec la clé publique — seul le détenteur de la clé privée peut le déchiffrer.

## Générer une paire de clés

```bash
# ED25519 — recommandé (plus court, plus sécurisé que RSA)
ssh-keygen -t ed25519 -C "mohamed@example.com"

# RSA 4096 — pour les systèmes anciens (AWS, certains HSM)
ssh-keygen -t rsa -b 4096 -C "mohamed@example.com"

# Clé dédiée avec nom personnalisé
ssh-keygen -t ed25519 -f ~/.ssh/prod_key -C "prod-server"

# → crée ~/.ssh/id_ed25519 (privée) et ~/.ssh/id_ed25519.pub (publique)
```

> [!warning] Ne jamais partager la clé privée
> `~/.ssh/id_ed25519` reste sur ta machine uniquement. Seul `id_ed25519.pub` se dépose sur les serveurs.

## Déposer la clé publique sur un serveur

```bash
# Méthode automatique (recommandée)
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@serveur

# Méthode manuelle
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys

# Permissions requises (SSH refusera si trop ouvertes)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

## Fichier ~/.ssh/config — gérer plusieurs serveurs

Le fichier config évite de taper les options à chaque connexion :

```
# ~/.ssh/config

# Serveur de production
Host prod
    HostName 52.12.34.56
    User ubuntu
    IdentityFile ~/.ssh/prod_key
    Port 22

# Bastion (jump host)
Host bastion
    HostName bastion.mycompany.com
    User ec2-user
    IdentityFile ~/.ssh/bastion_key

# Serveur interne via bastion (ProxyJump)
Host internal-db
    HostName 10.0.1.50
    User admin
    IdentityFile ~/.ssh/internal_key
    ProxyJump bastion      # ← passe par le bastion automatiquement

# Paramètres globaux
Host *
    AddKeysToAgent yes
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

```bash
# Connexion simplifiée grâce au config
ssh prod                   # au lieu de: ssh -i ~/.ssh/prod_key ubuntu@52.12.34.56
ssh internal-db            # connexion automatique via bastion
```

## SSH Agent — ne plus retaper la passphrase

```bash
# Démarrer l'agent
eval "$(ssh-agent -s)"

# Ajouter une clé (demande la passphrase une seule fois)
ssh-add ~/.ssh/id_ed25519
ssh-add ~/.ssh/prod_key

# Voir les clés chargées
ssh-add -l

# Supprimer les clés de l'agent
ssh-add -D
```

## Transfert de fichiers

```bash
# Copier un fichier vers un serveur
scp fichier.txt user@serveur:/chemin/destination/

# Copier depuis un serveur
scp user@serveur:/var/log/app.log ./

# Copier un dossier entier
scp -r ./dist/ user@serveur:/var/www/html/

# rsync — plus efficace (synchronisation différentielle)
rsync -avz ./dist/ user@serveur:/var/www/html/
rsync -avz --delete ./dist/ user@serveur:/var/www/html/  # supprime les fichiers absents
```

## Tunnel SSH (port forwarding)

```bash
# Local forwarding : accéder à un service distant comme s'il était local
ssh -L 5432:db-internal:5432 user@bastion
# → psql -h localhost -p 5432 ...  (accède à la BDD via le tunnel)

# Remote forwarding : exposer un service local vers le serveur distant
ssh -R 8080:localhost:3000 user@serveur

# SOCKS proxy (tunnel dynamique)
ssh -D 1080 user@serveur
# → configurer le navigateur sur 127.0.0.1:1080
```

## Explorer

- **[[SSH]]** — connexion SSH, options, hardening du serveur
- **[[Linux/Networking]]** — commandes réseau Linux, ports
- **[[Certificates]]** — cryptographie asymétrique (même principe que SSH)
