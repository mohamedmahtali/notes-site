---
title: Règle 3-2-1
tags: [reliability, beginner]
---

# Règle 3-2-1 des backups

## Définition

La règle 3-2-1 est le standard de l'industrie pour les stratégies de backup :
- **3** copies des données (1 production + 2 backups)
- **2** types de supports différents (disque + cloud, ou disque + bande)
- **1** copie hors site ou hors ligne (protection contre sinistre local)

> [!tip] Pourquoi cette règle ?
> Un backup sur le même serveur que la production ne protège pas contre la panne du serveur. Un backup uniquement local ne protège pas contre l'incendie, l'inondation ou le ransomware.

## Application pratique

```
Production DB (copy 1)
    │
    ├── Backup local quotidien (copy 2) — support: NAS local
    │   /backups/daily/
    │
    └── Backup cloud hebdomadaire (copy 3) — support: S3
        s3://company-backups/weekly/
        ↑
        Hors site = protège contre sinistre physique
```

## Exemple d'implémentation

```bash
#!/bin/bash
# backup-321.sh

DATE=$(date +%Y%m%d_%H%M)

# Copy 2 : backup local
pg_dump mydb | gzip > /backups/local/db_${DATE}.sql.gz

# Copy 3 : upload vers S3 (hors site)
aws s3 cp /backups/local/db_${DATE}.sql.gz   s3://company-backups/db/${DATE}/

# Nettoyage des anciens backups locaux (garder 7 jours)
find /backups/local/ -name "*.sql.gz" -mtime +7 -delete

echo "✅ Backup 3-2-1 terminé : ${DATE}"
```

## Extension 3-2-1-1-0

La règle moderne ajoute :
- **1** copie immuable (air-gapped ou WORM storage)
- **0** erreur de vérification (tester les restaurations automatiquement)

## Liens

- [[Backup strategies]]
- [[Full backup]]
- [[Incremental backup]]
- [[Disaster Recovery]]
