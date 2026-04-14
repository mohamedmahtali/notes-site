---
title: TLS
tags: [security, intermediate]
---

# TLS (Transport Layer Security)

## Définition

TLS est un protocole cryptographique qui sécurise les communications sur un réseau. Il assure confidentialité, intégrité et authentification. TLS 1.3 est la version actuelle recommandée.

> [!tip] Pourquoi c'est important
> TLS protège toutes les communications HTTPS, les emails, les connexions à base de données et les APIs. C'est la brique fondamentale de la sécurité réseau moderne.

## Versions

| Version | Statut |
|---------|--------|
| SSL 2/3 | Obsolète, interdit |
| TLS 1.0/1.1 | Déprécié |
| TLS 1.2 | Encore utilisé |
| TLS 1.3 | Recommandé |

## Configuration Nginx

```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/cert.pem;
    ssl_certificate_key /etc/ssl/private/key.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
}
```

## Liens

- [[Handshake]]
- [[Certificates]]
- [[Cipher suites]]
- [[Mutual TLS]]
