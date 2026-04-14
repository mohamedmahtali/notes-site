---
title: Azure provider
tags:
  - intermediate
---
# Azure provider

## Parent
- [[Terraform providers]]

---

## Définition

Le provider AzureRM gère les ressources Azure. Il supporte l'authentification via Service Principal, Managed Identity, ou Azure CLI.

---

## Configuration

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = true
    }
  }
  # Authentification via env vars :
  # ARM_CLIENT_ID, ARM_CLIENT_SECRET, ARM_TENANT_ID, ARM_SUBSCRIPTION_ID
  # Ou via Azure CLI : az login
}

# Resource Group
resource "azurerm_resource_group" "main" {
  name     = "myapp-rg"
  location = "West Europe"
}

# Virtual Network
resource "azurerm_virtual_network" "main" {
  name                = "myapp-vnet"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  address_space       = ["10.0.0.0/16"]
}
```
