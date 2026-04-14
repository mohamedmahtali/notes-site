---
title: commit-msg
tags:
  - intermediate
---

# commit-msg

## Parent
- [[Git hooks]]

## Concepts liés
- [[Git hooks]]
- [[pre-commit]]
- [[Commit message]]

---

## Définition

Le hook `commit-msg` valide le **message de commit** avant de finaliser le commit. Git lui passe le chemin vers un fichier temporaire contenant le message. Si le script retourne un code d'erreur, le commit est annulé avec une indication de l'erreur.

---

## Exemple – valider le format Conventional Commits

```bash
# .git/hooks/commit-msg
#!/bin/bash

MSG_FILE=$1
MSG=$(cat "$MSG_FILE")

# Pattern : type(scope): description
PATTERN="^(feat|fix|docs|chore|refactor|ci|test|perf|revert|style|build)(\(.+\))?: .{1,72}$"

if ! echo "$MSG" | grep -qE "$PATTERN"; then
  echo ""
  echo "❌ Invalid commit message format!"
  echo ""
  echo "   Expected: <type>(<scope>): <description>"
  echo "   Example:  feat(auth): add JWT middleware"
  echo ""
  echo "   Types: feat, fix, docs, chore, refactor, ci, test, perf"
  echo ""
  exit 1
fi

echo "✅ Commit message format OK"
exit 0
```

```bash
chmod +x .git/hooks/commit-msg
```

---

## Outil alternatif : commitlint

```bash
# Installation
npm install --save-dev @commitlint/cli @commitlint/config-conventional

# Configuration
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js

# Hook (avec husky)
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit $1'
```

---

> [!tip]
> Le hook `commit-msg` est plus puissant que simplement lire la doc des conventions — il les **impose** automatiquement. Impossible d'oublier ou de skippper par flemme.
