---
title: Services
tags:
  - intermediate
---

# Services

## Parent
- [[systemd]]

## Enfants
- [[Unit files]]
- [[Restart policies]]
- [[Dependencies]]
- [[Targets]]

---

## Définition

Un service systemd est une unité (unit) de type `.service` qui définit comment démarrer, arrêter, et gérer un processus. systemd gère le cycle de vie complet : démarrage automatique, surveillance, redémarrage en cas d'échec, et logging.

---

## Commandes

```bash
systemctl start mon-service
systemctl stop mon-service
systemctl restart mon-service
systemctl reload mon-service    # si supporté par le service
systemctl status mon-service    # état + derniers logs
systemctl enable mon-service    # démarrage automatique au boot
systemctl disable mon-service

# Voir les logs du service
journalctl -u mon-service
journalctl -u mon-service -f    # suivi temps réel
journalctl -u mon-service --since "1 hour ago"
```

---

## Exemple de service

```ini
# /etc/systemd/system/mon-api.service
[Unit]
Description=Mon API Node.js
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/mon-api
ExecStart=/usr/bin/node server.js
Restart=on-failure
RestartSec=5s
Environment=NODE_ENV=production
Environment=PORT=3000

[Install]
WantedBy=multi-user.target
```

```bash
# Activer le nouveau service
systemctl daemon-reload
systemctl enable mon-api
systemctl start mon-api
```
