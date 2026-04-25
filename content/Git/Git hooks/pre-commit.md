---
title: pre-commit
tags:
  - intermediate
---

# pre-commit

---

## Définition

Le hook `pre-commit` est un script exécuté automatiquement par [[Git]] **juste avant la création d'un [[Commit]]**. Si le script retourne un code d'erreur (≠ 0), le commit est annulé. C'est la première ligne de défense pour la qualité du code.

---

## Cas d'usage courants

| Vérification | Outil |
|---|---|
| Lint du code | ESLint, flake8, golangci-lint |
| Formatage | Prettier, black, gofmt |
| Tests rapides | `npm test -- --watch=false` |
| [[Secrets]] exposés | detect-secrets, gitleaks |
| Taille des fichiers | vérification custom |

---

## Créer un hook pre-commit

```bash
# Emplacement : .git/hooks/pre-commit
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
set -e

echo "🔍 Running linter..."
npm run lint

echo "🧪 Running tests..."
npm test -- --passWithNoTests

echo "✅ Pre-commit checks passed"
EOF

chmod +x .git/hooks/pre-commit
```

---

## Outil recommandé : pre-commit framework

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: detect-private-key

  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
```

```bash
pip install pre-commit
pre-commit install   # installe le hook dans .git/hooks/
pre-commit run --all-files  # tester sans committer
```

---

> [!tip]
> Partager `.pre-commit-config.yaml` dans le dépôt pour que toute l'équipe ait les mêmes vérifications. Les hooks dans `.git/hooks/` ne sont pas versionnés.
