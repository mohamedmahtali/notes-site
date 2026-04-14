---
title: Secrets management
tags: [security, intermediate]
---

# Secrets management

## Définition

La gestion des secrets consiste à stocker, distribuer et faire tourner les données sensibles (mots de passe, tokens, clés API, certificats) de façon sécurisée, sans les exposer dans le code ou les fichiers de configuration.

> [!warning] Secrets dans le code = faille critique
> Ne jamais committer de secrets dans git. Utiliser gitleaks ou detect-secrets en pre-commit hook pour prévenir les fuites.

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

## Liens

- [[Vault]]
- [[Environment secrets]]
- [[Secret rotation]]
