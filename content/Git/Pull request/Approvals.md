---
title: Approvals
tags:
  - intermediate
---

# Approvals

## Parent
- [[Pull request]]

## Concepts liés
- [[Pull request]]
- [[Code review]]
- [[Merge checks]]

---

## Définition

Une approval est la validation formelle d'un reviewer sur une Pull Request. Sur GitHub/GitLab, un reviewer peut **approuver**, **commenter** (sans bloquer), ou **demander des changements** (bloquant). Le nombre d'approvals requis est configurable par branche.

---

## États possibles

| État | Icône | Signification |
|---|---|---|
| Approved | ✅ | Le reviewer valide le merge |
| Changes requested | 🔄 | Modifications nécessaires avant merge |
| Commented | 💬 | Feedback sans avis formel |

---

## Configurer les approvals requis

```
GitHub : Settings → Branches → Branch protection
  → "Require approvals" → nombre minimum (ex: 1 ou 2)
  → "Dismiss stale reviews" → invalide les approvals si nouveau commit pushé
  → "Require review from code owners" → CODEOWNERS file
```

---

## Fichier CODEOWNERS

```bash
# .github/CODEOWNERS
# Les propriétaires du backend doivent approuver les changements dans src/api/
src/api/    @backend-team

# Les changements infra nécessitent une validation
infra/      @sre-team @devops-lead

# Tout le reste : un tech lead suffit
*           @tech-lead
```

---

## Bonnes pratiques

> [!tip]
> - 1 approval minimum sur les projets solo/petites équipes
> - 2 approvals sur les fichiers critiques (infra, auth, paiement)
> - Utiliser CODEOWNERS pour le routage automatique des reviews
> - `Dismiss stale reviews` évite que d'anciens LGTM passent des changements non reviewés
