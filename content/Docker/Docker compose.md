---
title: Docker compose
tags:
  - beginner
---

# Docker compose

---

## Définition

[[Docker]] Compose est un outil pour définir et gérer des applications multi-conteneurs via un fichier YAML (`compose.yml` ou `docker-compose.yml`). Il orchestre le lancement, la mise en réseau, et le cycle de vie de plusieurs conteneurs en une seule commande.

---

## Pourquoi c'est important

> [!tip] Environnement local reproductible
> Un `docker compose up` lance une stack complète (API + DB + cache + proxy) identique pour tous les développeurs, sans installation manuelle.

---

## Commandes essentielles

```bash
# Démarrer tous les services (en arrière-plan)
docker compose up -d

# Voir les logs
docker compose logs -f

# Voir l'état des services
docker compose ps

# Stopper les services
docker compose down

# Stopper + supprimer les volumes
docker compose down -v

# Rebuilder les images
docker compose build
docker compose up -d --build

# Scaler un service
docker compose up -d --scale api=3

# Exécuter une commande dans un service
docker compose exec api bash
```

---

## Exemple minimal

```yaml
# compose.yml
services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://app:secret@db:5432/myapp
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      - POSTGRES_USER=app
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=myapp
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```
