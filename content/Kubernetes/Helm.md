---
title: Helm
tags:
  - intermediate
---
# Helm

---

## Définition

Helm est le gestionnaire de [[Package]] pour [[Kubernetes]]. Un chart Helm est un ensemble de templates YAML paramétrables qui décrit une application Kubernetes complète. Helm simplifie le déploiement, la mise à jour, et le [[Rollback]] d'applications complexes.

---

## Pourquoi c'est important

> [!tip] npm pour Kubernetes
> Sans Helm, déployer une stack complète (Deployment + Service + [[Ingress]] + ConfigMap + Secret + [[RBAC]]) requiert d'appliquer et maintenir des dizaines de fichiers YAML. Helm les regroupe en un package versionné.

---

## Commandes essentielles

```bash
# Ajouter un repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Chercher un chart
helm search repo nginx
helm search hub prometheus

# Installer
helm install myrelease bitnami/nginx
helm install myapp ./my-chart --namespace prod --create-namespace

# Avec override de valeurs
helm install myapp bitnami/nginx   --set replicaCount=3   --values custom-values.yaml

# Voir les releases installées
helm list
helm list -A          # tous les namespaces

# Mettre à jour
helm upgrade myapp bitnami/nginx --set replicaCount=5
helm upgrade --install myapp ./my-chart   # install si n'existe pas

# Rollback
helm rollback myapp 1    # revenir à la revision 1
helm history myapp       # voir l'historique

# Supprimer
helm uninstall myapp
```

---

> [!note]
> Voir [[Charts]] pour la structure d'un chart, [[Templates]] pour la syntaxe Go template, [[Values]] pour la configuration.

## Explorer

- **[[Helm/Releases]]** — releases, révisions, rollback
- **[[Charts]]** — structure d'un chart, Chart.yaml, templates/
- **[[Kubernetes]]** — contexte Kubernetes, déploiements sans Helm
- **[[GitOps]]** — ArgoCD/Flux qui synchronisent des charts Helm depuis Git
