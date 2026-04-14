---
title: Passphrase
tags:
  - intermediate
---

# Passphrase

## Parent
- [[SSH keys]]

---

## Définition

La passphrase est un mot de passe qui chiffre la clé privée SSH sur disque. Sans passphrase, quiconque accède à ton fichier de clé privée peut se connecter à tous tes serveurs. Avec passphrase, la clé est chiffrée — elle est inutilisable sans le mot de passe.

---

## Ajouter/modifier une passphrase

```bash
# Ajouter lors de la génération
ssh-keygen -t ed25519 -C "mon@email.com"
# Enter passphrase: ****
# Enter same passphrase again: ****

# Ajouter à une clé existante sans passphrase
ssh-keygen -p -f ~/.ssh/id_ed25519

# Changer la passphrase
ssh-keygen -p -f ~/.ssh/id_ed25519
# Enter old passphrase: ****
# Enter new passphrase: ****
```

---

## ssh-agent – saisir la passphrase une seule fois

```bash
# Démarrer l'agent
eval "$(ssh-agent -s)"

# Ajouter la clé (saisir la passphrase une fois)
ssh-add ~/.ssh/id_ed25519

# La clé est mémorisée pour la session
ssh user@serveur   # plus de demande de passphrase
```

---

> [!tip]
> Utilise une passphrase forte + ssh-agent. Tu as la sécurité (clé chiffrée sur disque) sans la friction (saisie à chaque connexion).
