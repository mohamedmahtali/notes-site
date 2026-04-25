---
title: Log filtering
tags:
  - intermediate
---

# Log filtering

---

## Définition

[[journalctl]] offre des capacités de filtrage puissantes sur les logs structurés : par priorité, par service, par temps, par champ, ou par expression. C'est l'outil idéal pour diagnostiquer des incidents.

---

## Filtres courants

```bash
# Par priorité (0=emerg → 7=debug)
journalctl -p 0..3    # emerg, alert, crit, err
journalctl -p err     # erreurs seulement
journalctl -p warning # avertissements et au-dessus

# Par temps
journalctl --since "2024-01-15 10:00" --until "2024-01-15 11:00"
journalctl --since "30 min ago"

# Par utilisateur
journalctl _UID=1000
journalctl _SYSTEMD_USER_UNIT=mon-service.service

# Par exécutable
journalctl /usr/sbin/nginx
journalctl /usr/bin/python3

# Par PID
journalctl _PID=12345

# Combiner
journalctl -u nginx -p err --since yesterday

# Afficher le contexte (lignes avant/après)
journalctl -u nginx | grep -B2 -A2 "error"
```

---

## Format de sortie

```bash
journalctl -o short          # format classique
journalctl -o short-precise  # avec microsecondes
journalctl -o json           # JSON (une entrée par ligne)
journalctl -o json-pretty    # JSON indenté
journalctl -o cat            # message brut seulement
```
