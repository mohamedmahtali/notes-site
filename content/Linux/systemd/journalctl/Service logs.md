---
title: Service logs
tags:
  - beginner
---

# Service logs

## Parent
- [[journalctl]]

---

## Définition

journalctl permet de consulter les logs d'un service systemd spécifique grâce au flag `-u` (unit). Les logs incluent les sorties stdout/stderr du service et les événements systemd (démarrage, arrêt, redémarrage).

---

## Commandes

```bash
# Logs d'un service
journalctl -u nginx
journalctl -u postgresql
journalctl -u mon-api

# Suivi temps réel
journalctl -u nginx -f

# Dernières 50 lignes
journalctl -u nginx -n 50

# Depuis hier
journalctl -u nginx --since yesterday

# Erreurs seulement
journalctl -u nginx -p err

# Logs de plusieurs services
journalctl -u nginx -u php-fpm

# Depuis le dernier démarrage du service
journalctl -u nginx --since "$(systemctl show nginx -p ActiveEnterTimestamp --value)"
```

---

## Combiner avec grep

```bash
journalctl -u nginx | grep "502"
journalctl -u mon-api --since "1 hour ago" | grep -i "error"

# En JSON pour parsing
journalctl -u mon-api -o json | jq '.MESSAGE' | tail -20
```
