---
title: Service accounts
tags:
  - intermediate
---

# Service accounts

---

## Définition

Un compte de service est un utilisateur système créé pour exécuter un service applicatif ([[Nginx]], postgres, app). Il n'a pas de [[Shell]] interactif, pas de home directory réel, et ses [[Permissions]] sont limitées au strict nécessaire — principe du moindre privilège.

---

## Création

```bash
# Utilisateur système (sans home, sans shell)
useradd --system --no-create-home --shell /sbin/nologin appuser

# Ou avec des options explicites
adduser --system --group --no-create-home --shell /usr/sbin/nologin appuser

# Vérifier
grep "appuser" /etc/passwd
# appuser:x:999:999::/home/appuser:/usr/sbin/nologin
```

---

## Configurer un service systemd avec un compte de service

```ini
[Service]
User=appuser
Group=appgroup
# Le service tourne avec les permissions minimales de appuser
```

---

## Permissions typiques

```bash
# Fichiers de l'application appartenant au service account
chown -R appuser:appgroup /opt/mon-app
chmod 750 /opt/mon-app

# Logs
chown appuser:appgroup /var/log/mon-app/

# Seule la config est en lecture
chown root:appgroup /etc/mon-app/config.yaml
chmod 640 /etc/mon-app/config.yaml
```

---

> [!tip]
> Ne jamais faire tourner un service web, une API, ou une DB en tant que `root`. En cas de compromission, l'attaquant n'a que les droits du compte de service.
