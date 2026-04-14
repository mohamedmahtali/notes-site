---
title: Environment variables
tags:
  - beginner
---

# Environment variables

## Parent
- [[Docker run]]

---

## Définition

Les variables d'environnement permettent de configurer le comportement d'un conteneur au lancement sans modifier l'image. C'est le mécanisme standard pour injecter de la configuration (URLs, ports, mode de l'app) et des secrets (tokens, passwords).

---

## Commandes

```bash
# Une variable
docker run -e NODE_ENV=production mon-app

# Plusieurs variables
docker run   -e NODE_ENV=production   -e PORT=3000   -e DB_HOST=postgres   mon-app

# Depuis l'environnement hôte
export API_KEY=mon-secret
docker run -e API_KEY mon-app    # passe la valeur de $API_KEY

# Depuis un fichier .env
docker run --env-file .env mon-app
```

---

## Fichier .env

```bash
# .env
NODE_ENV=production
PORT=3000
DB_HOST=postgres
DB_USER=app
DB_PASSWORD=secret
```

---

## Inspecter les variables d'un conteneur

```bash
docker exec mon-app env
docker inspect mon-app | grep -A20 '"Env"'
```

---

> [!warning] Sécurité
> Les variables d'environnement sont visibles via `docker inspect`. Pour les secrets sensibles, utiliser Docker Secrets (Swarm) ou un outil externe (Vault, AWS Secrets Manager).
