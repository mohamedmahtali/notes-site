---
title: logrotate
tags:
  - intermediate
---

# logrotate

## Parent
- [[Logs]]

---

## Définition

`logrotate` automatise la rotation des fichiers de logs : archivage, compression, suppression des anciens fichiers. Sans logrotate, les logs grossissent indéfiniment et saturent le disque.

---

## Configuration

```bash
# /etc/logrotate.conf (configuration globale)
# /etc/logrotate.d/ (configurations par application)

# Exemple : /etc/logrotate.d/nginx
/var/log/nginx/*.log {
    daily             # rotation quotidienne
    missingok         # pas d'erreur si le fichier manque
    rotate 14         # garder 14 fichiers
    compress          # compresser avec gzip
    delaycompress     # compresser la rotation précédente (pas la courante)
    notifempty        # ne pas rotater si vide
    create 0640 www-data adm   # permissions du nouveau fichier
    sharedscripts
    postrotate
        nginx -s reopen   # demander à nginx d'ouvrir un nouveau fichier
    endscript
}
```

---

## Commandes

```bash
# Tester la configuration (sans exécuter)
logrotate -d /etc/logrotate.d/nginx

# Forcer la rotation (utile pour tester)
logrotate -f /etc/logrotate.d/nginx

# Voir l'état des rotations
cat /var/lib/logrotate/status

# Lancer manuellement (normalement via cron/systemd timer)
logrotate /etc/logrotate.conf
```
