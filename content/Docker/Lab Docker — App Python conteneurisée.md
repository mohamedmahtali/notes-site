---
title: "Lab Docker — App Python conteneurisée"
tags:
  - docker
  - beginner
---

# Lab Docker — App Python conteneurisée

## Objectif

Containeriser une application Flask Python, l'optimiser avec un build multi-stage, et l'orchestrer avec Docker Compose (app + base de données Redis).

> [!note] Prérequis
> - Docker installé
> - Docker Compose v2
> - Connaissance de base Python

---

## Étape 1 — L'application Flask

```bash
mkdir flask-lab && cd flask-lab
```

```python
# app.py
from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379)

@app.route("/")
def index():
    count = r.incr("visits")
    return jsonify({"message": "Hello DevOps!", "visits": count})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

```text
# requirements.txt
flask==3.0.0
redis==5.0.1
gunicorn==21.2.0
```

---

## Étape 2 — Dockerfile optimisé

```dockerfile
# Dockerfile
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# --- Runtime stage ---
FROM python:3.11-slim

# Utilisateur non-root
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

WORKDIR /app
COPY --from=builder /root/.local /home/appuser/.local
COPY app.py .

USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
ENV FLASK_ENV=production

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
```

```bash
# Construire et tester
docker build -t flask-lab:1.0 .
docker run --rm -p 5000:5000 -e REDIS_HOST=localhost flask-lab:1.0
```

---

## Étape 3 — Docker Compose

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      REDIS_HOST: redis
    depends_on:
      redis:
        condition: service_healthy
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

```bash
docker compose up -d
docker compose ps
curl http://localhost:5000
curl http://localhost:5000     # Le compteur doit s'incrémenter
curl http://localhost:5000/health
```

---

## Étape 4 — Optimisation et bonnes pratiques

```bash
# Vérifier la taille de l'image
docker images flask-lab:1.0

# Scanner les vulnérabilités
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock   aquasec/trivy:latest image flask-lab:1.0

# Inspecter les layers
docker history flask-lab:1.0
```

---

## Étape 5 — Nettoyage

```bash
docker compose down -v          # Supprimer containers + volumes
docker rmi flask-lab:1.0        # Supprimer l'image
docker system prune             # Nettoyer le reste
```

---

## Vérification finale

- [ ] Image construite avec build multi-stage
- [ ] App accessible sur http://localhost:5000
- [ ] Compteur de visites s'incrémente (Redis fonctionne)
- [ ] Health check `/health` répond `{"status": "ok"}`
- [ ] Pas de processus root dans le conteneur : `docker exec <id> whoami` → `appuser`

## Liens

- [[Docker]]
- [[Dockerfile]]
- [[Multi stage builds]]
- [[Docker compose]]
- [[Container security]]
