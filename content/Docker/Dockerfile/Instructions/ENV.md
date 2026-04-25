---
title: ENV
tags:
  - beginner
---

# ENV

---

## Définition

`ENV` définit des [[Variables]] d'environnement persistantes dans l'image. Elles sont disponibles pendant le build (pour les [[Instructions]] suivantes) ET dans les conteneurs lancés depuis l'image.

---

## Syntaxe

```dockerfile
# Syntaxe moderne (recommandée)
ENV NODE_ENV=production
ENV APP_PORT=3000

# Plusieurs variables en une ligne
ENV NODE_ENV=production     APP_PORT=3000     LOG_LEVEL=info
```

---

## ENV vs ARG

| Instruction | Disponible au build | Disponible au runtime | Visible dans l'image |
|---|---|---|---|
| `ENV` | ✅ | ✅ | ✅ Oui |
| `ARG` | ✅ | ❌ | ❌ Non |

```dockerfile
ARG APP_VERSION=1.0       # valeur de build seulement
ENV APP_VERSION=$APP_VERSION   # transférer en env si besoin au runtime
```

---

## Override au runtime

```bash
# Surcharger une ENV au lancement
docker run -e NODE_ENV=development mon-app
docker run --env-file .env mon-app
```

---

> [!warning] Ne jamais mettre des [[Secrets]] dans ENV
> Les variables ENV sont visibles dans l'image via `docker inspect`. Utilise les secrets [[Docker]] ou des variables injectées au runtime pour les données sensibles.
