---
title: journalctl
tags:
  - intermediate
---

# journalctl

---

## Définition

`journalctl` est l'outil de consultation du journal [[systemd]] (journald). Journald centralise tous les logs du système ([[Kernel]], [[Services]] systemd, applications) dans un format binaire structuré, interrogeable et filtrable.

---

## Commandes essentielles

```bash
# Tous les logs (depuis le début)
journalctl

# Suivre en temps réel
journalctl -f

# Logs d'un service spécifique
journalctl -u nginx
journalctl -u nginx -f

# Dernières N lignes
journalctl -n 100
journalctl -u nginx -n 50

# Depuis un moment précis
journalctl --since "2024-01-15 10:00:00"
journalctl --since "1 hour ago"
journalctl --since yesterday

# Filtrer par priorité (niveau)
journalctl -p err          # erreurs uniquement
journalctl -p warning..err # avertissements et erreurs

# Format court (comme /var/log/syslog)
journalctl -o short
journalctl -o json         # format JSON (pour parsing)
journalctl -o cat          # message seulement
```
