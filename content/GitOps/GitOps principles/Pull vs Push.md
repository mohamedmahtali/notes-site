---
title: Pull vs Push
tags: [gitops, intermediate]
---

# Pull vs Push (modèles de déploiement)

## Définition

Il existe deux modèles pour synchroniser l'état d'un cluster avec Git. GitOps privilégie le modèle **pull** pour des raisons de sécurité.

> [!tip] Pourquoi le pull est plus sûr
> Avec le pull, le pipeline CI n'a jamais accès au cluster de production. Seul l'agent qui tourne DANS le cluster peut modifier le cluster. Moins de credentials à gérer, moins de surface d'attaque.

## Comparaison

| Critère | Push (CI/CD classique) | Pull (GitOps) |
|---------|----------------------|---------------|
| Qui initie | Pipeline CI externe | Agent dans le cluster |
| Accès prod | Pipeline a les credentials | Pas de credentials externes |
| Synchronisation | Ponctuelle (à chaque deploy) | Continue (polling/webhook) |
| Dérive détectée | Non | Oui (auto-corrected) |
| Audit trail | Dans le CI | Dans Git |
| Exemples | GitHub Actions + kubectl | ArgoCD, Flux |

## Architecture Pull (GitOps)

```
Developer → git push → GitHub
                            ↑ poll (60s)
                       [ArgoCD / Flux]
                       (dans le cluster)
                            ↓ apply si diff
                       [Kubernetes cluster]
```

## Liens

- [[GitOps principles]]
- [[Reconciliation loop]]
- [[ArgoCD]]
- [[Flux]]
