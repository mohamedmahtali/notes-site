---
title: Profiles
tags:
  - intermediate
---

# Profiles

---

## Définition

Les profiles [[Docker compose]] permettent de regrouper des [[Services]] sous des étiquettes optionnelles. Un service sans profile est toujours démarré. Un service avec profile n'est démarré que si le profile est activé. Utile pour séparer les services de dev/debug des services de production.

---

## Configuration

```yaml
services:
  api:
    image: mon-app
    # pas de profile → toujours démarré

  postgres:
    image: postgres:16
    # pas de profile → toujours démarré

  pgadmin:
    image: dpage/pgadmin4
    profiles:
      - debug   # uniquement avec le profile "debug"

  mailhog:
    image: mailhog/mailhog
    profiles:
      - dev     # uniquement avec le profile "dev"
```

---

## Utilisation

```bash
# Démarrer uniquement les services sans profile
docker compose up -d

# Démarrer avec le profile "debug"
docker compose --profile debug up -d

# Démarrer avec plusieurs profiles
docker compose --profile debug --profile dev up -d

# Variable d'environnement
COMPOSE_PROFILES=debug,dev docker compose up -d
```

---

> [!tip]
> Les profiles évitent d'avoir plusieurs fichiers `docker-compose.yml` (compose.prod.yml, compose.dev.yml). Un seul fichier avec des services conditionnels.
