---
title: Project ignore
tags:
  - beginner
---

# Project ignore

---

## Définition

Le fichier `.gitignore` à la racine d'un projet définit les fichiers et dossiers que [[Git]] doit ignorer pour ce projet spécifique. Il est versionné avec le projet et partagé entre tous les contributeurs.

---

## Syntaxe

```gitignore
# Commentaire
node_modules/       ← dossier entier
*.log               ← tous les fichiers .log
.env                ← fichier spécifique
dist/               ← dossier build
!dist/.gitkeep      ← exception : garder ce fichier

# Patterns avancés
**/*.tmp            ← .tmp dans tous les sous-dossiers
src/**/*.test.js    ← tous les fichiers de test dans src/
/config.local.json  ← uniquement à la racine (slash initial)
```

---

## Templates courants

```gitignore
# Node.js
node_modules/
npm-debug.log*
.env
.env.local
dist/
build/

# Python
__pycache__/
*.pyc
.venv/
*.egg-info/
.pytest_cache/

# Docker
.docker/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

## Vérifier ce qu'un fichier est ignoré ou non

```bash
git check-ignore -v node_modules/
# .gitignore:1:node_modules/    node_modules/

git status --ignored
```

---

## Arrêter de tracker un fichier déjà commité

```bash
# Retirer le fichier du tracking sans le supprimer
echo ".env" >> .gitignore
git rm --cached .env
git commit -m "chore: stop tracking .env"
```

> [!warning]
> `.gitignore` ne protège pas les [[Secrets]] déjà committés. Utilise `git filter-repo` pour les retirer de l'historique et invalide les secrets exposés immédiatement.
