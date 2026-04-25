---
title: Dynamic secrets
tags:
  - security
  - advanced
---

# Dynamic secrets

## Définition

Les [[Secrets]] dynamiques sont générés à la demande par Vault, avec un [[TTL]] court. Chaque client obtient des credentials uniques qui expirent automatiquement, éliminant les secrets partagés.

> [!tip] Avantage clé
> Avec les secrets dynamiques, si des credentials sont compromis, ils expirent rapidement. Pas de rotation manuelle nécessaire. Chaque application a ses propres credentials traçables.

## Secrets dynamiques AWS

```bash
# Configurer le backend AWS
vault secrets enable aws

vault write aws/config/root   access_key=AKIAIOSFODNN7EXAMPLE   secret_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY   region=eu-west-1

# Créer un role AWS
vault write aws/roles/s3-readonly   credential_type=iam_user   policy_arns=arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Obtenir des credentials AWS dynamiques
vault read aws/creds/s3-readonly
# → access_key, secret_key, security_token (TTL: 1h)
```

## Secrets dynamiques Database

```bash
# Obtenir des credentials PostgreSQL dynamiques
vault read database/creds/readonly
# Retourne: username, password (uniques, TTL 1h)
# L'utilisateur est créé en temps réel dans la DB
# Révoqué automatiquement à l'expiration du TTL
```

## Secrets dynamiques Kubernetes (Vault Agent Injector)

Injecter des secrets dans les [[Pods]] sans les stocker dans [[Kubernetes]] Secrets.

```yaml
# Annotation sur le pod → Vault Agent injecte le secret en sidecar
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    metadata:
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/role: "myapp"
        # Injecte le secret dans /vault/secrets/db-creds
        vault.hashicorp.com/agent-inject-secret-db-creds: "database/creds/myapp"
        # Template pour formater le secret
        vault.hashicorp.com/agent-inject-template-db-creds: |
          {{- with secret "database/creds/myapp" -}}
          export DB_USER="{{ .Data.username }}"
          export DB_PASSWORD="{{ .Data.password }}"
          {{- end }}
```

```bash
# Dans le conteneur, sourcer le fichier injecté
source /vault/secrets/db-creds
echo $DB_USER   # → v-myapp-xyz123 (credentials dynamiques)
```

## Révoquer un secret avant expiration

```bash
# Révoquer un lease spécifique immédiatement
vault lease revoke database/creds/myapp/abc123-lease-id

# Révoquer tous les leases d'un role
vault lease revoke -prefix database/creds/myapp

# Voir les leases actifs
vault list sys/leases/lookup/database/creds/myapp
```

> [!tip] Renouveler un lease
> Si une application a besoin d'utiliser ses credentials plus longtemps, elle peut renouveler son lease avant expiration : `vault lease renew <lease-id>`. Le TTL max est défini dans le rôle.

## Liens

- [[Vault]]
- [[Secret engines]]
- [[Secret rotation]]
