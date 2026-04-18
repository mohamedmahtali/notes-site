---
title: Incremental backup
tags: [reliability, intermediate]
---

# Incremental backup (Sauvegarde incrémentale)

## Définition

Un backup incrémental ne sauvegarde que les données modifiées depuis le **dernier backup** (qu'il soit complet ou incrémental). Rapide et économe en espace, mais la restauration nécessite le backup complet + tous les incrementaux.

> [!note] Stratégie GFS (Grandfather-Father-Son)
> Une stratégie courante : backup complet hebdomadaire (Father), backup incrémental quotidien (Son), archivage mensuel (Grandfather). Balance entre espace disque et temps de restauration.

## Avec rsync

```bash
# Backup incrémental avec rsync (hard links pour les fichiers inchangés)
rsync -a --link-dest=../backup-yesterday/   /data/   /backups/backup-$(date +%Y%m%d)/

# Résultat : seuls les fichiers modifiés sont copiés
# Les fichiers inchangés sont des hard links (0 espace supplémentaire)
```

## PostgreSQL WAL (Write-Ahead Log)

```bash
# Point-In-Time Recovery (PITR) — backup incrémental PostgreSQL natif
# Configurer postgresql.conf :
archive_mode = on
archive_command = 'cp %p /backups/wal/%f'
wal_level = replica

# Restaurer à un point précis
recovery_target_time = '2024-01-15 14:30:00'
```

## Liens

- [[Backup strategies]]
- [[Full backup]]
- [[3-2-1 rule]]
