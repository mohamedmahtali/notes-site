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

## RBAC Azure

```bash
# Lister les rôles disponibles
az role definition list --query '[].roleName' --output table

# Attribuer un rôle à un utilisateur sur un resource group
az role assignment create \
  --assignee user@company.com \
  --role "Contributor" \
  --resource-group myapp-rg

# Créer un rôle custom (lecture seule sur AKS)
az role definition create --role-definition '{
  "Name": "AKS Reader Custom",
  "Actions": [
    "Microsoft.ContainerService/managedClusters/read",
    "Microsoft.ContainerService/managedClusters/listClusterUserCredential/action"
  ],
  "AssignableScopes": ["/subscriptions/<SUBSCRIPTION_ID>"]
}'

# Voir les accès d'un utilisateur
az role assignment list --assignee user@company.com --output table
```

## Service Principal (pour CI/CD)

```bash
# Créer un Service Principal avec rôle Contributor sur un resource group
SP=$(az ad sp create-for-rbac \
  --name "github-actions-sp" \
  --role Contributor \
  --scopes /subscriptions/<SUB>/resourceGroups/myapp-rg \
  --json-auth)

echo $SP
# → {clientId, clientSecret, subscriptionId, tenantId}
# Stocker ces valeurs dans GitHub Actions Secrets
```

> [!tip]
> Utiliser Managed Identities plutôt que Service Principals avec clés. Les Managed Identities n'ont pas de credentials à gérer — Azure les gère automatiquement et les renouvelle.
