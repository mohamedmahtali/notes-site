---
title: External secrets
tags:
  - advanced
---
# External secrets

## Parent
- [[Secrets]]

---

## Définition

External Secrets Operator (ESO) synchronise des secrets depuis des gestionnaires externes (AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager) vers des Secrets Kubernetes. Les secrets ne vivent pas dans Kubernetes — ils sont fetched à la demande.

---

## Pourquoi c'est important

> [!tip] Secrets hors du cluster = meilleure sécurité
> Avec ESO : les secrets sont dans AWS/Vault (auditables, rotatables, avec accès fine-grained). Les Secrets K8s sont des copies temporaires, automatiquement mises à jour. Pas de secrets dans git, pas de secrets dans etcd sans chiffrement explicite.

---

## Installation

```bash
helm repo add external-secrets https://charts.external-secrets.io
helm install external-secrets external-secrets/external-secrets   --namespace external-secrets --create-namespace
```

---

## Configuration AWS Secrets Manager

```yaml
# SecretStore — connexion au provider
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secretstore
  namespace: production
spec:
  provider:
    aws:
      service: SecretsManager
      region: eu-west-1
      auth:
        serviceAccount:
          name: external-secrets-sa

---
# ExternalSecret — définit quel secret synchroniser
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secretstore
    kind: SecretStore
  target:
    name: db-credentials     # nom du Secret K8s créé
  data:
  - secretKey: password      # clé dans le Secret K8s
    remoteRef:
      key: prod/myapp/db     # chemin dans AWS Secrets Manager
      property: password     # propriété JSON
```
