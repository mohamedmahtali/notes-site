---
title: Code review
tags:
  - beginner
---

# Code review

## Parent
- [[Pull request]]

## Concepts liés
- [[Pull request]]
- [[Merge checks]]
- [[Approvals]]
- [[Commit message]]

---

## Définition

La code review est le processus par lequel un ou plusieurs développeurs examinent les changements proposés dans une Pull Request avant le merge. C'est un filet de sécurité qualité et un vecteur de partage de connaissance.

---

## Pourquoi c'est important

> [!tip] Qualité et connaissance partagée
> Une bonne review attrape les bugs avant la production, maintient la cohérence du code, et fait monter l'équipe en compétence. C'est aussi une documentation vivante des décisions techniques.

---

## Ce qu'on vérifie

| Aspect | Questions clés |
|---|---|
| **Logique** | Le code fait-il ce qu'il prétend ? Y a-t-il des cas limites non gérés ? |
| **Lisibilité** | Le code est-il compréhensible sans explication ? |
| **Sécurité** | Y a-t-il des injections, données sensibles exposées, auth manquante ? |
| **Performance** | Y a-t-il des requêtes N+1, des boucles inutiles, des ressources non libérées ? |
| **Tests** | Les nouveaux comportements sont-ils couverts par des tests ? |

---

## Bonnes pratiques du reviewer

```
✅ Commenter le code, pas la personne
✅ Expliquer le "pourquoi" de chaque remarque
✅ Distinguer blocant (must fix) / suggestion (nice to have)
✅ Approuver avec des commentaires mineurs plutôt que bloquer
✅ Lire la description de la PR avant de plonger dans le diff
```

---

## Bonnes pratiques de l'auteur

```
✅ PR petite et focalisée sur un seul sujet
✅ Description claire : contexte, changements, comment tester
✅ Auto-review avant de demander une review
✅ Répondre à tous les commentaires (fix ou justification)
```

> [!note]
> Une PR de 50 lignes reçoit une vraie review. Une PR de 1000 lignes reçoit "LGTM" par lassitude.
