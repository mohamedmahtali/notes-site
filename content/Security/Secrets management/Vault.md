---
title: HashiCorp Vault
tags: [security, intermediate]
---

# HashiCorp Vault

## Définition

HashiCorp Vault est une solution de gestion de secrets qui stocke, distribue et fait tourner les secrets de façon sécurisée. Il centralise tous les credentials et fournit un audit trail complet.

> [!tip] Pourquoi c'est important
> Vault est le standard de l'industrie pour la gestion des secrets en production. Il supporte des secrets dynamiques (credentials générés à la demande avec TTL), évitant le partage de mots de passe statiques.

## Démarrage rapide

```bash
# Dev mode (pour les tests)
vault server -dev

# Variables d'environnement
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

# Écrire et lire un secret
vault kv put secret/myapp password="s3cr3t"
vault kv get secret/myapp
vault kv get -field=password secret/myapp
```

## Méthodes d'authentification

Vault ne stocke pas les identités — il délègue à des auth backends.

| Method | Usage |
|--------|-------|
| `token` | Par défaut, pour les scripts et tests |
| `approle` | Pour les applications machines (CI/CD) |
| `kubernetes` | Pods K8s s'authentifient via leur ServiceAccount |
| `github` | Développeurs s'authentifient via leur token GitHub |
| `ldap` / `oidc` | Auth entreprise |

```bash
# Activer l'auth Kubernetes
vault auth enable kubernetes

vault write auth/kubernetes/config \
  kubernetes_host="https://kubernetes.default.svc"

# Créer un rôle pour l'app "myapp" dans le namespace "production"
vault write auth/kubernetes/role/myapp \
  bound_service_account_names=myapp \
  bound_service_account_namespaces=production \
  policies=myapp-policy \
  ttl=1h
```

## Policies

Les policies définissent les permissions sur les chemins secrets.

```hcl
# myapp-policy.hcl
path "secret/data/myapp/*" {
  capabilities = ["read"]
}

path "database/creds/myapp" {
  capabilities = ["read"]
}
```

```bash
vault policy write myapp-policy myapp-policy.hcl
```

## Secrets dynamiques (Dynamic secrets)

Vault génère des credentials à la demande avec un TTL — ils sont révoqués automatiquement.

```bash
# Activer le moteur base de données
vault secrets enable database

# Configurer la connexion PostgreSQL
vault write database/config/mydb \
  plugin_name=postgresql-database-plugin \
  allowed_roles="myapp" \
  connection_url="postgresql://{{username}}:{{password}}@db:5432/mydb" \
  username="vault" \
  password="vaultpass"

# Définir le rôle avec un TTL de 1h
vault write database/roles/myapp \
  db_name=mydb \
  creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
  default_ttl="1h" \
  max_ttl="24h"

# Obtenir un credential (généré à la volée)
vault read database/creds/myapp
```

> [!tip] Avantage clé
> Chaque appel génère un utilisateur unique. Si l'appli est compromise, le credential expire automatiquement — pas de rotation manuelle.

## Liens

- [[Tokens]]
- [[Policies]]
- [[Secret engines]]
- [[Dynamic secrets]]
- [[Secrets management]]
