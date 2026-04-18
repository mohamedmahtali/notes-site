---
title: Nginx (reverse proxy)
tags: [networking, intermediate]
---

# Nginx (Reverse Proxy)

## Définition

Nginx est un serveur web et reverse proxy haute performance. Il est utilisé comme reverse proxy devant des applications Node.js, Python, Java pour gérer TLS, la compression, le cache et le load balancing.

> [!tip] Nginx vs Apache
> Nginx utilise une architecture event-driven asynchrone (un thread gère des milliers de connexions). Apache utilise un thread par connexion. Nginx est plus performant pour les charges élevées.

## Configuration de base

```nginx
# /etc/nginx/nginx.conf ou /etc/nginx/sites-available/myapp

upstream backend {
    server app1:8080;
    server app2:8080;
    keepalive 32;
}

server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/cert.pem;
    ssl_certificate_key /etc/ssl/private/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    gzip on;
    gzip_types text/plain application/json;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        root /var/www;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

## Commandes

```bash
nginx -t                    # Tester la configuration
nginx -s reload             # Recharger sans coupure
systemctl restart nginx
nginx -T                    # Afficher la config complète
```

## Liens

- [[Reverse proxy]]
- [[Load balancing]]
- [[TLS]]
- [[Networking]]
