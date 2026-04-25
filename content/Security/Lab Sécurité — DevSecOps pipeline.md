---
title: "Lab Sécurité — DevSecOps pipeline"
tags:
  - security
  - intermediate
---

# Lab Sécurité — DevSecOps pipeline

## Objectif

Intégrer la sécurité dans un [[Pipeline]] CI/CD : SAST avec Semgrep, scan de dépendances, build d'image avec Trivy, et détection de [[Secrets]] avec Gitleaks.

> [!note] Prérequis
> - [[Docker]] installé
> - Python 3.11+
> - Un repo GitHub pour le pipeline CI

---

## Étape 1 — Préparer un projet avec des vulnérabilités intentionnelles

```python
# app_insecure.py — EXEMPLES À NE JAMAIS UTILISER EN PROD
import sqlite3
import subprocess
import hashlib

def get_user(username):
    # ❌ Injection SQL
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return conn.execute(query).fetchall()

def run_command(cmd):
    # ❌ Injection de commande
    return subprocess.run(cmd, shell=True, capture_output=True)

def hash_password(password):
    # ❌ MD5 est obsolète pour les mots de passe
    return hashlib.md5(password.encode()).hexdigest()

# ❌ Secret codé en dur (ne jamais faire)
API_KEY = "sk-abc123secretkey"
DB_PASSWORD = "admin1234"
```

```text
# requirements.txt (avec dépendances volontairement vulnérables)
flask==2.1.0
requests==2.25.0
```

---

## Étape 2 — SAST avec Semgrep

```bash
# Installer Semgrep
pip install semgrep

# Scanner avec les règles OWASP
semgrep --config=p/owasp-top-ten app_insecure.py

# Scanner avec règles Python sécurité
semgrep --config=p/python-security app_insecure.py

# Format JSON (pour CI)
semgrep --config=p/owasp-top-ten --json app_insecure.py |   jq '.results[] | {rule: .check_id, message: .extra.message, line: .start.line}'
```

**Résultat attendu :** Semgrep doit détecter l'injection SQL, l'injection de commande et le hash MD5.

---

## Étape 3 — Détection de secrets avec Gitleaks

```bash
# Via Docker
docker run --rm -v $(pwd):/repo   zricethezav/gitleaks:latest detect   --source /repo   --verbose

# Résultat : doit détecter API_KEY et DB_PASSWORD
```

---

## Étape 4 — Scan de dépendances

```bash
# Trivy filesystem
docker run --rm -v $(pwd):/app   aquasec/trivy:latest fs   --security-checks vuln   /app

# Safety (Python)
pip install safety
safety check -r requirements.txt
```

---

## Étape 5 — Build et scan d'image

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app_insecure.py .
CMD ["python", "app_insecure.py"]
```

```bash
docker build -t seclab:1.0 .

# Scan Trivy
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock   aquasec/trivy:latest image   --severity HIGH,CRITICAL   seclab:1.0
```

---

## Étape 6 — Pipeline GitHub Actions DevSecOps

```yaml
# .github/workflows/devsecops.yml
name: DevSecOps Pipeline

on: [push, pull_request]

jobs:
  sast:
    name: SAST (Semgrep)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
        with:
          config: p/owasp-top-ten

  secrets-scan:
    name: Secrets Detection
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  dependency-scan:
    name: Dependency Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Trivy filesystem scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: fs
          security-checks: vuln
          severity: HIGH,CRITICAL
          exit-code: 1

  image-scan:
    name: Image Scan
    runs-on: ubuntu-latest
    needs: [sast, secrets-scan, dependency-scan]
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t seclab:${{ github.sha }} .
      - name: Trivy image scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: seclab:${{ github.sha }}
          severity: CRITICAL
          exit-code: 1
          ignore-unfixed: true
```

---

## Vérification finale

- [ ] Semgrep détecte l'injection SQL et MD5
- [ ] Gitleaks détecte `API_KEY` et `DB_PASSWORD`
- [ ] Trivy trouve des CVEs dans les dépendances
- [ ] Le pipeline CI échoue sur les vulnérabilités CRITICAL
- [ ] Corriger `app_insecure.py` et vérifier que le pipeline passe

## Liens

- [[Security]]
- [[DevSecOps]]
- [[SAST]]
- [[Image scanning]]
- [[Vulnerability scanning]]
- [[Shift left security]]
