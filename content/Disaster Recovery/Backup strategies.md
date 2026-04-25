---
title: Backup strategies
tags:
  - reliability
  - intermediate
---

# Backup strategies

## Définition

Une stratégie de backup définit comment, quand et où les données sont sauvegardées pour permettre une restauration en cas de sinistre. Elle est dimensionnée par le RPO cible.

> [!tip] La règle 3-2-1
> 3 copies des données, sur 2 [[Types]] de supports différents, dont 1 hors site (ou hors ligne). C'est la règle d'or des backups.

## Types de sauvegardes

| Type | Sauvegarde | Vitesse backup | Vitesse restore | Espace |
|------|-----------|----------------|-----------------|--------|
| Complète | Toutes les données | Lent | Rapide | Grand |
| Incrémentale | Changements depuis le dernier backup | Rapide | Lent | Petit |
| Différentielle | Changements depuis le dernier backup complet | Moyen | Moyen | Moyen |

## Outils courants

| Outil | Usage | Forces |
|-------|-------|--------|
| `rsync` | Fichiers [[Linux]], scripts [[Cron]] | Simple, universel |
| `pg_dump` / `pg_basebackup` | PostgreSQL | Natif, PITR |
| `mysqldump` / `xtrabackup` | MySQL | xtrabackup = online sans lock |
| Velero | [[Kubernetes]] ([[Pods]] + PVCs) | Backup/restore complet de namespace |
| Restic | Fichiers + [[Cloud]] (S3, B2, GCS...) | Déduplication, chiffrement natif |
| [[AWS]] Backup | [[Services]] AWS (RDS, EFS, [[EC2]]...) | Centralisé, cross-région |

## Backup PostgreSQL

```bash
# Dump logique (export SQL)
pg_dump -U postgres mydb > backup_$(date +%Y%m%d).sql

# Restore
psql -U postgres mydb < backup_20240115.sql

# Backup physique continu (WAL archiving) — dans postgresql.conf
archive_mode = on
archive_command = 'aws s3 cp %p s3://my-backups/wal/%f'

# Point-in-time recovery (PITR) — restaurer à un instant précis
restore_command = 'aws s3 cp s3://my-backups/wal/%f %p'
recovery_target_time = '2024-01-15 14:30:00'
```

## Backup Kubernetes avec Velero

```bash
# Installer Velero avec stockage S3
velero install \
  --provider aws \
  --bucket my-velero-backups \
  --backup-location-config region=eu-west-1

# Backup d'un namespace entier
velero backup create prod-backup --include-namespaces=production

# Planifier un backup quotidien à 2h
velero schedule create daily-backup \
  --schedule="0 2 * * *" \
  --include-namespaces=production \
  --ttl 720h

# Restaurer
velero restore create --from-backup prod-backup
```

## Backup fichiers avec Restic

```bash
# Initialiser un repo S3
export RESTIC_REPOSITORY=s3:s3.amazonaws.com/my-backups
export RESTIC_PASSWORD=mysecretpassword
restic init

# Backup d'un dossier
restic backup /var/data

# Lister les snapshots
restic snapshots

# Restaurer le dernier snapshot
restic restore latest --target /var/data-restored

# Politique de rétention (garder 7 quotidiens, 4 hebdo, 12 mensuels)
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune
```

> [!warning] Tester les restores régulièrement
> Un backup non testé n'est pas un backup — c'est un espoir. Planifier des tests de restauration automatisés (au moins mensuels) et mesurer le RTO réel.

## Liens

- [[Full backup]]
- [[Incremental backup]]
- [[3-2-1 rule]]
- [[Disaster Recovery]]
