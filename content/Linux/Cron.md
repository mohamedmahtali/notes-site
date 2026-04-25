---
title: Cron
tags:
  - intermediate
---

# Cron

---

## Définition

Cron est le daemon de planification de tâches [[Linux]]. Il exécute des commandes ou scripts à des moments définis (périodiquement ou à des horaires précis). Chaque utilisateur peut avoir sa propre crontab.

---

## Commandes

```bash
# Éditer la crontab de l'utilisateur courant
crontab -e

# Lister les tâches cron
crontab -l

# Supprimer toutes les tâches cron
crontab -r

# Crontab d'un autre utilisateur (root)
crontab -u deploy -e
crontab -u deploy -l

# Fichiers système
/etc/crontab              # crontab système (avec champ utilisateur)
/etc/cron.d/              # fichiers de cron par application
/etc/cron.daily/          # scripts exécutés chaque jour
/etc/cron.weekly/         # scripts exécutés chaque semaine
/etc/cron.monthly/        # scripts exécutés chaque mois
```

---

## Exemple rapide

```cron
# Backup chaque jour à 2h30
30 2 * * * /opt/scripts/backup.sh

# Nettoyage chaque lundi à minuit
0 0 * * 1 find /tmp -mtime +7 -delete

# Rapport toutes les heures
0 * * * * /opt/scripts/hourly-report.sh >> /var/log/report.log 2>&1
```
