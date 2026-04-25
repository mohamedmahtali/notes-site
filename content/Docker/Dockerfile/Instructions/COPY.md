---
title: COPY
tags:
  - beginner
---

# COPY

---

## Définition

`COPY` copie des fichiers ou dossiers depuis le **contexte de build** (ton machine locale) vers le filesystem du conteneur. C'est la méthode recommandée pour ajouter du code dans une image.

---

## Syntaxe

```dockerfile
COPY <src> <dest>
COPY <src1> <src2> <dest/>

# Exemples
COPY package.json ./
COPY . .
COPY src/ /app/src/
COPY --chown=appuser:appuser . .

# Multi-stage : copier depuis une autre étape
COPY --from=builder /app/dist ./dist
```

---

## Pattern classique Node.js

```dockerfile
WORKDIR /app

# Copier les fichiers de dépendances AVANT le code source
COPY package.json package-lock.json ./
RUN npm ci

# Copier le code source ensuite
COPY . .
```

> [!tip] Pourquoi copier [[Package]].json en premier ?
> Si tu copies tout avec `COPY . .` d'un coup, chaque changement de code source invalide le cache du `npm ci` — même si `package.json` n'a pas changé. En séparant, le layer `npm ci` est mis en cache tant que `package.json` ne change pas.

---

## COPY vs ADD

| Instruction | Fonctionnalité | Recommandation |
|---|---|---|
| `COPY` | Copie simple | ✅ Préférer toujours |
| `ADD` | Copie + extraction archives + URL | Utiliser seulement pour les archives |
