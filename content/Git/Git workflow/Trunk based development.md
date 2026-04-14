---
title: Trunk based development
tags:
  - intermediate
---

# Trunk based development

## Parent
- [[Git workflow]]

## Concepts liés
- [[Git workflow]]
- [[GitHub flow]]
- [[Git flow]]
- [[CI-CD]]
- [[Feature branch]]

---

## Définition

Le Trunk Based Development (TBD) est un modèle où tous les développeurs intègrent leurs changements directement et fréquemment dans une seule branche principale (`main` / `trunk`). Les branches de feature, si elles existent, ne durent jamais plus de 1-2 jours.

---

## Pourquoi c'est important

> [!tip] Le modèle des grandes équipes tech
> Google, Facebook, et la plupart des équipes pratiquant le vrai CI/CD utilisent le TBD. Il élimine l'enfer des merges de longues branches et force une intégration continue réelle.

---

## Les deux variantes

### 1. Direct commit sur trunk (petites équipes)
```bash
git checkout main
git pull origin main
# → modifier, tester localement
git add . && git commit -m "feat: add retry logic"
git push origin main
```

### 2. Short-lived feature branches (grandes équipes)
```bash
# Branches de max 1-2 jours
git checkout -b feature/add-retry
# → 1 ou 2 commits
git push origin feature/add-retry
# → PR → review → merge dans les 24h
git branch -d feature/add-retry
```

---

## Feature flags – clé du TBD

```python
# Déployer du code incomplet sans l'activer
if feature_flags.is_enabled("new_checkout_flow", user):
    return new_checkout(cart)
else:
    return legacy_checkout(cart)
```

Les feature flags permettent de merger du code non terminé dans `main` sans l'exposer aux utilisateurs.

---

## Comparaison

| Critère | TBD | GitHub flow | Git flow |
|---|---|---|---|
| Durée des branches | < 2 jours | Quelques jours | Semaines |
| Intégration | Continue | PR-based | Par release |
| Conflits | Rares | Occasionnels | Fréquents |
| Requiert | Feature flags, CI solide | CI de base | Processus strict |

> [!note]
> Le TBD n'est pas "committer sur main sans review". Il nécessite une CI robuste, des tests automatisés, et souvent des feature flags.
