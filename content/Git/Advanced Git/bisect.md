---
title: bisect
tags:
  - advanced
---

# bisect

## Parent
- [[Advanced Git]]

## Concepts liés
- [[Advanced Git]]
- [[Commit history]]
- [[reflog]]

---

## Définition

`git bisect` est un outil de recherche binaire dans l'historique Git. Il permet de trouver **exactement quel commit a introduit un bug** en divisant l'historique en deux à chaque étape, réduisant exponentiellement le nombre de commits à inspecter.

---

## Pourquoi c'est important

> [!tip] Trouver l'origine d'un bug en O(log n)
> Sur 1000 commits, `git bisect` trouve le commit fautif en 10 étapes maximum. Sans bisect, tu inspecterais les commits un par un ou au hasard.

---

## Workflow manuel

```bash
# 1. Démarrer le bisect
git bisect start

# 2. Marquer le commit actuel comme mauvais (bug présent)
git bisect bad

# 3. Marquer un commit ancien où ça fonctionnait
git bisect good v1.0.0
# Git checkout automatiquement un commit au milieu

# 4. Tester → indiquer si bon ou mauvais
git bisect good   # ou
git bisect bad

# → Git continue jusqu'à trouver le premier commit mauvais
# "abc1234 is the first bad commit"

# 5. Terminer et revenir à HEAD
git bisect reset
```

---

## Workflow automatique (recommandé)

```bash
# Créer un script de test
cat > test.sh << 'EOF'
#!/bin/bash
npm test -- --testNamePattern="checkout" --passWithNoTests
EOF
chmod +x test.sh

# Lancer le bisect automatique
git bisect start
git bisect bad HEAD
git bisect good v1.2.0
git bisect run ./test.sh
# → Git trouve automatiquement le commit fautif

git bisect reset
```

---

## Exemple

```bash
git bisect start
git bisect bad                    # HEAD est cassé
git bisect good a3f2c1e           # ce commit fonctionnait

# Git teste ~10 commits au lieu de 1000
# Résultat : "d4e5f6a is the first bad commit"

git show d4e5f6a
# → on voit exactement ce qui a changé
```
