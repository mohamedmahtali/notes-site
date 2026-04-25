---
title: Least connections
tags:
  - networking
  - intermediate
---

# Least connections

## Définition

L'algorithme "least connections" envoie chaque nouvelle requête au serveur qui a le moins de connexions actives à l'instant T. C'est plus intelligent que le round-robin pour les connexions de durée variable.

> [!tip] Quand l'utiliser
> Idéal pour les applications avec des requêtes de durée très variable (streaming, WebSockets, uploads). Le round-robin serait injuste si certaines requêtes durent 1ms et d'autres 30s.

## Configuration

```nginx
# Nginx
upstream backend {
    least_conn;              # Activer least_conn
    server app1:8080;
    server app2:8080;
    server app3:8080;
}
```

```
# HAProxy
backend app_servers
    balance leastconn
    server app1 10.0.1.10:8080 check
    server app2 10.0.1.11:8080 check
```

## Comparaison des algorithmes

| Algo | Idéal pour |
|------|-----------|
| Round robin | Requêtes courtes et uniformes |
| Least conn | Durées [[Variables]] (WebSockets, API) |
| IP hash | Sessions sticky (sans cookie de session) |
| Random | Simplicité + bonne distribution statistique |

## Liens

- [[Load balancing]]
- [[Round robin]]
- [[HAProxy]]
