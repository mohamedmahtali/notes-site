---
title: Vault Tokens
tags:
  - security
  - intermediate
---

# Vault Tokens

## Définition

Les tokens Vault sont les credentials d'authentification utilisés pour accéder à Vault. Chaque token a des policies attachées qui définissent ses [[Permissions]], ainsi qu'un [[TTL]] (Time To Live).

> [!note] Token root
> Le token root a tous les droits. Il doit être révoqué après l'initialisation de Vault et recréé uniquement si nécessaire.

## Gestion des tokens

```bash
# Créer un token avec TTL et policies
vault token create   -policy="readonly"   -ttl="1h"   -display-name="myapp-token"

# Voir les infos du token actuel
vault token lookup

# Renouveler un token
vault token renew

# Révoquer un token
vault token revoke <token_id>

# Révoquer tous les tokens d'un accessor
vault token revoke -accessor <accessor>
```

## Token Roles

```bash
# Créer un token role (template de token)
vault write auth/token/roles/myapp-role   allowed_policies="myapp-policy"   period="24h"   renewable=true

# Créer un token depuis le role
vault token create -role=myapp-role
```

## Liens

- [[Vault]]
- [[Policies]]
- [[Secrets management]]
