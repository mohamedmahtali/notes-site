---
title: Git hooks
tags:
  - intermediate
---
# Git hooks

---

## Définition

Les [[Git]] hooks sont des scripts exécutés automatiquement par Git lors d'événements spécifiques ([[Commit]], push, [[Merge]]). Ils permettent d'automatiser des vérifications de qualité **directement dans le workflow de développement**, avant que le code atteigne la CI.

---

## Pourquoi c'est important

> [!tip] Feedback local immédiat
> Un hook qui échoue en < 5 secondes vaut mieux qu'une CI qui échoue en 10 minutes. Les hooks détectent les problèmes au plus tôt, sans déclencher un [[Pipeline]] coûteux.

---

## Types de hooks

| Hook | Moment | Usage courant |
|---|---|---|
| [[pre-commit]] | Avant le commit | Lint, format, [[Secrets]] |
| [[commit-msg]] | Validation du message | Conventional commits |
| [[pre-push]] | Avant le push | Tests, protection de main |
| `post-merge` | Après un merge | `npm install`, migrations |
| `post-checkout` | Après un checkout | Nettoyage, setup |

---

## Emplacement

```bash
# Les hooks sont dans .git/hooks/ — non versionnés par défaut
ls .git/hooks/
# pre-commit.sample  commit-msg.sample  pre-push.sample ...

# Activer un hook : retirer le .sample et rendre exécutable
cp .git/hooks/pre-commit.sample .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---

## Partager les hooks avec l'équipe

```bash
# Option 1 : git config (depuis Git 2.9)
mkdir .githooks
git config core.hooksPath .githooks
# → les hooks dans .githooks/ sont versionnés

# Option 2 : framework pre-commit
pip install pre-commit
pre-commit install
```

> [!note]
> Les hooks dans `.git/hooks/` ne sont pas poussés sur le remote. Pour les partager, utilise `core.hooksPath` ou un framework comme [pre-commit](https://pre-commit.com/).
