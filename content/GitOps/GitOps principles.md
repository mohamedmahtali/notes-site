---
title: GitOps principles
tags:
  - gitops
  - intermediate
---

# GitOps principles

## Définition

Les 4 principes GitOps (formalisés par OpenGitOps/CNCF) définissent les caractéristiques d'un système GitOps valide. Ces principes sont indissociables — les ignorer partiellement revient à faire du CI/CD classique, pas du GitOps.

## Les 4 principes

### 1. Déclaratif

L'état désiré du système est décrit déclarativement, pas impérativement.

```yaml
# ✅ Déclaratif : "je veux 3 replicas"
spec:
  replicas: 3

# ❌ Impératif : "ajoute 2 replicas de plus"
kubectl scale deployment app --replicas=5
```

Les YAML Kubernetes, les charts Helm, les configs Kustomize sont déclaratifs. Un script `kubectl scale` est impératif et n'a pas sa place dans un workflow GitOps.

### 2. Versionné et immuable

Tout l'état désiré est stocké dans [[Git]] avec un historique immuable. Chaque commit = un audit trail.

```bash
# Rollback en GitOps = un revert de commit
git revert abc1234
# → ArgoCD/Flux détecte le changement et revient à l'état précédent
```

Avantages : audit complet (qui a changé quoi, quand, pourquoi), rollback en secondes, review via PR obligatoire.

### 3. Extrait automatiquement (pull-based)

Les agents GitOps ([[ArgoCD]], [[Flux]]) **tirent** les changements depuis Git — ils ne reçoivent pas d'instructions des pipelines.

```
Push (CI/CD classique)        Pull (GitOps)
──────────────────────        ──────────────────────
Pipeline → kubectl apply      Agent scrute Git
Pipeline a accès au cluster   Agent dans le cluster
Credentials externes          Pas de credentials sortants
```

Avantage de sécurité : le cluster n'est jamais accessible depuis l'extérieur. L'agent GitOps fait tout de l'intérieur.

### 4. Réconciliation continue

L'agent compare en permanence l'état désiré (Git) et l'état réel (cluster). Toute dérive est détectée et corrigée.

```
Git : 3 replicas         Cluster : 2 replicas (pod crashé)
     │                              │
     └──── Agent détecte la dérive ─┘
                   │
           Reconciliation → recréé le pod manquant
```

Si quelqu'un fait un `kubectl edit` en prod, l'agent le détecte et revert automatiquement (ou alerte, selon la politique).

## Ce que ces principes changent en pratique

| Avant (CI/CD classique) | Avec GitOps |
|-------------------------|-------------|
| Pipeline déploie en prod | Agent pull depuis Git |
| "Qui a déployé ça ?" | `git log` — trace complète |
| Rollback = redéployer | `git revert` + réconciliation auto |
| Config en live sur cluster | Config dans Git, cluster = reflet |
| Credentials prod dans CI | Aucun credentials sortant |

## Explorer

- **[[Single source of truth]]** — Git comme référentiel unique
- **[[Declarative config]]** — YAML vs scripts impératifs
- **[[Reconciliation loop]]** — mécanisme de détection et correction des dérives
- **[[Pull vs Push]]** — comparaison des deux modèles
