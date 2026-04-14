---
title: Secret rotation
tags: [security, intermediate]
---

# Secret rotation

## Définition

La rotation des secrets consiste à renouveler régulièrement les credentials (mots de passe, tokens, clés) pour limiter la fenêtre d'exposition en cas de compromission.

> [!tip] Rotation automatique
> La rotation manuelle est oubliée. Automatiser la rotation avec Vault Dynamic Secrets ou AWS Secrets Manager pour des credentials toujours frais.

## Rotation avec Vault

```bash
# Configurer la rotation automatique d'un secret
vault write database/config/mydb   plugin_name=postgresql-database-plugin   connection_url="postgresql://{{username}}:{{password}}@db:5432/mydb"   allowed_roles="readonly"   rotation_period=24h

# Déclencher une rotation manuelle
vault write -force database/rotate-root/mydb
```

## AWS Secrets Manager

```bash
# Activer la rotation automatique
aws secretsmanager rotate-secret   --secret-id myapp/db/password   --rotation-lambda-arn arn:aws:lambda:...   --rotation-rules AutomaticallyAfterDays=30
```

## Rotation dans Kubernetes

```yaml
# External Secrets Operator avec rotation
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-secret
spec:
  refreshInterval: 1h  # Récupère la dernière version toutes les heures
  secretStoreRef:
    name: vault-backend
  target:
    name: db-creds
  data:
    - secretKey: password
      remoteRef:
        key: secret/db
        property: password
```

## Liens

- [[Secrets management]]
- [[Vault]]
- [[Environment secrets]]
