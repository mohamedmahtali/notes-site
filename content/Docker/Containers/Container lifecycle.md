---
title: Container lifecycle
tags:
  - beginner
---

# Container lifecycle

---

## Définition

Le cycle de vie d'un conteneur [[Docker]] suit des états bien définis : created, running, paused, stopped, removed. Comprendre ces transitions permet de gérer correctement les conteneurs.

---

## États et transitions

```
                    docker start
        created ─────────────────→ running
           ↑                          │
docker create                    docker stop / docker kill
           │                          │
           └──── removed ←─────── stopped
                docker rm         docker start ↔ stopped
```

| État | Description |
|---|---|
| `created` | Créé mais pas démarré (`docker create`) |
| `running` | En cours d'exécution |
| `paused` | Processus suspendu (`docker pause`) |
| `stopped` (exited) | Processus terminé |
| `removed` | Supprimé définitivement |

---

## Commandes

```bash
docker create --name app nginx    # créer sans démarrer
docker start app                  # démarrer
docker pause app                  # suspendre
docker unpause app                # reprendre
docker stop app                   # arrêt propre (SIGTERM)
docker kill app                   # arrêt forcé (SIGKILL)
docker restart app                # stop + start
docker rm app                     # supprimer (doit être stopped)
docker rm -f app                  # forcer la suppression
```
