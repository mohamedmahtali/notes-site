---
title: compose.yml
tags:
  - beginner
---

# compose.yml

## Parent
- [[Docker compose]]

---

## Définition

`compose.yml` (ou `docker-compose.yml`) est le fichier de configuration central de Docker Compose. Il définit les services, réseaux, volumes, et variables d'environnement de la stack applicative.

---

## Structure complète

```yaml
# compose.yml
name: mon-projet   # optionnel, nom du projet

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        APP_VERSION: "1.0"
    image: mon-app:1.0
    container_name: mon-api
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DB_HOST=postgres
    env_file:
      - .env
    volumes:
      - ./logs:/app/logs
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: myapp
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  pgdata:

networks:
  backend:
    driver: bridge
```
