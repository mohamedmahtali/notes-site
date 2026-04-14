---
title: Syslog
tags:
  - intermediate
---

# Syslog

## Parent
- [[Logs]]

---

## Définition

Syslog est le protocole et le daemon standard de logging Unix/Linux. Il collecte les messages de toutes les applications et services, et les distribue vers des fichiers, serveurs distants, ou la console selon des règles de filtrage.

---

## Implémentations

| Daemon | Distribution | Notes |
|---|---|---|
| rsyslog | Ubuntu, Debian, RHEL | Standard actuel |
| syslog-ng | Option alternative | Plus de fonctionnalités |
| journald | Tous (systemd) | Remplace progressivement syslog |

---

## Niveaux de priorité

| Level | Numéro | Usage |
|---|---|---|
| emerg | 0 | Système inutilisable |
| alert | 1 | Action immédiate requise |
| crit | 2 | Condition critique |
| err | 3 | Erreurs |
| warning | 4 | Avertissements |
| notice | 5 | Condition normale mais notable |
| info | 6 | Informationnel |
| debug | 7 | Debug |

---

## Configuration rsyslog

```bash
# /etc/rsyslog.conf
# facility.level   destination
*.info;mail.none    /var/log/messages
auth,authpriv.*     /var/log/auth.log
mail.*              /var/log/mail.log
kern.*              /var/log/kern.log
*.emerg             :omusrmsg:*    # notifier tous les utilisateurs

# Envoyer vers un serveur central
*.* @syslog-server:514    # UDP
*.* @@syslog-server:514   # TCP
```
