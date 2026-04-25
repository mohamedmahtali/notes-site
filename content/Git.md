---
title: Git
tags:
  - beginner
---

# Git

---

## Définition

Git est un système de **contrôle de version distribué** créé par Linus Torvalds en 2005. Il permet de suivre les modifications d'un ensemble de fichiers au fil du temps, de collaborer à plusieurs sur un même projet, et de revenir à n'importe quel état antérieur du code.

Contrairement aux systèmes centralisés (SVN, CVS), chaque développeur possède une **copie complète** de l'historique du dépôt en local.

---

## Pourquoi c'est important

> [!tip] Indispensable en [[DevOps]]
> Git est la fondation de tout [[Pipeline]] CI/CD. Sans maîtrise de Git, impossible de comprendre comment le code passe du développeur à la production.

- **Traçabilité** : chaque modification est enregistrée avec son auteur, sa date et son message
- **Collaboration** : plusieurs personnes travaillent en parallèle sans écraser le travail des autres
- **Réversibilité** : revenir à un état antérieur en cas de bug ou de régression
- **Déclencheur CI/CD** : un `git push` déclenche automatiquement les pipelines de build et de déploiement

---

## Commandes essentielles

```bash
# Initialiser un dépôt
git init

# Cloner un dépôt existant
git clone https://github.com/user/repo.git

# Voir l'état du dépôt
git status

# Ajouter des fichiers à l'index
git add fichier.txt
git add .              # tous les fichiers modifiés

# Créer un commit
git commit -m "feat: add login feature"

# Pousser vers le dépôt distant
git push origin main

# Récupérer les modifications distantes
git pull origin main

# Voir l'historique
git log --oneline --graph
```

---

## Les 3 zones de Git

```
Working Directory  →  Staging Area (Index)  →  Repository
   (fichiers)           git add                  git commit
```

| Zone | Description |
|---|---|
| **Working Directory** | Tes fichiers locaux — modifiés mais pas encore suivis |
| **[[Staging]] Area** | Fichiers prêts à être committés (`git add`) |
| **[[Repository]]** | Historique des commits sauvegardé localement |

---

## Exemple

```bash
# Workflow basique
git clone https://github.com/user/projet.git
cd projet
git checkout -b feature/nouvelle-fonctionnalite

# ... on modifie des fichiers ...

git add .
git commit -m "feat: ajouter la page de connexion"
git push origin feature/nouvelle-fonctionnalite

# Ensuite : ouvrir une Pull Request sur GitHub
```

> [!note] Par où commencer ?
> Commence par maîtriser [[Commit]], [[Branch]] et [[Merge]] — ces trois concepts couvrent 90% des besoins quotidiens.
