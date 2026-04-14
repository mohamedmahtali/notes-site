---
title: Containers
tags:
  - beginner
---

# Containers

## Parent
- [[Docker]]

## Enfants
- [[Container lifecycle]]
- [[Container logs]]
- [[Exec into container]]
- [[Resource limits]]

---

## Définition

Un conteneur est une instance en cours d'exécution d'une image Docker. C'est un processus isolé sur le système hôte, avec son propre filesystem (via l'image), son propre namespace réseau, et ses propres processus — mais partageant le kernel de l'hôte.

---

## Image vs Conteneur

```
Image = recette (immuable, stockée)
Conteneur = instance de cette recette (éphémère, en cours d'exécution)

Un même image → plusieurs conteneurs simultanés
docker run nginx   # conteneur 1
docker run nginx   # conteneur 2 (identique, indépendant)
```

---

## Commandes essentielles

```bash
# Lancer un conteneur
docker run -d --name mon-app -p 8080:80 nginx

# Lister les conteneurs actifs
docker ps

# Lister tous les conteneurs (y compris arrêtés)
docker ps -a

# Stopper un conteneur
docker stop mon-app

# Démarrer un conteneur arrêté
docker start mon-app

# Supprimer un conteneur
docker rm mon-app

# Forcer l'arrêt + suppression
docker rm -f mon-app

# Voir les logs
docker logs mon-app
docker logs -f mon-app   # suivi en temps réel

# Entrer dans un conteneur
docker exec -it mon-app bash
```

---

## Nettoyage

```bash
# Supprimer tous les conteneurs arrêtés
docker container prune

# Nettoyage complet (conteneurs, images, volumes, réseaux orphelins)
docker system prune -a
```
