---
title: Non root user
tags:
  - intermediate
---

# Non root user

## Parent
- [[Docker security]]

---

## Définition

Par défaut, le processus dans un conteneur Docker s'exécute en tant que `root` (UID 0). Cela représente un risque de sécurité : en cas d'évasion du conteneur, l'attaquant a les droits root sur l'hôte. Exécuter en utilisateur non-root est une pratique de sécurité fondamentale.

---

## Créer un utilisateur dans le Dockerfile

```dockerfile
# Alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Debian/Ubuntu
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
USER appuser

# Avec UID/GID spécifiques (pour les volumes)
RUN groupadd -r -g 1001 appgroup && useradd -r -u 1001 -g appgroup appuser
USER 1001
```

---

## Au lancement

```bash
# Spécifier l'utilisateur au run
docker run -u 1001:1001 mon-app
docker run --user appuser mon-app
```

---

## Permissions de fichiers

```dockerfile
# Créer les dossiers avec les bonnes permissions avant de switcher d'user
RUN mkdir -p /app/logs && chown -R appuser:appgroup /app
USER appuser
```

---

> [!tip]
> Les images officielles récentes (node, python, nginx) fournissent souvent un utilisateur dédié (`node`, `www-data`). Utilise-le plutôt que de créer le tien :
> ```dockerfile
> USER node   # dans l'image node:20
> ```
