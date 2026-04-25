---
title: Bind mounts
tags:
  - beginner
---

# Bind mounts

---

## Définition

Un bind mount monte un **répertoire ou fichier de l'hôte** directement dans le conteneur. Tout changement dans l'hôte est immédiatement visible dans le conteneur et vice-versa. C'est le mécanisme de développement local par excellence.

---

## Commandes

```bash
# Monter le répertoire courant
docker run -v $(pwd):/app mon-app
# ou syntaxe --mount
docker run --mount type=bind,source=$(pwd),target=/app mon-app

# Monter un fichier unique
docker run -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro nginx

# Mode read-only (:ro)
docker run -v $(pwd)/config:/app/config:ro mon-app
```

---

## Cas d'usage

```yaml
# docker-compose.yml – développement local
services:
  api:
    image: mon-app:dev
    volumes:
      - .:/app              # code source → hot reload
      - /app/node_modules   # exception : garder node_modules du conteneur
```

---

## Bind mount vs Named volume

| Critère | Bind mount | Named volume |
|---|---|---|
| Performance [[Linux]] | ✅ Native | ✅ Native |
| Performance macOS | ⚠️ Lent | ✅ Rapide |
| Cas d'usage | Dev local | Données persistantes |
| Portabilité | ❌ Chemin absolu | ✅ Nommé |

> [!warning] Macros
> Sur macOS/Windows, les bind mounts sont plus lents à cause de la VM. Utiliser des [[Named [[Volumes]]]] pour les données de base de données sur ces OS.
