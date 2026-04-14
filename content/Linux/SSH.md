---
title: SSH
tags:
  - beginner
---

# SSH

## Parent
- [[Linux]]

## Enfants
- [[SSH keys]]
- [[SSH config]]
- [[Port forwarding]]
- [[SCP and SFTP]]

---

## Définition

SSH (Secure Shell) est un protocole cryptographique pour accéder et administrer des serveurs à distance de manière sécurisée. Il remplace Telnet et FTP en chiffrant toutes les communications.

---

## Connexion de base

```bash
# Connexion par mot de passe
ssh user@serveur.example.com
ssh user@192.168.1.10

# Port non-standard
ssh -p 2222 user@serveur.example.com

# Avec une clé SSH
ssh -i ~/.ssh/ma_cle user@serveur.example.com

# Exécuter une commande distante
ssh user@serveur "df -h"
ssh user@serveur "systemctl restart nginx"

# Plusieurs commandes
ssh user@serveur << 'EOF'
  cd /app
  git pull
  systemctl restart app
EOF
```

---

## Commandes essentielles

```bash
# Générer une paire de clés
ssh-keygen -t ed25519 -C "mon@email.com"

# Copier la clé publique sur un serveur
ssh-copy-id user@serveur

# Tester la connexion
ssh -v user@serveur     # verbose, pour déboguer
ssh -T git@github.com   # tester la clé GitHub

# Voir les connexions actives
who
w
last
```
