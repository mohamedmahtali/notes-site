---
title: IAM
tags:
  - intermediate
---
# IAM

---

## Définition

IAM (Identity and Access Management) est le système de contrôle d'accès du [[Cloud]]. Commun à [[AWS]], GCP, et [[Azure]] (sous des noms légèrement différents), il définit qui peut faire quoi sur quelles ressources.

---

## Modèle commun

```
Identity (qui)
  ├── User — personne physique
  ├── Group — ensemble d'users
  ├── Service Account / Role — identité pour les services
  └── Federated Identity — SSO, OIDC

Permission (quoi)
  └── Policy — liste d'actions autorisées/refusées sur des ressources

Binding (association)
  └── Attacher une policy à une identity
```

---

## Comparaison AWS/GCP/Azure

| Concept | AWS | GCP | Azure |
|---|---|---|---|
| Identité service | IAM Role | Service Account | Managed Identity |
| Politique | IAM Policy | IAM Policy | Azure Policy / [[RBAC]] |
| Console | IAM | IAM | [[Azure AD]] |

---

> [!warning]
> Le compte root/admin initial doit être sécurisé avec MFA et ne jamais être utilisé au quotidien. Créer des identités dédiées avec le minimum de [[Permissions]] nécessaires.
