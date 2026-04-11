---
title: Crontab syntax
tags:
  - advanced
---
# Crontab syntax

## Parent
- [[Cron]]

## Enfants
...

## Concepts liés
- [[Cron]]
- [[Scheduled jobs]]
- [[Timers]]

# Définition

La **crontab syntax** est la **structure utilisée pour définir quand un cron job doit s’exécuter .

Une entrée crontab est composée de **5 champs temporels + une commande**.

Format général :
```bash
* * * * * command_to_execute
```
Structure :
```bash
┌──────── minute (0 - 59)  
│ ┌────── heure (0 - 23)  
│ │ ┌──── jour du mois (1 - 31)  
│ │ │ ┌── mois (1 - 12)  
│ │ │ │ ┌ jour de la semaine (0 - 7) (0 et 7 = dimanche)  
│ │ │ │ │  
* * * * * command
```
---

# Pourquoi c'est important

La syntaxe crontab est essentielle car elle permet de :
### Automatiser des tâches

Exemples :
- backups
- nettoyage de logs
- synchronisations
- monitoring
- déploiements automatiques

---

### Construire des infrastructures autonomes

Dans un environnement **DevOps**, cron est souvent utilisé pour :

- scripts de maintenance
- rotation de logs
- tâches de batch
- synchronisation de données

---

### Comprendre les automatisations existantes

Sur beaucoup de serveurs Linux, **des dizaines de tâches cron tournent déjà**.

Comprendre la syntaxe permet de :

- les lire
- les modifier
- les dépanner

---

# Valeurs possibles

| Symbole | Signification      |
| ------- | ------------------ |
| `*`     | toutes les valeurs |
| `,`     | liste de valeurs   |
| `-`     | intervalle         |
| `/`     | pas (step)         |

---

### Exemples

#### Toutes les minutes
```bash
* * * * * script.sh
```
---

#### Toutes les heures
```bash
0 * * * * script.sh
```
---

#### Tous les jours à 02:00
```bash
0 2 * * * backup.sh
```
---

#### Tous les lundis
```bash
0 3 * * 1 script.sh
```
---

#### Toutes les 5 minutes
```bash
*/5 * * * * script.sh
```
---

#### Toutes les 10 minutes entre 9h et 18h
```bash
*/10 9-18 * * * script.sh
```
---

# Commandes utiles

### Voir la crontab de l’utilisateur
```bash
crontab -l
```
---

### Modifier la crontab
```bash
crontab -e
```
---

### Supprimer la crontab
```bash
crontab -r
```
---

### Voir la crontab d’un autre utilisateur
```bash
crontab -u user -l
```
---

# Exemple réel DevOps

Backup tous les jours à 02:30 :
```bash
30 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```
Processus :

1. cron lit la crontab
2. à 02:30 il exécute le script
3. la sortie est enregistrée dans un log
