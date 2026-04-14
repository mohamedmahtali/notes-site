---
title: Azure AD
tags:
  - intermediate
---
# Azure AD

## Parent
- [[Azure]]

---

## Définition

Azure Active Directory (Microsoft Entra ID) est le service d'identité et d'accès d'Azure. Il gère l'authentification des utilisateurs, les groupes, les applications, et les Managed Identities pour les services Azure.

---

## Concepts clés

```
Tenant          → organisation Azure AD (lié au domaine company.com)
User            → identité humaine
Group           → ensemble d'utilisateurs
Service Principal → identité pour les applications
Managed Identity → identité automatiquement gérée pour les services Azure
App Registration → enregistrement d'une application pour SSO/OAuth
```

---

## Managed Identity

```bash
# Activer une Managed Identity sur une VM
az vm identity assign   --resource-group myapp-rg   --name myapp-vm

# Donner accès à un Storage Account
az role assignment create   --assignee-object-id $(az vm identity show     --resource-group myapp-rg     --name myapp-vm     --query principalId -o tsv)   --role "Storage Blob Data Contributor"   --scope "/subscriptions/.../resourceGroups/myapp-rg/providers/Microsoft.Storage/storageAccounts/mystorage"
```

---

> [!tip]
> Utiliser Managed Identities plutôt que Service Principals avec clés. Les Managed Identities n'ont pas de credentials à gérer — Azure les gère automatiquement et les renouvelle.
