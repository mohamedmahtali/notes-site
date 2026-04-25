---
title: Unit files
tags:
  - intermediate
---

# Unit files

---

## Définition

Un unit file est un fichier de configuration INI qui définit une unité [[systemd]] (service, timer, socket, etc.). Les unit files système sont dans `/lib/systemd/system/` ; les custom sont dans `/etc/systemd/system/` (priorité plus haute).

---

## Structure complète

```ini
[Unit]
Description=Nom descriptif du service
Documentation=https://mon-app.example.com/docs
After=network.target postgresql.service    # ordre de démarrage
Requires=postgresql.service               # dépendance stricte
Wants=redis.service                        # dépendance souple

[Service]
Type=simple          # simple|forking|notify|oneshot|idle
User=appuser
Group=appgroup
WorkingDirectory=/opt/mon-app

# Commandes
ExecStartPre=/usr/bin/env /opt/mon-app/pre-start.sh
ExecStart=/usr/bin/node /opt/mon-app/server.js
ExecStop=/bin/kill -TERM $MAINPID
ExecReload=/bin/kill -HUP $MAINPID

# Environnement
Environment=NODE_ENV=production
EnvironmentFile=/etc/mon-app/env

# Redémarrage
Restart=on-failure
RestartSec=10s
StartLimitIntervalSec=60s
StartLimitBurst=3

# Ressources
LimitNOFILE=65536
MemoryLimit=512M

[Install]
WantedBy=multi-user.target
```

---

## Emplacements

```bash
/lib/systemd/system/     # packages système (ne pas modifier)
/etc/systemd/system/     # custom et overrides (modifier ici)

# Override partiel d'un service existant
systemctl edit nginx     # crée /etc/systemd/system/nginx.service.d/override.conf
```
