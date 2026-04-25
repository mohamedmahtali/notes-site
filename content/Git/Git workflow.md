---
title: Git workflow
tags:
  - intermediate
---
# Git workflow

---

## Définition

Un workflow [[Git]] est un ensemble de conventions qui définit comment les développeurs créent des branches, committent, et mergent leur code. Le choix du workflow impacte directement la fréquence de déploiement, la complexité des [[Merge]], et la collaboration.

---

## Pourquoi c'est important

> [!tip] Convention > improvisation
> Sans workflow défini, chaque développeur branching comme il veut. Le résultat : des merges chaos, des conflits fréquents, et un historique illisible. Un workflow clair évite tout ça.

---

## Les trois workflows principaux

| Workflow | Complexité | Déploiement | Idéal pour |
|---|---|---|---|
| [[GitHub flow]] | Simple | Continu (plusieurs/jour) | Web, [[SaaS]], CI/CD |
| [[Git flow]] | Complexe | Par release planifiée | Logiciel versionné |
| [[Trunk based development\|Trunk Based Dev]] | Simple | Continu (très fréquent) | Grandes équipes, [[DevOps]] mature |

---

## Choisir son workflow

```
Tu déploies plusieurs fois par semaine ?
  → GitHub flow ou Trunk Based Development

Tu as des cycles de release définis (v1.0, v2.0) ?
  → Git flow

Tu as une grande équipe avec feature flags ?
  → Trunk Based Development

Tu démarres un projet solo ou petite équipe ?
  → GitHub flow (le plus simple)
```

---

> [!note]
> Quel que soit le workflow, la règle commune est identique : **`main` doit toujours être dans un état déployable**.
