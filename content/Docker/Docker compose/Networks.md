---
title: Networks
tags:
  - intermediate
---

# Networks

## Parent
- [[Docker compose]]

---

## Définition

Docker Compose crée automatiquement un réseau bridge par défaut pour tous les services du fichier. Les services peuvent se contacter par leur nom de service. On peut définir des réseaux supplémentaires pour isoler les services.

---

## Réseau par défaut

```yaml
# Sans configuration réseau explicite
services:
  api:
    image: mon-app
  db:
    image: postgres:16
# → api peut contacter db via hostname "db"
```

---

## Réseaux custom

```yaml
services:
  frontend:
    image: nginx
    networks:
      - frontend-net
      - backend-net

  api:
    image: mon-api
    networks:
      - backend-net

  db:
    image: postgres:16
    networks:
      - backend-net
    # db n'est pas accessible depuis frontend-net

networks:
  frontend-net:
    driver: bridge
  backend-net:
    driver: bridge
    internal: true   # pas d'accès internet
```

---

## Rejoindre un réseau externe

```yaml
networks:
  shared-net:
    external: true    # réseau déjà créé par docker network create
    name: mon-reseau-existant
```
