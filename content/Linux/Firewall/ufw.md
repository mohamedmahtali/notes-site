---
title: ufw
tags:
  - beginner
---

# ufw

## Parent
- [[Firewall]]

## Enfants
- [[Allow rules]]
- [[Deny rules]]
- [[Status]]

---

## Définition

UFW (Uncomplicated Firewall) est un frontend pour iptables conçu pour être simple à utiliser. C'est l'outil recommandé sur Ubuntu et Debian pour la gestion du firewall.

---

## Commandes essentielles

```bash
# Activer/désactiver
ufw enable
ufw disable

# Voir l'état et les règles
ufw status
ufw status verbose
ufw status numbered

# Règle par défaut (recommandé)
ufw default deny incoming
ufw default allow outgoing

# Autoriser des services
ufw allow ssh          # ou : ufw allow 22/tcp
ufw allow http         # port 80
ufw allow https        # port 443

# Autoriser depuis une IP spécifique
ufw allow from 192.168.1.0/24
ufw allow from 203.0.113.10 to any port 22

# Supprimer une règle
ufw delete allow http
ufw delete 3           # par numéro (ufw status numbered)

# Logs
ufw logging on
```
