---
title: ssh-agent
tags:
  - intermediate
---

# ssh-agent

---

## Définition

`ssh-agent` est un daemon qui mémorise les clés [[SSH]] déchiffrées en mémoire. Une fois la clé ajoutée à l'agent (avec la [[Passphrase]]), tu peux te connecter à autant de serveurs que tu veux sans ressaisir la passphrase.

---

## Utilisation

```bash
# Démarrer l'agent
eval "$(ssh-agent -s)"
# Agent pid 12345

# Ajouter une clé
ssh-add ~/.ssh/id_ed25519
# Enter passphrase: ****
# Identity added: /home/user/.ssh/id_ed25519

# Ajouter toutes les clés standards
ssh-add

# Lister les clés en mémoire
ssh-add -l

# Supprimer une clé de l'agent
ssh-add -d ~/.ssh/id_ed25519

# Supprimer toutes les clés
ssh-add -D
```

---

## SSH agent forwarding

```bash
# Se connecter avec forwarding (passer l'agent aux sauts SSH)
ssh -A user@jump-server

# Dans ~/.ssh/config
Host jump-server
    ForwardAgent yes

# Utile pour git pull depuis un serveur sans clé
ssh -A user@prod-server
git clone git@github.com:org/repo.git  # utilise ton agent local
```

---

> [!warning]
> Agent [[Forwarding]] sur des serveurs non fiables présente un risque — un admin du serveur peut utiliser ton agent. Utiliser uniquement sur des machines de confiance.
