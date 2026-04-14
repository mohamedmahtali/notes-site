---
title: systemd
tags:
  - intermediate
---

# systemd

## Parent
- [[Linux]]

## Enfants
- [[Services]]
- [[journalctl]]
- [[Timers]]

---

## Définition

systemd est le système d'init et de gestion des services de la plupart des distributions Linux modernes (Ubuntu, Debian, RHEL, CentOS…). Il démarre les services au boot, les surveille, les redémarre en cas de crash, et centralise les logs via journald.

---

## Commandes essentielles

```bash
# Gestion des services
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx          # rechargement de config (si supporté)
systemctl status nginx          # état détaillé

# Activation au démarrage
systemctl enable nginx          # activer au boot
systemctl disable nginx         # désactiver au boot
systemctl is-enabled nginx      # vérifier

# Voir tous les services
systemctl list-units --type=service
systemctl list-units --type=service --state=failed

# Recharger la config systemd (après modification d'un unit file)
systemctl daemon-reload
```

---

## Inspecter l'état

```bash
# État global du système
systemctl is-system-running    # running / degraded / starting

# Services en échec
systemctl --failed

# Dépendances d'un service
systemctl list-dependencies nginx
```
