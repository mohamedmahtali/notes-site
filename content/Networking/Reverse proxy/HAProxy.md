---
title: HAProxy
tags: [networking, advanced]
---

# HAProxy

## Définition

HAProxy (High Availability Proxy) est un load balancer et proxy TCP/HTTP open-source, réputé pour ses performances extrêmes et sa fiabilité. Il est utilisé par des géants du web (GitHub, Stack Overflow, Reddit).

> [!note] HAProxy vs Nginx
> HAProxy excelle dans le load balancing pur (Layer 4 et 7), les health checks avancés, et les statistiques en temps réel. Nginx est plus polyvalent (fichiers statiques, PHP). Les deux se complètent souvent.

## Configuration de base

```
# /etc/haproxy/haproxy.cfg
global
    maxconn 50000
    log stdout format raw local0

defaults
    mode http
    timeout connect 5s
    timeout client  50s
    timeout server  50s
    log global

frontend web
    bind *:80
    bind *:443 ssl crt /etc/ssl/certs/combined.pem
    redirect scheme https if !{ ssl_fc }
    default_backend app_servers

backend app_servers
    balance roundrobin
    option httpchk GET /health HTTP/1.1
Host:\ localhost
    server app1 10.0.1.10:8080 check
    server app2 10.0.1.11:8080 check
    server app3 10.0.1.12:8080 check backup

# Stats
frontend stats
    bind *:8404
    stats enable
    stats uri /stats
    stats refresh 10s
```

## Algorithmes de load balancing

| Algo | Description |
|------|-------------|
| `roundrobin` | Tour à tour (défaut) |
| `leastconn` | Serveur avec moins de connexions |
| `source` | IP source → même serveur (sticky) |
| `random` | Aléatoire |
| `first` | Premier serveur disponible |

## Liens

- [[Reverse proxy]]
- [[Load balancing]]
- [[Networking]]
