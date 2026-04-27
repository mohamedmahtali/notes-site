---
title: Image scanning
tags:
  - security
  - intermediate
---

# Image scanning

## Définition

L'image scanning analyse les images de conteneurs pour détecter les vulnérabilités CVE dans les paquets OS et les dépendances applicatives avant le déploiement.

> [!tip] Pourquoi c'est important
> Une image [[Docker]] peut embarquer des centaines de paquets avec des vulnérabilités connues. Scanner en CI/CD permet de bloquer les images dangereuses avant qu'elles n'atteignent la production.

## Quoi est scanné

```
Image Docker
├── OS packages     — CVEs dans Ubuntu/Alpine/Debian (apt, apk)
├── Langages        — npm, pip, gem, maven, go.sum
├── Configs         — fichiers sensibles exposés par erreur
└── Secrets         — clés API, tokens hardcodés dans les layers
```

## Trivy — outil recommandé

```bash
# Scanner une image depuis Docker Hub
trivy image nginx:latest

# Seulement les vulnérabilités avec fix disponible
trivy image --ignore-unfixed nginx:latest

# Filtrer par sévérité
trivy image --severity HIGH,CRITICAL nginx:latest

# Format JSON pour intégration CI
trivy image --format json --output results.json nginx:latest

# Scanner le filesystem local (dépendances du code)
trivy fs .

# Scanner un repo git distant
trivy repo https://github.com/myorg/myapp

# Générer un SBOM (Software Bill of Materials)
trivy image --format cyclonedx --output sbom.json nginx:latest
```

## Intégration CI/CD

### GitHub Actions

```yaml
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Scan image with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: sarif
          output: trivy-results.sarif
          severity: HIGH,CRITICAL
          exit-code: 1          # fail le pipeline si vulnérabilités trouvées

      - name: Upload results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: trivy-results.sarif
```

### GitLab CI

```yaml
container_scan:
  image: aquasec/trivy:latest
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  allow_failure: false
```

## Réduire les vulnérabilités à la source

```dockerfile
# ✅ Préférer des images minimales
FROM gcr.io/distroless/java17-debian11   # pas de shell, pas d'apt
# ou
FROM alpine:3.19                          # surface réduite vs ubuntu

# ✅ Build multi-stage : ne copier que le binaire final
FROM golang:1.22 AS builder
WORKDIR /app
COPY . .
RUN go build -o server .

FROM gcr.io/distroless/static
COPY --from=builder /app/server /server
CMD ["/server"]

# ❌ Éviter
FROM ubuntu:latest      # trop de paquets
RUN apt install -y curl wget git   # outils inutiles en prod
```

## Politique de blocage

| Sévérité CVSS | Action recommandée |
|---------------|-------------------|
| CRITICAL (9-10) | Bloquer immédiatement, correctif obligatoire |
| HIGH (7-8.9) | Bloquer en CI, délai de remédiation court |
| MEDIUM (4-6.9) | Alerte, tracked dans le backlog |
| LOW (0-3.9) | Informatif, pas de blocage |

## Explorer

- **[[CVE detection]]** — base de données CVE, scores CVSS
- **[[Container security]]** — sécurité runtime des conteneurs
- **[[DevSecOps]]** — intégration sécurité dans le pipeline CI/CD
- **[[Vulnerability scanning]]** — scanning au-delà des images (code, IaC)
