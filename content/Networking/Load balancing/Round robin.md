---
title: Round robin
tags:
  - networking
  - beginner
---

# Round robin

## Définition

Le round-robin est l'algorithme de load balancing le plus simple : chaque nouvelle requête est envoyée au serveur suivant dans la liste de façon circulaire.

> [!note] Limitation
> Le round-robin ne tient pas compte de la charge réelle de chaque serveur. Si un serveur est lent, il continuera de recevoir des requêtes. Utiliser `leastconn` pour les connexions longues.

## Configuration Nginx

```nginx
upstream backend {
    server app1:8080;    # Poids 1 (défaut)
    server app2:8080;    # Poids 1
    server app3:8080 weight=3;  # 3x plus de trafic
}
```

## Flux de distribution

```
Requête 1 → app1
Requête 2 → app2
Requête 3 → app3
Requête 4 → app1
Requête 5 → app2
...
```

## Avec poids (weighted round robin)

```nginx
upstream backend {
    server powerful-server:8080 weight=5;  # 5/7 du trafic
    server small-server:8080 weight=2;     # 2/7 du trafic
}
```

## Liens

- [[Load balancing]]
- [[Least connections]]
- [[Nginx]]
- [[HAProxy]]
