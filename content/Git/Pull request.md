---
title: Pull request
tags:
  - intermediate
---
# Pull request

---

## Définition

Une Pull Request (PR) — ou [[Merge]] Request (MR) sur GitLab — est une demande formelle d'intégrer les modifications d'une branche dans une autre. C'est le point central de la collaboration : code review, CI automatique, discussions, et merge s'y déroulent.

---

## Pourquoi c'est important

> [!tip] Plus qu'un simple merge
> Une PR est une conversation autour d'un changement : contexte, tests, review, approbation. Elle crée une traçabilité permanente du pourquoi d'un changement.

---

## Anatomie d'une bonne PR

```markdown
## Contexte
Pourquoi ce changement est-il nécessaire ?

## Changements
- Ajout du middleware JWT pour l'authentification
- Tests unitaires pour les cas d'erreur
- Mise à jour de la documentation API

## Comment tester
1. `npm install && npm start`
2. POST /api/login avec { email, password }
3. Vérifier que le token est retourné

## Screenshots (si UI)
[avant / après]
```

---

## Workflow

```bash
# 1. Créer une branche
git checkout -b feature/ajout-auth

# 2. Développer + committer
git commit -m "feat(auth): add JWT middleware"

# 3. Pousser
git push -u origin feature/ajout-auth

# 4. Créer la PR sur GitHub (UI ou CLI)
gh pr create --title "feat: add JWT authentication" --body "..."

# 5. CI s'exécute automatiquement
# 6. Code review
# 7. Merge
gh pr merge --squash
```

---

## Checklist avant d'ouvrir une PR

```
☑ Branche à jour avec main (git rebase origin/main)
☑ Tests passent localement
☑ Description claire avec contexte et instructions de test
☑ Auto-review du diff avant soumission
☑ PR < 400 lignes (sinon découper)
```

---

> [!note]
> Voir [[Code review]], [[Approvals]], [[Merge checks]] pour les sous-processus d'une PR.
