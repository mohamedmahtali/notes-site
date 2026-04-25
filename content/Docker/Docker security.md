---
title: Docker security
tags:
  - intermediate
---

# Docker security

---

## Définition

La sécurité [[Docker]] couvre l'ensemble des pratiques qui réduisent la surface d'attaque des conteneurs et de l'hôte Docker. Les conteneurs ne sont pas des VMs — une mauvaise configuration peut exposer l'hôte.

---

## Pourquoi c'est important

> [!warning] Un conteneur root ≠ sécurité
> Un processus root dans un conteneur peut potentiellement compromettre l'hôte si des [[Volumes]] ou le socket Docker sont montés. Le principe du moindre privilège s'applique.

---

## Checklist sécurité

```dockerfile
# 1. Utilisateur non-root
RUN addgroup -S app && adduser -S app -G app
USER app

# 2. Image minimale (moins de packages = moins de CVEs)
FROM python:3.12-slim
# ou distroless

# 3. Version exacte de l'image de base (pas latest)
FROM node:20.11.0-alpine3.19

# 4. Pas de secrets dans l'image
# ❌ ENV SECRET=mysecret
# ✅ Injecter au runtime via -e ou secrets manager

# 5. Filesystem en lecture seule
docker run --read-only mon-app
```

---

## Scanner les vulnérabilités

```bash
# Trivy (open source)
trivy image mon-app:latest

# Docker Scout
docker scout cves mon-app:latest

# Grype
grype mon-app:latest
```

---

> [!tip]
> Intégrer le scan d'image dans la CI pour bloquer les déploiements d'images avec des CVEs critiques.
