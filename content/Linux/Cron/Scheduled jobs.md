---
title: Scheduled jobs
tags:
  - advanced
---
# Scheduled jobs

## Parent
- [[Cron]]

## Enfants
...

## Concepts liés
- [[Cron]]
- [[Timers]]
- [[Schedule trigger]]

# Définition

Un **scheduled job** est une **tâche configurée pour s’exécuter automatiquement à un moment précis ou selon un intervalle défini**.

Sous Linux, ces tâches sont généralement exécutées par :

- **Cron**
- **systemd timers**
- parfois **at / batch** pour les tâches uniques

Un scheduled job est composé de :

1. **un déclencheur temporel** (schedule)
2. **une commande ou un script**
3. **un environnement d’exécution**

Exemple :
```bash
0 2 * * * /usr/local/bin/backup.sh
```
Cette tâche exécutera le script **tous les jours à 02:00**.

---

# Pourquoi c'est important

Les scheduled jobs sont fondamentaux dans les systèmes Linux car ils permettent **d’automatiser la maintenance et les opérations répétitives**.

---

### Automatisation des tâches

Exemples typiques :

- backups
- rotation des logs
- synchronisation de fichiers
- nettoyage du système
- monitoring

---

### Maintenance système

Beaucoup de systèmes utilisent des scheduled jobs pour :

- mettre à jour des bases de données
- nettoyer `/tmp`
- renouveler des certificats SSL
- générer des rapports

---

### Infrastructure DevOps

Dans les environnements DevOps, les scheduled jobs servent à :

- lancer des pipelines
- effectuer des backups cloud
- synchroniser des données
- envoyer des métriques

---

# Types de scheduled jobs

### Jobs récurrents

Ils s’exécutent **à intervalles réguliers**.

Exemples :
```bash
*/5 * * * * script.sh
```
Toutes les **5 minutes**.

---

### Jobs quotidiens
```bash
0 3 * * * script.sh
```
Tous les jours à **03:00**.

---

### Jobs hebdomadaires
```bash
0 2 * * 0 script.sh
```
Chaque **dimanche à 02:00**.

---

### Jobs mensuels
```bash
0 1 1 * * script.sh
```
Le **1er jour du mois à 01:00**.

---

# Commandes utiles

### Voir les tâches planifiées
```bash
crontab -l
```
---

### Modifier les scheduled jobs
```bash
crontab -e
```
---

### Supprimer les tâches
```bash
crontab -r
```
---

# Exemple réel DevOps

### Backup quotidien
```bash
0 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```
Processus :

1. cron vérifie les schedules chaque minute
2. à **02:00** il déclenche le job
3. le script backup s’exécute
4. la sortie est enregistrée dans les logs

---

### Nettoyage automatique des logs
```bash
0 4 * * 0 /usr/local/bin/cleanup_logs.sh
```
Chaque **dimanche à 04:00**.