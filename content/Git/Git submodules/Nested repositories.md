---
title: Nested repositories
tags:
  - advanced
---

# Nested repositories

---

## Définition

Un dépôt imbriqué (nested [[Repository]]) est un dépôt [[Git]] situé à l'intérieur d'un autre dépôt Git. Git les gère via le mécanisme de **submodules**, qui maintient un pointeur vers un [[Commit]] précis du dépôt enfant.

---

## Structure

```
projet-principal/          ← dépôt Git A
├── .git/
├── .gitmodules
├── src/
└── libs/
    └── shared-utils/      ← dépôt Git B (sous-module)
        ├── .git/
        └── src/
```

---

## Bonnes pratiques

> [!tip] Quand utiliser les sous-[[Modules]]
> - Partager du code entre plusieurs projets (bibliothèque interne)
> - Fixer une dépendance à un commit précis pour garantir la reproductibilité
> - Intégrer un projet tiers sans le fork

> [!warning] Pièges courants
> - Oublier `git submodule update --init` après un clone → dossier vide
> - Modifier du code dans le sous-module sans committer dedans → perte de changements
> - Push du parent sans push du sous-module → CI cassée pour les autres

---

## Diagnostic rapide

```bash
# État de tous les sous-modules
git submodule status

# Voir si des sous-modules sont en retard
git submodule foreach 'git log --oneline -1'
```
