---
title: SSH keys
tags:
  - beginner
---

# SSH keys

---

## Définition

L'authentification par clé [[SSH]] utilise un mécanisme de cryptographie asymétrique : une **clé privée** (secrète, sur ta machine) et une **clé publique** (sur les serveurs). Le serveur chiffre un challenge avec la clé publique, seul celui qui a la clé privée peut le déchiffrer.

---

## Générer une paire de clés

```bash
# ED25519 (recommandé, plus moderne et sécurisé)
ssh-keygen -t ed25519 -C "mohamed@example.com"

# RSA 4096 (compatibilité avec systèmes anciens)
ssh-keygen -t rsa -b 4096 -C "mohamed@example.com"

# Avec nom de fichier personnalisé
ssh-keygen -t ed25519 -f ~/.ssh/cle_prod -C "prod-server"

# → crée ~/.ssh/id_ed25519 (privée) et ~/.ssh/id_ed25519.pub (publique)
```

---

## Ajouter la clé publique sur un serveur

```bash
# Méthode automatique
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@serveur

# Méthode manuelle
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys

# Permissions requises (IMPORTANT)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```
