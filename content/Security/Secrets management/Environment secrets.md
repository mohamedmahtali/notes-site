---
title: Environment secrets
tags: [security, beginner]
---

# Environment secrets

## Définition

Les secrets d'environnement sont des valeurs sensibles injectées dans les processus via des variables d'environnement. C'est la méthode la plus simple, mais aussi la plus risquée si mal utilisée.

> [!warning] Risques des variables d'environnement
> Les variables d'env sont visibles via `/proc/<pid>/environ`, dans les logs d'erreur, et dans les outils de debug. Préférer des secrets montés en fichiers pour les données très sensibles.

## Bonnes pratiques

```bash
# ❌ Ne jamais coder en dur
export DB_PASSWORD="mysecret"

# ✓ Charger depuis un fichier externe
export DB_PASSWORD=$(cat /run/secrets/db_password)

# ✓ Utiliser un gestionnaire de secrets
export DB_PASSWORD=$(vault kv get -field=password secret/db)
```

## GitHub Actions secrets

```yaml
jobs:
  deploy:
    steps:
      - name: Deploy
        env:
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
          API_KEY: ${{ secrets.API_KEY }}
        run: ./deploy.sh
```

## Kubernetes : injection depuis Secret

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-creds
        key: password
```

## Liens

- [[Secrets management]]
- [[Secret rotation]]
- [[Vault]]
