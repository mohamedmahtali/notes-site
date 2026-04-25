---
title: Instructions
tags:
  - beginner
---

# Instructions

---

## Définition

Les instructions [[Dockerfile]] sont les commandes qui composent la recette de construction d'une image. Chaque instruction crée un layer dans l'image finale.

---

## Référence rapide

| Instruction | Rôle |
|---|---|
| `FROM` | Image de base |
| `WORKDIR` | Répertoire de travail courant |
| `COPY` | Copier des fichiers depuis le [[Host]] |
| `ADD` | Copier + extraire archives + URL |
| `RUN` | Exécuter une commande lors du build |
| `ENV` | Définir une variable d'environnement |
| `EXPOSE` | Documenter le port utilisé |
| `CMD` | Commande par défaut au démarrage |
| `ENTRYPOINT` | Point d'entrée non overridable |
| `ARG` | Variable de build (non persistée) |
| `LABEL` | Métadonnées de l'image |
| `USER` | Utilisateur pour les instructions suivantes |
| `HEALTHCHECK` | Vérification de santé du conteneur |
| `VOLUME` | Déclarer un point de montage |

---

## Exemple complet

```dockerfile
FROM python:3.12-slim
LABEL maintainer="Mohamed Mahtali"
ARG APP_VERSION=1.0
ENV APP_VERSION=$APP_VERSION NODE_ENV=production
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache
COPY --chown=appuser:appuser . .
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/health || exit 1
CMD ["python", "app.py"]
```
