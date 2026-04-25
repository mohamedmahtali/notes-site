---
title: IAM
tags:
  - intermediate
---
# IAM

---

## Définition

GCP IAM (Identity and Access Management) contrôle les accès aux ressources GCP. Il utilise un modèle de binding : attacher un rôle à un membre (user, group, service account) sur une ressource.

---

## Concepts GCP IAM

```
Member (qui) :
  - user:alice@company.com
  - group:devops@company.com
  - serviceAccount:myapp@project.iam.gserviceaccount.com
  - allUsers (accès public)

Role (permissions) :
  - Primitifs : Owner, Editor, Viewer (trop larges)
  - Prédéfinis : roles/storage.objectViewer, roles/container.developer
  - Personnalisés : créés par l'utilisateur

Binding :
  - Membre + Rôle + Resource
```

---

## Commandes

```bash
# Attacher un rôle
gcloud projects add-iam-policy-binding my-project   --member="serviceAccount:myapp@my-project.iam.gserviceaccount.com"   --role="roles/storage.objectAdmin"

# Créer un Service Account
gcloud iam service-accounts create myapp-sa   --display-name="My App Service Account"

# Générer une clé (éviter si possible — utiliser Workload Identity)
gcloud iam service-accounts keys create key.json   --iam-account=myapp-sa@my-project.iam.gserviceaccount.com
```

---

> [!tip]
> Utiliser Workload Identity plutôt que les clés JSON pour les applications [[GKE]]. Ça associe un Service Account [[Kubernetes]] à un Service Account GCP sans clé à gérer.
