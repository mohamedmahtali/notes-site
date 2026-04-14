---
title: Docker networks
tags:
  - intermediate
---

# Docker networks

## Parent
- [[Docker]]

## Enfants
- [[Bridge]]
- [[Host]]
- [[Overlay]]
- [[DNS in Docker]]

---

## Définition

Docker crée des réseaux virtuels isolés pour permettre la communication entre conteneurs. Chaque réseau a son propre espace d'adressage IP. Par défaut, les conteneurs sur le même réseau peuvent se contacter par nom (DNS automatique).

---

## Types de réseaux

| Driver | Description |
|---|---|
| [[Bridge]] | Réseau isolé sur le host (défaut) |
| [[Host]] | Partage le réseau de l'hôte |
| [[Overlay]] | Multi-hosts (Docker Swarm) |
| `none` | Aucun réseau |
| `macvlan` | IP directe sur le réseau physique |

---

## Commandes essentielles

```bash
# Lister les réseaux
docker network ls

# Créer un réseau
docker network create mon-reseau

# Lancer un conteneur sur un réseau
docker run -d --network mon-reseau --name api mon-app

# Connecter un conteneur existant à un réseau
docker network connect mon-reseau mon-conteneur

# Inspecter un réseau
docker network inspect mon-reseau

# Supprimer un réseau
docker network rm mon-reseau
docker network prune   # supprimer les réseaux non utilisés
```

---

## Exemple – API + Base de données

```bash
docker network create backend-net

docker run -d --name postgres --network backend-net postgres:16
docker run -d --name api --network backend-net mon-app
# → api peut contacter postgres par le nom "postgres"
```
