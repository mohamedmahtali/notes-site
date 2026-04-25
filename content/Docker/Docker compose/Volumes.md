---
title: Volumes
tags:
  - beginner
---

# Volumes

---

## Définition

[[Docker compose]] permet de déclarer des volumes nommés dans la section `volumes` du fichier. Ces volumes sont créés automatiquement et persistent entre les redémarrages de la stack (`docker compose down` sans `-v`).

---

## Syntaxe

```yaml
services:
  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data      # volume nommé
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql  # bind mount
      - /tmp/pg-temp:/tmp                    # bind mount absolu

  api:
    image: mon-app
    volumes:
      - logvol:/var/log/app

volumes:
  pgdata:               # volume nommé simple
  logvol:
    driver: local
    driver_opts:
      type: none
      device: /mnt/logs
      o: bind
```

---

## Comportement de down

```bash
# Stopper sans supprimer les volumes (données préservées)
docker compose down

# Stopper ET supprimer les volumes (reset complet)
docker compose down -v
```

---

> [!warning]
> `docker compose down -v` supprime tous les volumes déclarés dans Compose — données de DB incluses. Attention en prod.
