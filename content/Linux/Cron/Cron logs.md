---
title: Cron logs
tags:
  - advanced
---
# Cron logs

## Parent
- [[Cron]]

## Enfants
...

## Concepts liés
- [[Cron]]
- [[Logs]]
- [[journalctl]]

- - - 
## Définition
Les **Cron logs** sont les **journaux générés par le service Cron** lorsqu'il exécute des tâches planifiées (cron jobs).

Ils enregistrent notamment :
- le moment où une tâche est exécutée
- l’utilisateur qui exécute la tâche
- la commande lancée
- parfois les erreurs ou sorties du script

Ces logs permettent de **vérifier que les tâches planifiées fonctionnent correctement**.

Selon la distribution Linux, les logs Cron se trouvent généralement dans :

```bash
/var/log/syslog
```
ou
```bash
/var/log/cron
```

- - - 
## Pourquoi c'est important

Les Cron logs sont essentiels pour :
### 1️⃣ Vérifier qu'un job s’exécute bien
Si une tâche ne fonctionne pas, les logs permettent de confirmer si **cron l’a réellement lancée**.

---
### 2️⃣ Déboguer un script
Beaucoup de problèmes viennent du fait que :
- le PATH est différent
- les permissions sont incorrectes
- un script échoue silencieusement
Les logs permettent de **voir exactement ce qui s'est passé**.

---
### 3️⃣ Surveiller les tâches automatiques
Dans un environnement **DevOps / production**, de nombreuses tâches sont automatisées :
- backups
- rotations de logs
- synchronisations
- scripts de maintenance
Les logs permettent de **surveiller ces automatisations**.

- - - 
## Exemple
### Exemple de ligne de log Cron
Dans `/var/log/syslog` :
```bash
Mar  7 10:00:01 server CRON[12345]: (root) CMD (/usr/local/bin/backup.sh)
```

Signification :

| Élément        | Signification     |
| -------------- | ----------------- |
| Mar 7 10:00:01 | date et heure     |
| server         | nom de la machine |
| CRON[12345]    | processus cron    |
| (root)         | utilisateur       |
| CMD            | commande exécutée |

---

### Voir les logs Cron

#### Sur Debian / Ubuntu
```bash
grep CRON /var/log/syslog
```
ou
```bash
tail -f /var/log/syslog | grep CRON
```
---
#### Avec systemd
```bash
journalctl -u cron
```
ou en temps réel :
```bash
journalctl -u cron -f
```
---
### Capturer la sortie d’un cron job

Par défaut, **cron ne sauvegarde pas la sortie d’un script**.

On redirige donc la sortie :
```bash
* * * * * /script.sh >> /var/log/script.log 2>&1
```
Signification :

| Partie | Signification        |
| ------ | -------------------- |
| `>>`   | ajoute au log        |
| `2>&1` | redirige les erreurs |

---
### Exemple réel DevOps

Cron job pour backup quotidien :

```bash
0 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```
Tous les jours à **02:00** :

1. cron lance `backup.sh`
2. la sortie est écrite dans `/var/log/backup.log`
3. les erreurs sont aussi enregistrées