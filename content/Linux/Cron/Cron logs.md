---
title: Cron logs
tags:
  - intermediate
---
# Cron logs

## Parent
- [[Cron]]

---

## Définition

Les logs cron enregistrent chaque exécution de tâche planifiée — succès, échec, et sortie standard. Sur les systèmes systemd, ils transitent par journald ; sur les systèmes syslog traditionnels, ils vont dans `/var/log/syslog` ou `/var/log/cron`.

---

## Pourquoi c'est important

> [!tip] Déboguer sans logs = aveugle
> Si un cron ne tourne pas comme prévu, les logs sont le premier endroit à consulter. Sans eux, impossible de savoir si la tâche a été déclenchée, si elle a échoué, ou si la sortie a été silencieusement ignorée.

---

## Consulter les logs cron

```bash
# Sur systemd (Ubuntu 20.04+, Debian 10+)
journalctl -u cron
journalctl -u cron --since "1 hour ago"
journalctl -u crond -f          # follow en temps réel

# Sur syslog traditionnel
grep CRON /var/log/syslog
grep CRON /var/log/cron          # RedHat/CentOS

# Voir les N dernières lignes
tail -100 /var/log/syslog | grep CRON
```

---

## Capturer la sortie d'un job

Par défaut, cron envoie la sortie par email (si configuré). Pour capturer dans un fichier :

```bash
# Dans la crontab
0 * * * * /opt/script.sh >> /var/log/myjob.log 2>&1

# Avec timestamp
0 * * * * echo "$(date): start" >> /var/log/myjob.log && /opt/script.sh >> /var/log/myjob.log 2>&1
```

---

> [!note]
> `2>&1` redirige stderr vers stdout pour capturer les erreurs aussi. Sans cela, les erreurs sont perdues ou envoyées par email.
