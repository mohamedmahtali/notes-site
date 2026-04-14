---
title: start
tags:
  - beginner
---

# start

## Parent
- [[Container lifecycle]]

---

## Définition

`docker start` démarre un conteneur existant qui est dans l'état `created` ou `stopped`. Contrairement à `docker run`, il ne crée pas un nouveau conteneur — il réutilise un conteneur déjà créé.

---

## Commandes

```bash
# Démarrer un conteneur arrêté
docker start mon-app

# Démarrer en mode interactif (avec terminal)
docker start -ai mon-app

# Démarrer plusieurs conteneurs
docker start app1 app2 app3
```

---

## run vs start

| Commande | Comportement |
|---|---|
| `docker run` | Crée ET démarre un nouveau conteneur |
| `docker start` | Démarre un conteneur **existant** |

```bash
# Après docker stop, les données du conteneur sont préservées
docker stop mon-app
docker start mon-app   # redémarre avec le même état filesystem
```
