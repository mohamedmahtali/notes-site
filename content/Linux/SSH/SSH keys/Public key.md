---
title: Public key
tags:
  - beginner
---
# Public key

## Parent
- [[SSH keys]]

---

## Définition

La clé publique est la moitié partageable d'une paire de clés asymétriques. Elle est placée sur les serveurs distants dans `~/.ssh/authorized_keys`. Toute personne possédant la clé privée correspondante peut s'authentifier.

---

## Pourquoi c'est important

> [!tip] Peut être partagée librement
> La clé publique n'est pas un secret. Tu peux la coller dans GitHub, la distribuer sur tous tes serveurs, ou la publier en ligne — sans risque. C'est la clé **privée** qui doit rester secrète.

---

## Utilisation

```bash
# Afficher sa clé publique
cat ~/.ssh/id_ed25519.pub

# Copier sur un serveur distant
ssh-copy-id user@server
# ou manuellement :
cat ~/.ssh/id_ed25519.pub | ssh user@server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# Format d'une clé publique Ed25519
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... user@machine
```

---

## Sur GitHub / GitLab

Aller dans **Settings → SSH Keys**, coller le contenu de `~/.ssh/id_ed25519.pub`. GitHub utilise ta clé publique pour vérifier ton identité lors des push/pull SSH.

---

> [!note]
> Voir [[Private key]] pour la clé privée et [[ssh-agent]] pour éviter de retaper la passphrase.
