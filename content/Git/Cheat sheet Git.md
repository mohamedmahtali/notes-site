---
title: Cheat sheet Git
tags:
  - git
  - beginner
---

# Cheat sheet Git

## Setup

```bash
git config --global user.name "Mohamed"
git config --global user.email "m@example.com"
git config --global core.editor "vim"
git config --list                        # Voir la config
```

## Initialisation

```bash
git init                                 # Nouveau repo local
git clone https://github.com/org/repo   # Cloner un repo
git clone --depth 1 https://...          # Clone superficiel (dernier commit)
```

## Status & diff

```bash
git status                               # Fichiers modifiés/staged
git diff                                 # Modifications non staged
git diff --staged                        # Modifications staged
git diff main..feature                   # Entre deux branches
git log --oneline -10                    # 10 derniers commits
git log --oneline --graph --all          # Arbre des branches
git show abc1234                         # Détails d'un commit
```

## Stage & commit

```bash
git add file.txt                         # Stager un fichier
git add .                                # Stager tout
git add -p                               # Stager par chunks (interactif)
git commit -m "feat: add login"          # Committer
git commit --amend                       # Modifier le dernier commit
git commit --amend --no-edit             # Amend sans changer le message
```

## Branches

```bash
git branch                               # Branches locales
git branch -a                            # Toutes (+ remote)
git checkout -b feature/login            # Créer et basculer
git switch -c feature/login              # Idem (syntaxe moderne)
git switch main                          # Basculer sur main
git branch -d feature/login              # Supprimer branche
git branch -D feature/login              # Forcer la suppression
```

## Remote

```bash
git remote -v                            # Remotes configurés
git fetch origin                         # Récupérer sans merger
git pull                                 # Fetch + merge
git pull --rebase                        # Fetch + rebase
git push origin feature/login            # Pousser une branche
git push -u origin feature/login         # + set upstream
git push --force-with-lease              # Force push sécurisé
```

## Merge & rebase

```bash
git merge feature/login                  # Merger dans la branche courante
git merge --no-ff feature/login          # Forcer un merge commit
git rebase main                          # Rebaser sur main
git rebase -i HEAD~3                     # Rebase interactif (3 commits)
git cherry-pick abc1234                  # Appliquer un commit spécifique
```

## Undo

```bash
git restore file.txt                     # Annuler modifs non staged
git restore --staged file.txt            # Désindexer
git revert abc1234                       # Annuler un commit (nouveau commit)
git reset --soft HEAD~1                  # Annuler commit (garde les modifs staged)
git reset --mixed HEAD~1                 # Annuler commit (modifs non staged)
git reset --hard HEAD~1                  # Annuler commit + modifs (destructif)
git stash                                # Mettre de côté
git stash pop                            # Restaurer
git stash list                           # Lister les stashs
```

## Tags

```bash
git tag v1.0.0                           # Tag léger
git tag -a v1.0.0 -m "Release 1.0"      # Tag annoté
git push origin v1.0.0                   # Pousser un tag
git push origin --tags                   # Pousser tous les tags
```

## Liens

- [[Git]]
- [[Branch]]
- [[Commit]]
- [[Rebase]]
- [[Git workflow]]
