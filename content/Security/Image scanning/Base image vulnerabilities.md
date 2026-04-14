---
title: Base image vulnerabilities
tags: [security, intermediate]
---

# Base image vulnerabilities

## Définition

Les vulnérabilités d'image de base sont les CVEs présents dans l'OS et les paquets système de l'image Docker parent (FROM). Elles représentent souvent la majorité des vulnérabilités détectées.

> [!tip] Stratégie minimale
> Utiliser des images distroless ou Alpine minimise drastiquement la surface d'attaque. `FROM scratch` donne zéro paquet OS (pour les binaires statiques).

## Comparer les images de base

```bash
# ubuntu:22.04 - nombreuses vulnérabilités
trivy image ubuntu:22.04 | tail -5

# alpine:3.18 - très peu de vulnérabilités
trivy image alpine:3.18 | tail -5

# distroless - quasi aucune
trivy image gcr.io/distroless/base-debian12 | tail -5
```

## Bonnes pratiques

```dockerfile
# ❌ Mauvais : image lourde avec beaucoup de paquets
FROM ubuntu:22.04

# ✓ Mieux : Alpine minimal
FROM alpine:3.18

# ✓ Mieux encore : distroless (pas de shell, pas de gestionnaire de paquets)
FROM gcr.io/distroless/python3

# ✓ Build multi-stage : builder lourd, runtime minimal
FROM python:3.11 AS builder
RUN pip install --user -r requirements.txt

FROM gcr.io/distroless/python3
COPY --from=builder /root/.local /root/.local
COPY app.py .
CMD ["app.py"]
```

## Liens

- [[Image scanning]]
- [[CVE detection]]
- [[Container security]]
