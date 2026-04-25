---
title: Releases
tags:
  - intermediate
---
# Releases

---

## Définition

Une release [[Helm]] est une instance d'un chart déployée dans un [[Cluster]] [[Kubernetes]]. Le même chart peut être installé plusieurs fois sous différents noms de release (ex: `myapp-staging`, `myapp-production`). Helm garde l'historique de chaque release.

---

## Gestion des releases

```bash
# Lister toutes les releases
helm list
helm list -n production
helm list -A              # tous les namespaces

# Statut d'une release
helm status myapp

# Historique d'une release
helm history myapp
# REVISION  STATUS     CHART          DESCRIPTION
# 1         superseded myapp-1.0.0    Install complete
# 2         superseded myapp-1.1.0    Upgrade complete
# 3         deployed   myapp-1.2.0    Upgrade complete

# Voir les values d'une release
helm get values myapp
helm get values myapp --all    # y compris les défauts

# Voir les manifests d'une release
helm get manifest myapp

# Rollback
helm rollback myapp 2          # revenir à la revision 2
helm rollback myapp            # revision précédente

# Supprimer une release
helm uninstall myapp
helm uninstall myapp --keep-history  # garder l'historique
```

---

> [!tip]
> Utiliser `helm upgrade --install myapp ./chart` dans les [[Pipeline]] CI/CD — crée la release si elle n'existe pas, ou la met à jour si elle existe. Idempotent et safe pour l'automatisation.
