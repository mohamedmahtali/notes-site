---
title: Global ignore
tags:
  - beginner
---

# Global ignore

## Parent
- [[Git ignore]]

## Concepts liés
- [[Git ignore]]
- [[Project ignore]]

---

## Définition

Le fichier d'ignore global (`~/.gitignore_global`) définit les patterns à ignorer sur **tous les dépôts Git** de ta machine, sans les committer. Idéal pour les fichiers liés à ton environnement (IDE, OS) que tu ne veux pas imposer aux autres contributeurs.

---

## Configuration

```bash
# Créer le fichier global
touch ~/.gitignore_global

# Configurer Git pour l'utiliser
git config --global core.excludesfile ~/.gitignore_global
```

---

## Contenu typique

```gitignore
# macOS
.DS_Store
.AppleDouble
.LSOverride

# Windows
Thumbs.db
Desktop.ini

# Linux
*~
.nfs*

# Éditeurs
.vscode/
.idea/
*.swp
*.swo
.sublime-workspace

# Outils
.direnv/
.envrc
```

---

## Global vs Project .gitignore

| Aspect | Global (`~/.gitignore_global`) | Project (`.gitignore`) |
|---|---|---|
| Scope | Toute la machine | Projet uniquement |
| Versionné | ❌ Non | ✅ Oui |
| Partagé avec l'équipe | ❌ Non | ✅ Oui |
| Idéal pour | IDE, OS, outils perso | Dépendances, build, secrets |

> [!tip]
> Règle simple : tout ce qui est lié à **ton environnement de travail** va dans le global. Tout ce qui est lié au **projet** va dans le `.gitignore` du projet.
