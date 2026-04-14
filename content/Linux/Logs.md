---
title: Logs
tags:
  - intermediate
---

# Logs

## Parent
- [[Linux]]

## Enfants
- [[Syslog]]
- [[Application logs]]
- [[Audit logs]]
- [[logrotate]]

---

## Définition

Les logs Linux sont des fichiers texte ou des entrées de journal qui enregistrent les événements système, applicatifs, et de sécurité. Ils sont essentiels pour le diagnostic, l'audit, et la surveillance.

---

## Emplacements principaux

```
/var/log/
├── syslog         ← messages système généraux (Debian/Ubuntu)
├── messages       ← messages système généraux (RHEL/CentOS)
├── auth.log       ← authentification et sudo
├── kern.log       ← messages kernel
├── dmesg          ← boot et drivers
├── nginx/
│   ├── access.log
│   └── error.log
├── mysql/error.log
└── apt/history.log
```

---

## Commandes

```bash
# Lire un log
cat /var/log/syslog
tail -f /var/log/syslog     # suivi temps réel
tail -n 100 /var/log/auth.log

# Filtrer
grep "ERROR" /var/log/app.log
grep "Failed password" /var/log/auth.log

# Messages kernel depuis le boot
dmesg
dmesg | tail -20
dmesg -T    # avec timestamps lisibles

# systemd logs (voir journalctl)
journalctl -f
journalctl -u nginx
```
