---
title: MX
tags:
  - intermediate
---

# MX

---

## Définition

Un enregistrement MX (Mail eXchange) indique les serveurs de messagerie responsables de la réception des emails pour un domaine, avec une priorité (plus basse = plus prioritaire).

---

## Format

```
domaine     TTL   type  priorité  serveur
example.com 300   MX    10        mail1.example.com
example.com 300   MX    20        mail2.example.com  # backup
```

---

## Commandes

```bash
# Voir les MX d'un domaine
dig example.com MX
# example.com. 300 IN MX 10 mail1.example.com.
# example.com. 300 IN MX 20 mail2.example.com.

# Tester la connexion SMTP
telnet mail1.example.com 25
```

---

## Services courants

| Service | MX records |
|---|---|
| Gmail | `aspmx.l.google.com` (priorité 1) |
| Office 365 | `domain.mail.protection.outlook.com` |
| Mailgun | Records spécifiques à chaque domaine |

> [!note]
> Les MX doivent pointer vers des A records, jamais vers des [[CNAME]]. Le serveur SMTP résout le MX puis l'[[A record]] pour se connecter.
