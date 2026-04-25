---
title: stop
tags:
  - beginner
---

# stop

---

## Définition

`docker stop` envoie un signal `SIGTERM` au processus principal du conteneur pour lui permettre de s'arrêter proprement. Si le processus ne s'arrête pas dans le délai imparti (10s par défaut), [[Docker]] envoie `SIGKILL`.

---

## Commandes

```bash
# Arrêt propre (SIGTERM → attendre 10s → SIGKILL si nécessaire)
docker stop mon-app

# Réduire le timeout (ex: 5 secondes)
docker stop --time 5 mon-app

# Arrêt immédiat brutal (SIGKILL)
docker kill mon-app

# Arrêter tous les conteneurs actifs
docker stop $(docker ps -q)
```

---

## stop vs kill

| Commande | Signal | Arrêt propre |
|---|---|---|
| `docker stop` | [[SIGTERM]] → [[SIGKILL]] | ✅ Oui (si le process le gère) |
| `docker kill` | SIGKILL direct | ❌ Non |

> [!tip]
> Préférer `docker stop` pour permettre à l'application de fermer ses connexions, vider ses buffers, et écrire ses logs avant de s'arrêter.
