---
title: remove
tags:
  - beginner
---

# remove

## Parent
- [[Container lifecycle]]

---

## Définition

`docker rm` supprime un ou plusieurs conteneurs arrêtés. Les données dans le filesystem du conteneur (hors volumes) sont perdues définitivement. Un conteneur en cours d'exécution doit d'abord être stoppé (ou `rm -f` pour forcer).

---

## Commandes

```bash
# Supprimer un conteneur arrêté
docker rm mon-app

# Forcer la suppression (stop + remove)
docker rm -f mon-app

# Supprimer avec les volumes anonymes associés
docker rm -v mon-app

# Supprimer tous les conteneurs arrêtés
docker container prune

# Supprimer les conteneurs qui matchent un filtre
docker rm $(docker ps -aq --filter status=exited)
```

---

## Lancer et auto-supprimer

```bash
# --rm supprime le conteneur automatiquement à l'arrêt
docker run --rm -it ubuntu bash
# → à la sortie du shell, le conteneur est supprimé
```

> [!tip]
> Pour les tests et commandes one-shot, `--rm` est indispensable pour éviter l'accumulation de conteneurs arrêtés.
