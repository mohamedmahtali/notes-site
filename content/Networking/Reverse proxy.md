---
title: Reverse proxy
tags: [networking, intermediate]
---

# Reverse proxy

## Définition

Un reverse proxy est un serveur intermédiaire qui reçoit les requêtes des clients et les transmet aux serveurs backend. Contrairement au proxy forward (qui protège les clients), le reverse proxy protège et optimise les serveurs.

> [!tip] Pourquoi c'est important
> Le reverse proxy est un composant fondamental de toute architecture web : terminaison TLS, load balancing, cache, compression, rate limiting, et routage par path ou host — le tout en un seul point d'entrée.

## Fonctions principales

```
Client → [Reverse Proxy] → Backend servers
                │
                ├── Terminaison TLS (HTTPS)
                ├── Load balancing
                ├── Cache statique
                ├── Compression gzip/brotli
                ├── Rate limiting
                └── Routage (path / host based)
```

## Configurations Nginx essentielles

```nginx
# Reverse proxy simple vers un backend
server {
    listen 80;
    server_name myapp.example.com;

    location / {
        proxy_pass http://backend:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```nginx
# Routage par path — plusieurs services derrière un même domaine
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate     /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    location /api/users {
        proxy_pass http://users-service:8001;
    }

    location /api/orders {
        proxy_pass http://orders-service:8002;
    }

    location /static/ {
        root /var/www;
        expires 30d;
    }
}
```

```nginx
# Terminaison TLS + redirection HTTP → HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}
```

## Traefik — auto-découverte Docker

```yaml
# docker-compose.yml
services:
  traefik:
    image: traefik:v3
    command:
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.letsencrypt.acme.email=admin@example.com"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

  myapp:
    image: myapp:latest
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.myapp.rule=Host(`myapp.example.com`)"
      - "traefik.http.routers.myapp.tls.certresolver=letsencrypt"
```

> [!tip] Traefik vs Nginx
> Traefik reconfigure automatiquement ses routes quand des conteneurs démarrent ou s'arrêtent. Nginx nécessite un rechargement manuel (`nginx -s reload`) ou un outil comme nginx-proxy.

## Outils

- **[[Nginx]]** — Le plus utilisé, performant, configuration simple
- **[[HAProxy]]** — Spécialisé load balancing, haute disponibilité
- **[[Traefik]]** — Cloud-native, auto-découverte Docker/K8s

## Liens

- [[Nginx]]
- [[HAProxy]]
- [[Traefik]]
- [[Load balancing]]
- [[TLS]]
- [[Networking]]
