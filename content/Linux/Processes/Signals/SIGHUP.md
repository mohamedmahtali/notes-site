---
title: SIGHUP
tags:
  - intermediate
---
# SIGHUP

---

## Définition

SIGHUP (signal 1, "Hang Up") était historiquement envoyé quand un terminal se déconnectait. Aujourd'hui, les daemons l'utilisent comme convention pour **recharger leur configuration** sans redémarrer.

---

## Pourquoi c'est important

> [!tip] Reload sans downtime
> Envoyer SIGHUP à [[Nginx]], Apache, ou sshd recharge la configuration à chaud — zéro connexion perdue, zéro temps d'arrêt. C'est la façon standard de mettre à jour la config d'un service en production.

---

## Utilisation

```bash
# Recharger la config nginx
kill -HUP $(cat /var/run/nginx.pid)
pkill -HUP nginx
nginx -s reload              # équivalent

# Recharger sshd
kill -HUP $(cat /var/run/sshd.pid)

# Recharger rsyslog
kill -HUP $(pgrep rsyslogd)

# Via systemd (préféré)
systemctl reload nginx       # envoie SIGHUP en interne
```

---

## SIGHUP et les processus en arrière-plan

```bash
# nohup empêche SIGHUP de tuer un processus quand le terminal se ferme
nohup ./long-running-script.sh &

# screen/tmux protègent aussi les sessions contre SIGHUP
```

---

> [!note]
> Tous les daemons ne réagissent pas à SIGHUP de la même façon. Consulter la documentation du service avant d'envoyer le signal.
