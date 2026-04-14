---
title: Allow rules
tags:
  - beginner
---

# Allow rules

## Parent
- [[ufw]]

---

## Définition

Les règles `allow` dans UFW autorisent le trafic réseau qui serait sinon bloqué par la politique par défaut.

---

## Syntaxe

```bash
# Par service (lit /etc/services)
ufw allow ssh
ufw allow http
ufw allow https
ufw allow mysql

# Par port
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 5432/tcp   # PostgreSQL

# Plage de ports
ufw allow 8000:8080/tcp

# Depuis une IP spécifique
ufw allow from 192.168.1.10
ufw allow from 192.168.1.10 to any port 22

# Depuis un sous-réseau
ufw allow from 192.168.1.0/24
ufw allow from 10.0.0.0/8 to any port 5432

# Règle complète (protocole + port + source)
ufw allow proto tcp from 203.0.113.10 to any port 22
```

---

## Limiter (rate limiting SSH)

```bash
# Limiter SSH pour prévenir les attaques brute force
ufw limit ssh
# → bloque les IPs qui ont tenté > 6 connexions en 30 secondes
```
