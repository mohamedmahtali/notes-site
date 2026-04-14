---
title: Build context
tags:
  - intermediate
---

# Build context

## Parent
- [[Docker build]]

---

## Définition

Le contexte de build est l'ensemble des fichiers envoyés au daemon Docker lors d'un `docker build`. Par défaut, c'est le répertoire passé en argument (`.`). Tout fichier dans ce répertoire est potentiellement accessible dans le Dockerfile via `COPY` ou `ADD`.

---

## Optimiser le contexte

```bash
# Voir la taille du contexte envoyé
docker build . 2>&1 | head
# Sending build context to Docker daemon  142MB  ← trop gros !
```

```gitignore
# .dockerignore – exclure les fichiers inutiles
node_modules/
.git/
*.log
dist/
.env
tests/
docs/
```

---

## .dockerignore

Fonctionne comme `.gitignore` mais pour le contexte de build Docker.

```dockerignore
# Ne pas envoyer au daemon
node_modules/
.git/
.github/
*.md
*.test.js
coverage/
.DS_Store
```

---

## Contextes alternatifs

```bash
# Depuis une URL Git
docker build https://github.com/org/repo.git#main

# Depuis un tar
docker build - < archive.tar

# Spécifier un sous-répertoire comme contexte
docker build -f services/api/Dockerfile services/api/
```

> [!tip]
> Un `.dockerignore` efficace peut réduire le contexte de 500MB à quelques MB, accélérant considérablement le build.
