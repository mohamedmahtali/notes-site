---
title: Dynamic secrets
tags: [security, advanced]
---

# Dynamic secrets

## Définition

Les secrets dynamiques sont générés à la demande par Vault, avec un TTL court. Chaque client obtient des credentials uniques qui expirent automatiquement, éliminant les secrets partagés.

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

## Liens

- [[Vault]]
- [[Secret engines]]
- [[Secret rotation]]
