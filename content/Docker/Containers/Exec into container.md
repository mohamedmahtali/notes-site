---
title: Exec into container
tags:
  - beginner
---

# Exec into container

---

## Définition

`docker exec` exécute une commande dans un conteneur **en cours d'exécution**. C'est l'outil de débogage principal pour inspecter l'état d'un conteneur sans le redémarrer.

---

## Commandes

```bash
# Ouvrir un shell interactif
docker exec -it mon-app bash
docker exec -it mon-app sh    # si bash non disponible (alpine)

# Exécuter une commande simple
docker exec mon-app ls /app
docker exec mon-app env
docker exec mon-app cat /etc/nginx/nginx.conf

# Avec un utilisateur spécifique
docker exec -it --user root mon-app bash

# Avec des variables d'environnement
docker exec -e DEBUG=true mon-app ./run.sh
```

---

## Déboguer une image sans shell

```bash
# Copier un fichier dans/depuis un conteneur
docker cp mon-app:/app/logs/error.log ./error.log
docker cp ./config.json mon-app:/app/config.json

# Inspecter le filesystem
docker exec mon-app find /app -name "*.log"

# Processus actifs dans le conteneur
docker exec mon-app ps aux

# Utilisation mémoire
docker stats mon-app
```

---

> [!note]
> `docker exec` n'est disponible que sur des conteneurs en état `running`. Pour inspecter un conteneur arrêté, utiliser `docker cp` ou relancer avec un entrypoint personnalisé.
