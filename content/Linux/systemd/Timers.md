---
title: Timers
tags:
  - intermediate
---

# Timers

## Parent
- [[systemd]]

---

## Définition

Les timers systemd sont une alternative aux crons. Ils permettent de planifier l'exécution de services (`.service`) à des moments précis ou à intervalles réguliers. Avantage sur cron : logs dans journald, gestion des dépendances, et rattrapage des exécutions manquées.

---

## Créer un timer

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Backup quotidien

[Timer]
# Tous les jours à 2h du matin
OnCalendar=*-*-* 02:00:00

# Ou à des intervalles relatifs
# OnBootSec=10min        # 10 min après le boot
# OnUnitActiveSec=1h     # 1h après la dernière exécution

# Rattraper si le système était éteint
Persistent=true

[Install]
WantedBy=timers.target
```

```ini
# /etc/systemd/system/backup.service
[Unit]
Description=Script de backup

[Service]
Type=oneshot
ExecStart=/opt/scripts/backup.sh
User=backup
```

```bash
systemctl daemon-reload
systemctl enable backup.timer
systemctl start backup.timer
```

---

## Syntaxe OnCalendar

```
*-*-* *:*:*     # chaque seconde
*-*-* HH:MM:SS  # chaque jour à HH:MM:SS
Mon *-*-* 09:00 # chaque lundi à 9h
weekly          # chaque semaine
daily           # chaque jour à minuit
hourly          # chaque heure
```

---

## Gestion

```bash
# Lister les timers
systemctl list-timers

# Voir le prochain déclenchement
systemctl list-timers --all | grep backup

# Logs du timer
journalctl -u backup.timer
journalctl -u backup.service
```
