---
title: ADD
tags:
  - intermediate
---

# ADD

---

## Définition

`ADD` fait tout ce que fait `COPY` plus deux fonctionnalités supplémentaires : l'extraction automatique d'archives `.tar` et le téléchargement depuis des URLs. Dans la plupart des cas, `COPY` est préférable car plus explicite.

---

## Syntaxe

```dockerfile
ADD <src> <dest>

# Copie simple (préférer COPY)
ADD README.md /app/

# Extraction automatique d'archive
ADD source.tar.gz /app/     # extrait dans /app/

# Depuis une URL (déconseillé)
ADD https://example.com/file.tar.gz /tmp/
```

---

## Quand utiliser ADD

```dockerfile
# Cas valide : extraire une archive lors du build
ADD app-v1.2.tar.gz /opt/app/

# Tout le reste → utiliser COPY
COPY . .
```

---

## Pourquoi éviter ADD pour les URLs

> [!warning]
> `ADD https://...` ne peut pas être mis en cache correctement par [[Docker]] — le conteneur doit refaire le téléchargement à chaque build invalidé. Préférer :
> ```[[Dockerfile]]
> RUN curl -fsSL https://example.com/file.tar.gz | tar -xz -C /opt/
> ```
