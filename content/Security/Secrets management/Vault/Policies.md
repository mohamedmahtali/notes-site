---
title: Vault Policies
tags: [security, intermediate]
---

# Vault Policies

## Définition

Les policies Vault définissent les permissions d'accès aux paths de secrets. Elles suivent le principe de moindre privilège et sont écrites en HCL (HashiCorp Configuration Language).

> [!tip] Default deny
> Vault suit un modèle default-deny. Si une policy ne mentionne pas un path, l'accès est refusé. Les policies doivent explicitement autoriser chaque opération.

## Syntaxe des policies

```hcl
# Policy pour une application
path "secret/data/myapp/*" {
  capabilities = ["read", "list"]
}

path "secret/data/myapp/db" {
  capabilities = ["read"]
}

# Capacités disponibles
# create, read, update, delete, list, sudo, deny
```

## Gestion des policies

```bash
# Écrire une policy
vault policy write myapp-policy policy.hcl

# Lister les policies
vault policy list

# Lire une policy
vault policy read myapp-policy

# Attacher une policy à un token
vault token create -policy="myapp-policy"
```

## Liens

- [[Vault]]
- [[Tokens]]
- [[Secret engines]]
