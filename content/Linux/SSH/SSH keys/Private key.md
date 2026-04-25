---
title: Private key
tags:
  - intermediate
---
# Private key

---

## Définition

La clé privée est la moitié secrète d'une paire de clés [[SSH]]. Elle reste toujours sur ta machine locale et ne doit jamais être partagée. Elle est utilisée pour prouver ton identité lors d'une connexion SSH.

---

## Pourquoi c'est important

> [!warning] Ne jamais partager la clé privée
> Si quelqu'un obtient ta clé privée (sans [[Passphrase]]), il peut se connecter à tous les serveurs où ta clé publique est autorisée. Protège-la avec une passphrase forte et des [[Permissions]] restrictives.

---

## Permissions et sécurité

```bash
# Permissions obligatoires — SSH refusera si trop permissives
chmod 600 ~/.ssh/id_ed25519
chmod 700 ~/.ssh/

# Vérifier les permissions
ls -la ~/.ssh/
# id_ed25519 doit être -rw------- (600)
# id_ed25519.pub peut être -rw-r--r-- (644)
```

---

## Génération

```bash
# Ed25519 (recommandé, 2024)
ssh-keygen -t ed25519 -C "commentaire@machine"

# RSA 4096 bits (compatibilité legacy)
ssh-keygen -t rsa -b 4096 -C "commentaire"

# Chemin et passphrase demandés interactivement
```

---

> [!tip]
> Toujours protéger avec une passphrase. Utiliser [[ssh-agent]] pour ne la taper qu'une fois par session.
