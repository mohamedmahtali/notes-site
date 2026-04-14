---
title: Rewrite history
tags:
  - advanced
---

# Rewrite history

## Parent
- [[Rebase]]

## Concepts liés
- [[Rebase]]
- [[Interactive rebase]]
- [[Squash]]
- [[Amend]]

---

## Définition

Réécrire l'historique Git signifie modifier des commits existants — leur message, leur contenu, leur ordre, ou leur existence. Les outils principaux sont `git commit --amend`, `git rebase -i`, et `git filter-branch` / `git filter-repo`.

---

## Pourquoi c'est important

> [!danger] Règle absolue
> Ne jamais réécrire l'historique de commits déjà poussés sur une branche partagée (main, develop). Cela force tous les collaborateurs à resynchroniser et peut causer des pertes de données.

---

## Outils par cas d'usage

| Cas | Outil |
|---|---|
| Corriger le dernier commit | `git commit --amend` |
| Nettoyer les N derniers commits | `git rebase -i HEAD~N` |
| Supprimer un fichier de tout l'historique | `git filter-repo --path fichier.txt --invert-paths` |
| Changer l'email de tous les commits | `git filter-repo --email-callback` |

---

## Supprimer un secret commis par erreur

```bash
# Installer git-filter-repo (recommandé vs filter-branch)
pip install git-filter-repo

# Supprimer le fichier de tout l'historique
git filter-repo --path .env --invert-paths

# Force push (après avoir invalidé le secret côté service !)
git push origin --force --all
```

> [!warning] Invalider le secret en priorité
> Réécrire l'historique n'efface pas le secret des forks, clones, ou caches GitHub. La première action doit toujours être d'invalider/révoquer le secret exposé.

---

## Rebase interactif – réécriture courante

```bash
# Modifier un commit plus ancien (pas le dernier)
git rebase -i HEAD~5

# Changer "pick" en "edit" pour le commit à modifier
# Git s'arrête sur ce commit
git commit --amend -m "feat: nouveau message corrigé"
git rebase --continue
```
