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

## Liens

- [[Tokens]]
- [[Policies]]
- [[Secret engines]]
- [[Dynamic secrets]]
- [[Secrets management]]
