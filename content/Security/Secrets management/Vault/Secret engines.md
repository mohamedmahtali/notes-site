---
title: Secret engines
tags: [security, advanced]
---

# Secret engines

## Définition

Les secret engines sont les backends de Vault qui stockent, génèrent ou chiffrent des données. Chaque engine a un comportement spécifique (KV statique, secrets dynamiques, PKI, chiffrement...).

> [!note] Engines principaux
> KV (Key-Value), Database, AWS, PKI, Transit (chiffrement as a service), SSH, TOTP.

## Secret engine KV v2

```bash
# Activer le KV v2
vault secrets enable -path=secret kv-v2

# Écrire/lire un secret avec versioning
vault kv put secret/myapp key=value
vault kv get secret/myapp
vault kv get -version=2 secret/myapp

# Voir l'historique des versions
vault kv metadata get secret/myapp
```

## Secret engine Database

```bash
# Configurer PostgreSQL
vault secrets enable database

vault write database/config/postgres   plugin_name=postgresql-database-plugin   connection_url="postgresql://vault:{{password}}@db:5432/mydb"   allowed_roles="readonly"

# Créer un role pour générer des credentials
vault write database/roles/readonly   db_name=postgres   creation_statements="CREATE ROLE '{{name}}' WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO '{{name}}';"
  default_ttl="1h"
  max_ttl="24h"

# Obtenir des credentials dynamiques
vault read database/creds/readonly
```

## Secret engine PKI

```bash
# Activer et configurer le PKI
vault secrets enable pki
vault write pki/root/generate/internal   common_name="internal-ca"   ttl=87600h

# Émettre un certificat
vault write pki/issue/web-role   common_name="web.internal"
```

## Liens

- [[Vault]]
- [[Dynamic secrets]]
- [[Policies]]
