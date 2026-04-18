---
title: GitOps
tags: [gitops, intermediate]
---

# GitOps

## Définition

GitOps est une approche opérationnelle qui utilise Git comme source de vérité unique pour l'infrastructure et les applications. Tout changement d'état du système passe par un commit git, et un agent automatique (ArgoCD, Flux) réconcilie l'état réel vers l'état déclaré dans Git.

> [!tip] Pourquoi c'est important
> GitOps donne à l'infrastructure les mêmes garanties que le code : historique complet, rollback en un commit, revue via PR, audit trail automatique. Il élimine les "apply manuel en prod" et réduit les erreurs humaines.

## Principes fondamentaux

```
1. Git = source de vérité unique
2. Configuration déclarative (YAML, Helm, Kustomize)
3. Réconciliation automatique (pull-based)
4. Opérations via PR/MR, pas via kubectl direct
```

## GitOps vs DevOps classique (push vs pull)

```
Push (CI/CD classique)        Pull (GitOps)
──────────────────────        ─────────────────────────
CI pipeline → kubectl apply   Git → Agent détecte diff
Pipeline a accès à prod       Agent dans le cluster
Accès credentials prod        Pas de credentials externes
Synchronisation ponctuelle    Réconciliation continue
```

## Outils principaux

- **[[ArgoCD]]** — UI riche, GitOps pour Kubernetes, très populaire
- **[[Flux]]** — Natif CNCF, plus léger, intégration Helm/Kustomize

## Liens

- [[GitOps principles]]
- [[ArgoCD]]
- [[Flux]]
- [[Environments]]
- [[CI-CD]]
- [[Kubernetes]]
