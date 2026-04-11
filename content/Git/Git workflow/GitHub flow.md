---
title: GitHub flow
tags:
  - beginner
---

# GitHub flow

## Parent
- [[Git workflow]]

## Concepts liés
- [[Git flow]]
- [[Trunk based development]]
- [[Pull request]]
- [[Branch]]
- [[CI-CD]]

---

## Définition

GitHub flow est un workflow Git **simple et léger**, conçu pour des équipes qui déploient régulièrement (plusieurs fois par jour). Il repose sur une seule branche principale (`main`) toujours déployable, et des branches de feature courtes.

C'est le workflow le plus répandu dans les projets modernes avec CI/CD.

---

## Pourquoi c'est important

> [!tip] Idéal pour le CI/CD
> GitHub flow est pensé pour s'intégrer naturellement avec les pipelines d'intégration continue. Chaque Pull Request déclenche des tests automatiques avant le merge.

- **Simple** : une seule règle — `main` est toujours déployable
- **Rapide** : cycles courts, feedback rapide
- **Compatible CI/CD** : chaque PR = pipeline de validation automatique

---

## Les 6 étapes

```mermaid
flowchart LR
    A[1. main à jour] --> B[2. Créer une branche]
    B --> C[3. Committer]
    C --> D[4. Ouvrir une PR]
    D --> E[5. Review & CI]
    E --> F[6. Merge dans main]
    F --> G[Deploy 🚀]

    style A fill:#1e2330,color:#c9d1e0,stroke:#60a5fa
    style G fill:#10b981,color:#fff,stroke:none
```

### 1. Partir de `main` à jour

```bash
git checkout main
git pull origin main
```

### 2. Créer une branche descriptive

```bash
git checkout -b feature/ajout-authentification
# ou
git checkout -b fix/correction-timeout-api
```

### 3. Committer régulièrement

```bash
git add .
git commit -m "feat(auth): add JWT validation middleware"
git push origin feature/ajout-authentification
```

### 4. Ouvrir une Pull Request

Sur GitHub : comparer ta branche avec `main` et ouvrir une PR avec une description claire du changement.

### 5. Code review + CI

- Les pipelines CI s'exécutent automatiquement (tests, lint, build)
- Les reviewers commentent et approuvent
- Les corrections sont poussées sur la même branche

### 6. Merger dans `main` et déployer

```bash
# Sur GitHub : bouton "Merge pull request"
# En local après merge :
git checkout main
git pull origin main
git branch -d feature/ajout-authentification
```

---

## Comparaison avec Git flow

| Critère | GitHub flow | Git flow |
|---|---|---|
| Complexité | Simple | Complexe |
| Branches | 1 principale + features | main, develop, release, hotfix |
| Déploiement | Continu | Par release |
| Idéal pour | Web, SaaS, CI/CD | Logiciel versionné |

> [!note] Quelle règle retenir ?
> **`main` doit toujours être dans un état déployable.** Si ce n'est pas le cas, le workflow est cassé.

---

## Exemple complet

```bash
# Démarrer
git checkout main && git pull origin main
git checkout -b feature/page-contact

# Développer
git add .
git commit -m "feat: add contact page"
git push origin feature/page-contact

# → Ouvrir PR sur GitHub
# → CI passe ✅, review approuvée ✅
# → Merge dans main → deploy automatique 🚀

# Nettoyage local
git checkout main
git pull origin main
git branch -d feature/page-contact
```
