---
title: Secrets handling
tags:
  - intermediate
---

# Secrets handling

---

## Définition

La gestion des [[Secrets]] dans [[Docker]] concerne l'injection de données sensibles (passwords, [[Tokens]], clés API) dans les conteneurs sans les exposer dans les images, les [[Variables]] d'environnement visibles, ou les logs.

---

## Mauvaises pratiques

```dockerfile
# ❌ Dans le Dockerfile
ENV DB_PASSWORD=secret123

# ❌ ARG n'est pas plus sûr (visible dans docker history)
ARG DB_PASSWORD=secret123
```

---

## Bonnes pratiques

### 1. Variables d'environnement au runtime

```bash
# Pas dans l'image, injecté au lancement
docker run -e DB_PASSWORD=$(vault kv get -field=password secret/db) mon-app
```

### 2. Docker Secrets (Swarm)

```bash
# Créer un secret
echo "secret123" | docker secret create db_password -

# Utiliser dans un service
docker service create   --secret db_password   mon-app
# → disponible dans /run/secrets/db_password
```

### 3. Build secrets (pas dans les layers)

```dockerfile
# Installer une dépendance privée sans exposer le token
RUN --mount=type=secret,id=npm_token     NPM_TOKEN=$(cat /run/secrets/npm_token) npm install
```

```bash
docker buildx build --secret id=npm_token,env=NPM_TOKEN .
```

---

> [!tip]
> En production, utiliser un gestionnaire de secrets externe : HashiCorp [[Vault]], [[AWS]] Secrets Manager, GCP Secret Manager. L'injection au démarrage du conteneur depuis ces systèmes est la meilleure approche.
