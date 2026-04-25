---
title: Secrets management
tags:
  - security
  - intermediate
---

# Secrets management

## Définition

La gestion des [[Secrets]] consiste à stocker, distribuer et faire tourner les données sensibles (mots de passe, [[Tokens]], clés API, certificats) de façon sécurisée, sans les exposer dans le code ou les fichiers de configuration.

> [!warning] Secrets dans le code = faille critique
> Ne jamais committer de secrets dans [[Git]]. Utiliser gitleaks ou detect-secrets en [[pre-[[Commit]]]] hook pour prévenir les fuites.

## Hiérarchie des solutions

```
Code/Env vars        ← Interdit pour les secrets
→ .env (gitignored)  ← Acceptable en dev
→ K8s Secrets        ← Base, mais encodé en base64 seulement
→ Sealed Secrets     ← Chiffré, stockable dans git
→ HashiCorp Vault    ← Solution enterprise complète
→ AWS Secrets Manager / GCP Secret Manager
```

## Kubernetes Secrets

```bash
# Créer un secret
kubectl create secret generic db-creds   --from-literal=username=admin   --from-literal=password=s3cr3t

# Injecter dans un pod
kubectl set env deployment/myapp   --from=secret/db-creds
```

## Prévenir les leaks avec pre-commit

```bash
# gitleaks — scanner les commits avant qu'ils partent
brew install gitleaks

# Scan du repo
gitleaks detect --source .

# Hook pre-commit (dans .git/hooks/pre-commit)
#!/bin/bash
gitleaks protect --staged -v
```

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

## Sealed Secrets — secrets chiffrés dans Git

```bash
# Installer kubeseal
brew install kubeseal

# Chiffrer un secret K8s (seul le cluster peut le déchiffrer)
kubectl create secret generic db-creds \
  --from-literal=password=s3cr3t \
  --dry-run=client -o yaml | \
  kubeseal --format yaml > db-creds-sealed.yaml

# db-creds-sealed.yaml peut être commité dans Git (chiffré RSA)
git add db-creds-sealed.yaml
```

## External Secrets Operator — sync depuis Vault/AWS/GCP

```yaml
# Synchroniser un secret depuis AWS Secrets Manager
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: db-credentials     # Nom du Secret K8s créé
  data:
  - secretKey: password
    remoteRef:
      key: production/myapp/db
      property: password
```

## Rotation des secrets

```bash
# AWS — rotation automatique d'un secret RDS
aws secretsmanager rotate-secret \
  --secret-id production/myapp/db \
  --rotation-rules AutomaticallyAfterDays=30

# Vault — configurer la rotation automatique (dynamic secrets)
# Les credentials sont générés à la demande avec TTL
# → Pas de rotation manuelle nécessaire
```

> [!tip] Bonne pratique : préférer les secrets dynamiques
> Un secret dynamique (Vault, [[AWS]] RDS [[IAM]] auth) n'existe que le temps d'une session. Même s'il est intercepté, il expire automatiquement. Supérieur à une rotation périodique d'un secret statique.

## Liens

- [[Vault]]
- [[Environment secrets]]
- [[Secret rotation]]
