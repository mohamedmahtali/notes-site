---
title: RUN
tags:
  - beginner
---

# RUN

## Parent
- [[Instructions]]

---

## Définition

`RUN` exécute une commande lors du **build** de l'image et crée un nouveau layer avec le résultat. C'est l'instruction pour installer des dépendances, compiler du code, configurer l'environnement.

---

## Syntaxe

```dockerfile
# Shell form (passe par /bin/sh -c)
RUN apt-get update && apt-get install -y curl

# Exec form (plus prévisible, sans shell)
RUN ["apt-get", "install", "-y", "curl"]
```

---

## Bonnes pratiques

```dockerfile
# ✅ Combiner en une seule commande = 1 seul layer
RUN apt-get update &&     apt-get install -y --no-install-recommends         curl         git         vim &&     rm -rf /var/lib/apt/lists/*

# ❌ Plusieurs RUN séparés = plusieurs layers inutiles
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
```

---

## Nettoyer le cache dans le même layer

```dockerfile
# Toujours nettoyer dans la même instruction RUN
RUN pip install -r requirements.txt &&     rm -rf /root/.cache/pip

RUN npm ci &&     npm cache clean --force
```

> [!warning]
> Si tu nettoies dans un RUN séparé, les fichiers du cache existent toujours dans le layer précédent — l'image n'est pas plus petite.
