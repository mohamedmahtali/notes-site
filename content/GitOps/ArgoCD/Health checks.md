---
title: Health checks
tags: [gitops, intermediate]
---

# Health checks (ArgoCD)

## Définition

ArgoCD évalue automatiquement la santé de chaque ressource Kubernetes déployée. Les health checks permettent de savoir si un déploiement s'est bien passé, sans monitorer manuellement.

> [!tip] Déploiements progressifs
> ArgoCD attend que les ressources soient `Healthy` avant de marquer le sync comme réussi. Si un Deployment ne devient pas healthy (ex: ImagePullBackOff), ArgoCD le signale immédiatement.

## États de santé

| État | Description |
|------|-------------|
| `Healthy` | Ressource fonctionne normalement |
| `Progressing` | Ressource en cours de démarrage |
| `Degraded` | Ressource en erreur |
| `Suspended` | Ressource en pause (ex: CronJob) |
| `Missing` | Ressource absente du cluster |
| `Unknown` | Pas de health check disponible |

## Health check personnalisé (Lua)

```yaml
# ConfigMap argocd-cm — health check pour une CRD custom
data:
  resource.customizations.health.mygroup_MyResource: |
    hs = {}
    if obj.status ~= nil then
      if obj.status.phase == "Running" then
        hs.status = "Healthy"
        hs.message = "Resource is running"
      elseif obj.status.phase == "Failed" then
        hs.status = "Degraded"
        hs.message = obj.status.message
      else
        hs.status = "Progressing"
      end
    end
    return hs
```

## Liens

- [[ArgoCD]]
- [[Applications]]
- [[Sync policies]]
