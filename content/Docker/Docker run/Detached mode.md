---
title: Detached mode
tags:
  - beginner
---

# Detached mode

---

## Définition

Le mode détaché (`-d` / `--detach`) lance le conteneur en arrière-plan et retourne immédiatement à la ligne de commande. C'est le mode standard pour les [[Services]] (web servers, bases de données, etc.).

---

## Commandes

```bash
# Mode détaché
docker run -d --name mon-api mon-app

# Mode interactif (oppose du detach)
docker run -it --name debug ubuntu bash
# → reste attaché au terminal

# Attacher un terminal à un conteneur détaché
docker attach mon-api

# Sortir sans stopper (Ctrl+P puis Ctrl+Q)
```

---

## Vérifier qu'un conteneur tourne

```bash
docker ps
# CONTAINER ID  IMAGE    STATUS        NAMES
# abc123        mon-app  Up 2 minutes  mon-api

docker logs mon-api
docker logs -f mon-api   # suivi
```

---

## -d vs --rm

| Option | Comportement |
|---|---|
| `-d` | Arrière-plan, conteneur persiste après arrêt |
| `--rm` | Suppression automatique à l'arrêt |
| `-d --rm` | Arrière-plan + suppression automatique |

```bash
# Tâche ponctuelle en arrière-plan, auto-nettoyée
docker run -d --rm --name backup mon-backup-task
```
