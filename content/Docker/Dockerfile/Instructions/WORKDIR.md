---
title: WORKDIR
tags:
  - beginner
---

# WORKDIR

---

## Définition

`WORKDIR` définit le répertoire de travail courant pour les [[Instructions]] `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, et `ADD` qui suivent dans le [[Dockerfile]]. Il crée le répertoire s'il n'existe pas.

---

## Syntaxe

```dockerfile
WORKDIR /app

# Relatif au WORKDIR précédent
WORKDIR /app
WORKDIR src    # → /app/src
```

---

## Bonnes pratiques

```dockerfile
# ✅ Utiliser un chemin absolu clair
WORKDIR /app

# ❌ Éviter de faire avec RUN
RUN mkdir /app && cd /app
# (cd n'est pas persisté entre les RUN)
```

---

## Exemple

```dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

# CMD s'exécute depuis /app
CMD ["node", "index.js"]
```

---

> [!tip]
> Toujours utiliser `/app` comme convention pour les applications. C'est un standard de facto dans les images [[Docker]].
