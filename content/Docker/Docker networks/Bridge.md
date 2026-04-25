---
title: Bridge
tags:
  - intermediate
---

# Bridge

---

## Définition

Le driver `bridge` crée un réseau privé virtuel sur l'hôte [[Docker]]. C'est le driver par défaut. Les conteneurs sur le même réseau bridge peuvent se contacter. La communication avec l'extérieur passe par [[NAT]].

---

## Bridge par défaut vs custom bridge

| Critère | Bridge par défaut (`docker0`) | Custom bridge |
|---|---|---|
| [[DNS]] automatique | ❌ Non | ✅ Oui |
| Isolation | Partagé avec tous les conteneurs | Réseau dédié |
| Recommandé | ❌ Non | ✅ Oui |

---

## Créer et utiliser un custom bridge

```bash
# Créer un réseau bridge custom
docker network create --driver bridge app-net

# Lancer des conteneurs sur ce réseau
docker run -d --name api --network app-net mon-api
docker run -d --name db  --network app-net postgres:16

# api peut contacter db par son nom
docker exec api ping db   # → résolution DNS automatique
```

---

## En Docker Compose

[[Docker compose]] crée automatiquement un réseau bridge custom pour chaque projet :

```yaml
services:
  api:
    image: mon-api
  db:
    image: postgres:16
# → api peut contacter db via "db" (nom du service)
```

---

> [!tip]
> Toujours utiliser des **custom bridge [[Networks]]** plutôt que le bridge par défaut. Le bridge par défaut n'a pas de DNS automatique et met tous les conteneurs sur le même réseau.
