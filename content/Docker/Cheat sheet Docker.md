---
title: Cheat sheet Docker
tags:
  - docker
  - beginner
---

# Cheat sheet Docker

## Images

```bash
docker images                          # Lister les images locales
docker pull nginx:latest               # Télécharger une image
docker build -t myapp:1.0 .            # Construire depuis Dockerfile
docker build --no-cache -t myapp .     # Sans cache
docker rmi myapp:1.0                   # Supprimer une image
docker image prune                     # Supprimer les images non utilisées
docker tag myapp:1.0 registry/myapp:1.0  # Renommer/tagger
docker push registry/myapp:1.0         # Push vers un registry
docker save myapp > myapp.tar          # Exporter en fichier
docker load < myapp.tar                # Importer depuis fichier
```

## Conteneurs

```bash
docker run -d --name web nginx         # Lancer en arrière-plan
docker run -it ubuntu bash             # Interactif avec shell
docker run -p 8080:80 nginx            # Mapper port host:container
docker run -v /data:/app/data nginx    # Monter un volume
docker run --rm nginx                  # Supprimer après arrêt
docker run -e VAR=value nginx          # Variable d'environnement
docker ps                              # Conteneurs en cours
docker ps -a                           # Tous les conteneurs
docker stop web                        # Arrêter
docker start web                       # Démarrer
docker restart web                     # Redémarrer
docker rm web                          # Supprimer
docker rm -f web                       # Forcer la suppression
```

## Inspection & debug

```bash
docker logs web                        # Voir les logs
docker logs -f web                     # Suivre les logs
docker logs --tail 100 web             # 100 dernières lignes
docker exec -it web bash               # Shell dans le conteneur
docker exec web ls /etc/nginx          # Commande dans le conteneur
docker inspect web                     # Infos JSON complètes
docker stats                           # Utilisation CPU/RAM temps réel
docker top web                         # Processus dans le conteneur
docker diff web                        # Fichiers modifiés
```

## Volumes

```bash
docker volume create mydata            # Créer un volume
docker volume ls                       # Lister les volumes
docker volume inspect mydata           # Détails
docker volume rm mydata                # Supprimer
docker volume prune                    # Supprimer les non utilisés
docker run -v mydata:/app/data nginx   # Utiliser un volume nommé
```

## Réseaux

```bash
docker network create mynet            # Créer un réseau
docker network ls                      # Lister les réseaux
docker network inspect mynet           # Détails
docker run --network mynet nginx       # Utiliser un réseau
docker network connect mynet web       # Connecter un conteneur
docker network disconnect mynet web    # Déconnecter
```

## Docker Compose

```bash
docker compose up -d                   # Démarrer (détaché)
docker compose up --build              # Reconstruire avant de démarrer
docker compose down                    # Arrêter et supprimer
docker compose down -v                 # + supprimer les volumes
docker compose ps                      # Statut des services
docker compose logs -f                 # Suivre les logs
docker compose exec web bash           # Shell dans un service
docker compose pull                    # Mettre à jour les images
docker compose restart web             # Redémarrer un service
```

## Nettoyage

```bash
docker system prune                    # Tout supprimer (non utilisé)
docker system prune -a                 # + images non taguées
docker system df                       # Espace utilisé par Docker
docker container prune                 # Conteneurs arrêtés
docker image prune -a                  # Images non utilisées
```

## Liens

- [[Docker]]
- [[Dockerfile]]
- [[Containers]]
- [[Docker volumes]]
- [[Docker networks]]
