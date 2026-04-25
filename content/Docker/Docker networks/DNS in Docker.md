---
title: DNS in Docker
tags:
  - intermediate
---

# DNS in Docker

---

## Définition

[[Docker]] embarque un serveur [[DNS]] interne (127.0.0.11) qui résout automatiquement les noms des conteneurs et [[Services]]. Sur les custom [[Bridge]] [[Networks]] et les réseaux [[Overlay]], les conteneurs peuvent se contacter par leur **nom de conteneur** ou leur **nom de service** [[Docker compose]].

---

## Résolution automatique

```bash
# Réseau custom bridge
docker network create app-net
docker run -d --name postgres --network app-net postgres:16
docker run -d --name api --network app-net mon-app

# Dans le conteneur api, postgres est résolvable par son nom
docker exec api ping postgres
# → PING postgres (172.18.0.2): 56 data bytes

# En Node.js
const pg = new Pool({ host: 'postgres', port: 5432 })

# En Python
conn = psycopg2.connect(host='postgres', port=5432)
```

---

## Avec Docker Compose

```yaml
services:
  api:
    image: mon-app
    environment:
      - DB_HOST=postgres     # nom du service = hostname DNS
  postgres:
    image: postgres:16
```

---

## Serveur DNS interne

```bash
# Voir le DNS configuré dans un conteneur
docker exec mon-app cat /etc/resolv.conf
# nameserver 127.0.0.11   ← DNS Docker
# options ndots:0
```

---

> [!warning] Bridge par défaut
> Sur le bridge par défaut (`docker0`), la résolution DNS par nom **ne fonctionne pas**. Toujours utiliser des custom networks ou Docker Compose.
