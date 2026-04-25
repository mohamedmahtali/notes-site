---
title: "Lab CI/CD — Pipeline GitHub Actions complet"
tags:
  - ci-cd
  - intermediate
---

# Lab CI/CD — Pipeline GitHub Actions complet

## Objectif

Créer un pipeline GitHub Actions complet : lint → test → build image Docker → push vers GHCR → déploiement conditionnel sur la branche main.

> [!note] Prérequis
> - Repo GitHub (public ou privé)
> - Docker installé localement
> - Compte GHCR (GitHub Container Registry) — inclus avec GitHub

---

## Étape 1 — Structure du projet

```bash
mkdir cicd-lab && cd cicd-lab
git init
git remote add origin https://github.com/TON_USERNAME/cicd-lab.git
```

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello CI/CD!"

@app.route("/health")
def health():
    return {"status": "ok"}, 200
```

```python
# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_hello(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Hello" in r.data

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "ok"
```

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
```

---

## Étape 2 — Pipeline CI/CD

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: ["*"]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ─── Lint & Test ────────────────────────────────────
  test:
    name: Lint & Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: pip install -r requirements.txt pytest flake8

      - name: Lint (flake8)
        run: flake8 app.py --max-line-length=100

      - name: Run tests
        run: pytest test_app.py -v

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: "*.xml"

  # ─── Build & Push ────────────────────────────────────
  build:
    name: Build & Push Image
    runs-on: ubuntu-latest
    needs: test
    permissions:
      contents: read
      packages: write

    outputs:
      image-digest: ${{ steps.push.outputs.digest }}
      image-tag: ${{ steps.meta.outputs.version }}

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to GHCR
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=
            type=ref,event=branch
            type=semver,pattern={{version}}

      - name: Build and push
        id: push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # ─── Deploy ──────────────────────────────────────────
  deploy:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment: production

    steps:
      - name: Deploy
        run: |
          echo "Deploying image: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ needs.build.outputs.image-tag }}"
          # Ici : ssh deploy, kubectl set image, helm upgrade, etc.
          echo "✅ Deployment successful"
```

---

## Étape 3 — Configurer les secrets GitHub

```
Settings → Secrets and variables → Actions → New repository secret

DEPLOY_KEY = (clé SSH de déploiement si nécessaire)
```

> [!note] `GITHUB_TOKEN` est automatique
> Le token `secrets.GITHUB_TOKEN` est fourni automatiquement par GitHub Actions pour pousser vers GHCR — pas besoin de le configurer.

---

## Étape 4 — Tester le pipeline

```bash
# Push pour déclencher le pipeline
git add .
git commit -m "feat: add CI/CD pipeline"
git push origin main

# Ouvrir GitHub → Actions pour voir le pipeline en cours
```

---

## Vérification finale

- [ ] Job `test` passe (lint + pytest)
- [ ] Job `build` construit et push l'image sur GHCR
- [ ] Image visible dans : GitHub → [[Package]]
- [ ] Job `deploy` s'exécute seulement sur `main`
- [ ] Cache Docker actif (2e run plus rapide)

## Liens

- [[CI-CD]]
- [[GitHub actions]]
- [[Pipeline]]
- [[Docker]]
- [[Artifacts]]
