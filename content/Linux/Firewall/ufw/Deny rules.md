---
title: Deny rules
tags:
  - beginner
---

# Deny rules

## Parent
- [[ufw]]

---

## Définition

Les règles `deny` dans UFW bloquent le trafic réseau. Avec `ufw default deny incoming`, tout le trafic entrant est bloqué par défaut — les règles `allow` définissent les exceptions.

---

## Syntaxe

```bash
# Bloquer un port
ufw deny 23/tcp          # bloquer Telnet

# Bloquer depuis une IP
ufw deny from 203.0.113.10

# Bloquer un sous-réseau
ufw deny from 10.0.0.0/8

# deny vs reject
ufw deny 23/tcp     # DROP : la connexion timeout silencieusement
ufw reject 23/tcp   # REJECT : envoie une erreur ICMP immédiate
```

---

## Politique par défaut

```bash
# Configuration recommandée pour un serveur
ufw default deny incoming   # bloquer tout en entrée
ufw default allow outgoing  # autoriser tout en sortie

# Puis ouvrir seulement ce qui est nécessaire
ufw allow ssh
ufw allow https
```

---

> [!tip]
> `deny` (DROP) est préférable à `reject` pour les connexions non désirées — les scanners et bots passent à autre chose plus vite s'ils ne reçoivent pas de réponse.
