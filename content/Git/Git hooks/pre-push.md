---
title: pre-push
tags:
  - intermediate
---

# pre-push

---

## Définition

Le hook `pre-push` s'exécute juste avant un `git push`. Il reçoit sur [[stdin]] les références qui vont être poussées. Si le script retourne un code d'erreur, le push est annulé. C'est le dernier filet avant que le code parte vers le remote et déclenche la CI.

---

## Cas d'usage

| Vérification | Quand utile |
|---|---|
| Tests complets | Avant de déclencher la CI (éviter les runs inutiles) |
| Build de vérification | S'assurer que le build passe |
| Vérification de branche | Interdire le push direct sur main |

---

## Exemple – tests + protection de main

```bash
# .git/hooks/pre-push
#!/bin/bash

BRANCH=$(git symbolic-ref HEAD 2>/dev/null | cut -d'/' -f3)

# Interdire le push direct sur main
if [ "$BRANCH" = "main" ]; then
  echo "❌ Direct push to main is not allowed."
  echo "   Please create a Pull Request."
  exit 1
fi

# Lancer les tests
echo "🧪 Running tests before push..."
npm test -- --passWithNoTests --watchAll=false

if [ $? -ne 0 ]; then
  echo "❌ Tests failed. Push aborted."
  exit 1
fi

echo "✅ All checks passed. Pushing..."
exit 0
```

```bash
chmod +x .git/hooks/pre-push
```

---

> [!note] CI ne remplace pas les hooks locaux
> Les hooks locaux donnent un feedback immédiat (< 30s). La CI donne un feedback après plusieurs minutes. Les deux sont complémentaires : les hooks évitent les runs CI inutiles, la CI valide dans un environnement propre.
