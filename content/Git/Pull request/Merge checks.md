---
title: Merge checks
tags:
  - intermediate
---

# Merge checks

## Parent
- [[Pull request]]

## Concepts liés
- [[Pull request]]
- [[Code review]]
- [[Approvals]]
- [[CI-CD]]

---

## Définition

Les merge checks sont des conditions automatiques ou manuelles qu'une Pull Request doit satisfaire avant d'autoriser le merge dans la branche cible. Sur GitHub, on les appelle **branch protection rules** + **required status checks**.

---

## Types de checks courants

| Check | Type | Description |
|---|---|---|
| CI pass | Automatique | Tests, lint, build doivent passer |
| Approvals | Manuel | N reviewers doivent approuver |
| Conversations resolved | Manuel | Tous les commentaires doivent être répondus |
| Up-to-date | Automatique | La branche doit être à jour avec `main` |
| No conflicts | Automatique | Pas de conflits de merge |
| Signed commits | Automatique | Commits signés GPG |

---

## Configurer sur GitHub

```
Repository → Settings → Branches → Add branch protection rule

☑ Require a pull request before merging
  ☑ Require approvals: 1
☑ Require status checks to pass before merging
  → Ajouter : "test", "lint", "build"
☑ Require branches to be up to date before merging
☑ Do not allow bypassing the above settings
```

---

## Exemple de workflow protégé

```bash
# La PR est ouverte
# → GitHub Actions lance : tests + lint + build
# → 1 reviewer approuve
# → La branche est à jour avec main
# → Bouton "Merge" devient disponible ✅
```

> [!tip] Automatiser pour ne pas oublier
> Les merge checks remplacent la discipline humaine. Un check qui échoue bloque le merge même si tout le monde a oublié de regarder.
