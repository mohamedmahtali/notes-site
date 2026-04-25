---
title: Traefik
tags:
  - networking
  - intermediate
---

# Traefik

## Définition

Traefik est un reverse proxy et load balancer [[Cloud]]-native qui se configure automatiquement en découvrant les [[Services]] via [[Docker]] labels, [[Kubernetes]] [[Ingress]]/[[CRD]], ou Consul. Il gère automatiquement les certificats Let's Encrypt.

> [!tip] Avantage clé
> Avec Traefik, zéro configuration manuelle des routes : il détecte les conteneurs Docker ou [[Pods]] Kubernetes et configure les routes automatiquement via des annotations ou labels.

## Avec Docker Compose

```yaml
# docker-compose.yml
services:
  traefik:
    image: traefik:v3.0
    command:
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.le.acme.email=admin@example.com"
      - "--certificatesresolvers.le.acme.storage=/acme.json"
      - "--certificatesresolvers.le.acme.tlschallenge=true"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./acme.json:/acme.json

  myapp:
    image: nginx
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.myapp.rule=Host(`myapp.example.com`)"
      - "traefik.http.routers.myapp.tls.certresolver=le"
```

## Avec Kubernetes (IngressRoute)

```yaml
apiVersion: traefik.io/v1alpha1
kind: IngressRoute
metadata:
  name: myapp
spec:
  entryPoints:
    - websecure
  routes:
    - match: Host(`myapp.example.com`)
      kind: Rule
      services:
        - name: myapp
          port: 80
  tls:
    certResolver: le
```

## Liens

- [[Reverse proxy]]
- [[Load balancing]]
- [[Networking]]
- [[TLS]]
