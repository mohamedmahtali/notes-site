---
title: Full backup
tags: [reliability, beginner]
---

# Full backup (Sauvegarde complète)

## Définition

Un backup complet copie l'intégralité des données à un instant T. C'est la base de toute stratégie de backup : simple à restaurer, mais long à créer et volumineux.

> [!note] Fréquence recommandée
> Hebdomadaire pour la plupart des systèmes, quotidien pour les données critiques. Les backups complets sont souvent combinés avec des backups incrementaux.

## Exemples de backup complet

```bash
# Backup base PostgreSQL
pg_dump -h localhost -U postgres mydb > backup_$(date +%Y%m%d).sql

# Backup complet avec compression
pg_dump mydb | gzip > backup_$(date +%Y%m%d_%H%M).sql.gz

# Backup tous les schemas
pg_dumpall > all_databases_$(date +%Y%m%d).sql

# Backup volume Docker
docker run --rm   -v myapp_data:/data   -v $(pwd):/backup   alpine tar czf /backup/data_$(date +%Y%m%d).tar.gz /data

# Backup S3 (sync complet)
aws s3 sync s3://mybucket/ ./backup/
```

## Vérification du backup

```bash
# TOUJOURS tester la restauration !
pg_restore -d testdb backup_20240101.sql

# Vérifier l'intégrité
md5sum backup_20240101.sql.gz > backup_20240101.md5
md5sum -c backup_20240101.md5
```

## Liens

- [[Backup strategies]]
- [[Incremental backup]]
- [[3-2-1 rule]]
