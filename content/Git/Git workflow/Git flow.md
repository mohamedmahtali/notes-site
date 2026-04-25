---
title: Git flow
tags:
  - intermediate
---

# Git flow

---

## Définition

[[Git]] flow est un modèle de branching strict créé par Vincent Driessen en 2010. Il structure le développement autour de deux branches permanentes (`main` et `develop`) et trois [[Types]] de branches temporaires (`feature`, `release`, `hotfix`). Conçu pour les logiciels avec des cycles de release définis.

---

## Structure des branches

```
main          ──●────────────────●──────────── (tags: v1.0, v1.1)
                  \              /
release/1.1    ────●────●───────●
                          develop       ──●──●──●───●──●──●──●──
                    \       /    feature       ───────●──●──       ●──●──
```

| Branche | Rôle | Durée |
|---|---|---|
| `main` | Code en production, tagué | Permanente |
| `develop` | Intégration continue des features | Permanente |
| `feature/*` | Nouvelles fonctionnalités | Courte |
| `release/*` | Préparation d'une release | Moyenne |
| `hotfix/*` | Correction urgente sur main | Très courte |

---

## Workflow

```bash
# 1. Démarrer une feature
git checkout develop
git checkout -b feature/ajout-paiement

# 2. Finir la feature → merge dans develop
git checkout develop
git merge --no-ff feature/ajout-paiement
git branch -d feature/ajout-paiement

# 3. Préparer une release
git checkout -b release/1.2.0
# → tests finaux, corrections mineures, bump de version
git checkout main && git merge --no-ff release/1.2.0
git tag -a v1.2.0 -m "Release 1.2.0"
git checkout develop && git merge --no-ff release/1.2.0

# 4. Hotfix urgent
git checkout main
git checkout -b hotfix/1.2.1
# → corriger le bug
git checkout main && git merge --no-ff hotfix/1.2.1
git tag -a v1.2.1
git checkout develop && git merge --no-ff hotfix/1.2.1
```

---

## Git flow vs GitHub flow

| Critère | Git flow | [[GitHub flow]] |
|---|---|---|
| Branches permanentes | main + develop | main uniquement |
| Complexité | Élevée | Simple |
| Idéal pour | Logiciel versionné | Web/[[SaaS]] CI/CD |
| [[Releases]] | Planifiées | Continues |

> [!tip] Quand choisir Git flow ?
> Projets avec plusieurs versions maintenues en parallèle (v1.x et v2.x), applications mobile (app stores imposent des cycles), ou logiciels avec processus de QA formels.
