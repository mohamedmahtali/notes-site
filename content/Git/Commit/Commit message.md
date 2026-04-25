---
title: Commit message
tags:
  - beginner
---

# Commit message

---

## Définition

Un [[Commit]] message est la description textuelle associée à un commit [[Git]]. Il documente **pourquoi** une modification a été faite, et non ce qui a été changé (le diff le montre déjà).

Un bon message de commit est une forme de documentation qui aide les coéquipiers — et toi dans 6 mois — à comprendre l'historique du projet.

---

## Pourquoi c'est important

> [!warning] Un mauvais message de commit coûte cher
> `fix bug`, `wip`, `update` — ces messages sont inutiles lors d'un `git log` ou d'un débogage. Un historique lisible accélère les reviews et le diagnostic des régressions.

---

## Convention : Conventional Commits

Le standard le plus adopté en [[DevOps]] et open source :

```
<type>(<scope>): <description courte>

[corps optionnel]

[footer optionnel]
```

### Types courants

| Type | Usage |
|---|---|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation uniquement |
| `chore` | Tâches de maintenance (deps, config) |
| `refactor` | Refactoring sans changement de comportement |
| `ci` | Modifications des [[Pipeline]] CI/CD |
| `test` | Ajout ou correction de tests |
| `perf` | Amélioration des performances |

---

## Exemples

```bash
# ✅ Bon
git commit -m "feat(auth): add JWT token refresh logic"
git commit -m "fix(api): handle null response from external service"
git commit -m "ci: add docker build cache to GitHub Actions workflow"
git commit -m "docs: update README with local setup instructions"

# ❌ Mauvais
git commit -m "fix"
git commit -m "update fichier"
git commit -m "wip"
git commit -m "aaaa"
```

### Commit avec corps

```bash
git commit -m "fix(k8s): increase memory limit on worker pods

Worker pods were OOMKilled under high load due to insufficient memory.
Increased limit from 256Mi to 512Mi based on observed peak usage.

Closes #142"
```

---

## Règles d'or

1. **Ligne de titre ≤ 72 caractères**
2. **Utiliser l'impératif** : "add feature" et non "added feature"
3. **Expliquer le pourquoi**, pas le comment
4. **Un commit = une intention** — ne pas mélanger plusieurs changements non liés

> [!tip] Automatiser avec un hook
> Utilise un [[commit-msg|hook commit-msg]] pour valider automatiquement le format des messages avant chaque commit.
