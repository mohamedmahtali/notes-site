---
title: Dockerfile
tags:
  - beginner
---

# Dockerfile

---

## Définition

Un Dockerfile est un fichier texte contenant une série d'[[Instructions]] qui définissent comment construire une image [[Docker]]. Chaque instruction crée une nouvelle couche dans l'image finale. C'est la "recette" de ton environnement applicatif.

---

## Structure de base

```dockerfile
# Image de base
FROM node:20-alpine

# Répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances en premier (cache layer)
COPY package*.json ./

# Installer les dépendances
RUN npm ci --only=production

# Copier le reste du code
COPY . .

# Variable d'environnement
ENV NODE_ENV=production

# Port exposé (documentation)
EXPOSE 3000

# Commande de démarrage
CMD ["node", "server.js"]
```

---

## Ordre des instructions = ordre des layers

> [!tip] Les [[Layers]] stables en premier
> Docker met en cache chaque layer. Si une instruction change, toutes les instructions suivantes sont recalculées. Mettre les choses qui changent rarement en haut (`FROM`, `RUN apt-get`), les choses qui changent souvent en bas (`COPY . .`).

---

## Exemple Python

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
