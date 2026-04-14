---
title: Best practices
tags:
  - intermediate
---

# Best practices

## Parent
- [[Dockerfile]]

---

## Définition

Les bonnes pratiques Dockerfile visent trois objectifs : images **légères** (moins de surface d'attaque, transferts rapides), builds **rapides** (cache optimisé), et images **sécurisées** (principe du moindre privilège).

---

## Checklist

```dockerfile
# ✅ 1. Image de base minimale et versionnée
FROM node:20.11-alpine3.19   # pin la version exacte, pas "latest"

# ✅ 2. Un seul processus par conteneur
CMD ["node", "server.js"]    # pas de supervisor ou d'init system

# ✅ 3. Layers optimisés pour le cache
COPY package.json ./
RUN npm ci                    # avant COPY . .

COPY . .                      # code source en dernier

# ✅ 4. Nettoyer dans le même RUN
RUN apt-get update && apt-get install -y curl &&     rm -rf /var/lib/apt/lists/*

# ✅ 5. Utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# ✅ 6. .dockerignore complet
# (node_modules/, .git/, .env, dist/)

# ✅ 7. Multi-stage pour séparer build/runtime
```

---

## Analyser une image

```bash
# Voir les layers et leur taille
docker image history mon-app:latest

# Scanner les vulnérabilités
docker scout cves mon-app:latest
# ou
trivy image mon-app:latest
```

---

## Tailles typiques

| Image | Taille recommandée |
|---|---|
| API Node.js | < 100MB |
| API Python | < 200MB |
| Binaire Go | < 20MB |
| App React buildée | < 30MB (nginx:alpine) |
