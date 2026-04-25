---
title: Scheduled jobs
tags:
  - intermediate
---

# Scheduled jobs

---

## Définition

Les tâches planifiées (scheduled jobs) sont des scripts ou commandes exécutés automatiquement à des horaires définis. En [[Linux]], [[Cron]] est le mécanisme principal, mais les [[Timers|timers systemd]] sont une alternative plus robuste.

---

## Bonnes pratiques

```bash
# 1. Toujours rediriger les sorties
0 2 * * * /opt/backup.sh >> /var/log/backup.log 2>&1

# 2. Utiliser des chemins absolus
0 2 * * * /usr/bin/python3 /opt/scripts/backup.py

# 3. Définir l'environnement si nécessaire
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
HOME=/root

0 2 * * * /opt/backup.sh

# 4. Envoyer les erreurs par email
MAILTO=admin@example.com
0 2 * * * /opt/backup.sh

# 5. Éviter les exécutions simultanées avec flock
*/5 * * * * flock -n /tmp/script.lock /opt/script.sh
```

---

## Tâches courantes

```cron
# Backup DB quotidien
0 2 * * * pg_dump mydb > /backup/$(date +%Y%m%d).sql

# Nettoyage des logs anciens
0 3 * * 0 find /var/log -name "*.log" -mtime +30 -delete

# Renouvellement certificat SSL
0 0,12 * * * certbot renew --quiet

# Healthcheck
*/5 * * * * curl -sf http://localhost/health || systemctl restart app
```
