---
title: Port mapping
tags:
  - beginner
---

# Port mapping

---

## Définition

Le port mapping (`-p`) crée une règle [[iptables]] qui redirige le trafic d'un port de l'hôte vers un port du conteneur. Sans mapping, le conteneur est isolé réseau et inaccessible depuis l'extérieur.

---

## Syntaxe

```bash
-p [IP_HÔTE:]PORT_HÔTE:PORT_CONTENEUR[/PROTOCOLE]

# Exemples
-p 8080:80              # hôte:8080 → conteneur:80
-p 80:80                # même port
-p 127.0.0.1:8080:80   # seulement sur localhost
-p 8080:80/udp          # UDP
-p 80:80 -p 443:443     # plusieurs ports
```

---

## Commandes

```bash
# Mapping simple
docker run -d -p 8080:80 nginx

# Publier tous les ports EXPOSE
docker run -d -P nginx
# → ports aléatoires sur l'hôte

# Voir les mappings
docker port mon-app
# 80/tcp -> 0.0.0.0:8080
```

---

## Schéma

```
Hôte (port 8080) ──→ iptables ──→ Conteneur (port 80)
   curl localhost:8080           nginx écoute sur :80
```

---

> [!tip]
> En développement, utiliser des [[Ports]] différents par service :
> - API → 8080
> - Frontend → 3000
> - DB → 5432 (ne pas exposer en production !)
