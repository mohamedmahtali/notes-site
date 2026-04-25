---
title: Docker volumes
tags:
  - beginner
---

# Docker volumes

---

## Définition

Par défaut, le filesystem d'un conteneur est **éphémère** — les données sont perdues à la suppression du conteneur. Les [[Volumes]] [[Docker]] fournissent du stockage **persistant** et indépendant du cycle de vie du conteneur.

---

## Types de montage

| Type | Syntaxe | Usage |
|---|---|---|
| [[Named volumes\|Named volume]] | `-v nom:/chemin` | Stockage persistant géré par Docker |
| [[Bind mounts\|Bind mount]] | `-v /hôte:/conteneur` | Monter un dossier de l'hôte |
| `tmpfs` | `--tmpfs /chemin` | RAM uniquement (temporaire, sécurisé) |

---

## Commandes

```bash
# Créer un volume nommé
docker volume create pgdata

# Lister les volumes
docker volume ls

# Inspecter un volume
docker volume inspect pgdata

# Supprimer un volume
docker volume rm pgdata

# Supprimer les volumes non utilisés
docker volume prune

# Monter un volume
docker run -v pgdata:/var/lib/postgresql/data postgres:16

# Bind mount
docker run -v $(pwd)/src:/app/src mon-app
```

---

## Exemple – base de données persistante

```bash
docker volume create pgdata

docker run -d   --name postgres   -e POSTGRES_PASSWORD=secret   -v pgdata:/var/lib/postgresql/data   postgres:16

# Supprimer le conteneur → les données restent dans pgdata
docker rm -f postgres
docker run -d --name postgres -v pgdata:/var/lib/postgresql/data postgres:16
# → même données qu'avant
```
