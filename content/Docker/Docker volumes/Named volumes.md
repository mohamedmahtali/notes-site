---
title: Named volumes
tags:
  - beginner
---

# Named volumes

---

## Définition

Un volume nommé est un volume créé et géré par [[Docker]], stocké dans `/var/lib/docker/volumes/` sur l'hôte. Il est identifié par un nom, indépendant de tout conteneur, et persiste jusqu'à sa suppression explicite.

---

## Commandes

```bash
# Créer un volume
docker volume create mydata

# Utiliser un volume
docker run -v mydata:/app/data mon-app

# Le volume est créé automatiquement s'il n'existe pas
docker run -v pgdata:/var/lib/postgresql/data postgres:16

# Inspecter
docker volume inspect pgdata
# → Mountpoint: /var/lib/docker/volumes/pgdata/_data

# Lister
docker volume ls

# Supprimer
docker volume rm mydata
docker volume prune    # supprimer les non utilisés
```

---

## En Docker Compose

```yaml
services:
  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:    # déclarer le volume nommé
```

---

## Named volume vs Bind mount

| Critère | Named volume | Bind mount |
|---|---|---|
| Géré par | Docker | OS/utilisateur |
| Localisation | `/var/lib/docker/volumes/` | N'importe quel chemin |
| [[Permissions]] | Docker les gère | Dépend du FS hôte |
| Usage | Données persistantes | Dev (code source) |
