---
title: Load balancing
tags: [networking, intermediate]
---

# Load balancing

## Définition

Le load balancing (équilibrage de charge) distribue le trafic réseau entrant sur plusieurs serveurs backend pour éviter la surcharge d'un serveur unique, améliorer la disponibilité et augmenter la scalabilité.

> [!tip] Pourquoi c'est important
> Sans load balancer, un seul serveur devient un SPOF (Single Point of Failure). Avec load balancing, on peut scaler horizontalement et maintenir la disponibilité même si un serveur tombe.

## Layer 4 vs Layer 7

| | L4 (Transport) | L7 (Application) |
|--|---------------|-----------------|
| Niveau | TCP/UDP | HTTP/HTTPS |
| Routing basé sur | IP + Port | URL, headers, cookies |
| Vitesse | Très rapide | Plus lent (parse HTTP) |
| Flexibilité | Faible | Élevée |
| Exemple | HAProxy TCP, AWS NLB | Nginx, Traefik, AWS ALB |

## Health checks

Le load balancer vérifie régulièrement que chaque backend est vivant. Un backend qui échoue est retiré du pool automatiquement.

```nginx
# Nginx — upstream avec health check passif
upstream backend {
    server app1:8080;
    server app2:8080;
    server app3:8080 backup;  # Utilisé seulement si les autres tombent
}
```

```
# HAProxy — health check actif (HTTP)
backend web_servers
    balance roundrobin
    option httpchk GET /health
    http-check expect status 200
    server app1 10.0.0.1:8080 check inter 5s fall 3 rise 2
    server app2 10.0.0.2:8080 check inter 5s fall 3 rise 2
```

> [!note] fall et rise
> `fall 3` : 3 échecs consécutifs avant de marquer DOWN. `rise 2` : 2 succès avant de remarquer UP. Évite les flapping (oscilations rapides).

## Sticky sessions (Session persistence)

Par défaut le load balancer ne garantit pas qu'un client revient toujours sur le même serveur. Les sticky sessions forcent cette affinité.

| Méthode | Mécanisme | Usage |
|---------|-----------|-------|
| Cookie-based | Le LB insère un cookie `SERVERID` | Applis avec session HTTP |
| IP hash | Hash de l'IP source → serveur fixe | APIs stateless, simple |
| Consistent hashing | Redistribution minimale si serveur ajouté | Cache distribué |

```nginx
# Nginx — sticky sessions par IP hash
upstream backend {
    ip_hash;
    server app1:8080;
    server app2:8080;
}
```

> [!warning] Sticky sessions ≠ HA
> Si le serveur cible tombe, la session est perdue. Préférer un stockage de session externe (Redis) plutôt que de compter sur la persistence.

## Algorithmes de distribution

| Algorithme | Principe | Quand l'utiliser |
|------------|---------|-----------------|
| Round Robin | Tour à tour | Serveurs homogènes, requêtes similaires |
| Weighted Round Robin | Tour à tour avec poids | Serveurs de capacités différentes |
| Least Connections | Serveur avec le moins de connexions actives | Requêtes de durées variables |
| Random | Aléatoire | Simple, performant sous haute charge |
| IP Hash | Hash IP source | Affinité client, cache L7 |

## Liens

- [[Round robin]]
- [[Least connections]]
- [[Reverse proxy]]
- [[Nginx]]
- [[HAProxy]]
- [[Networking]]
