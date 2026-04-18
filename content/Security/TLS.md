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

## Certificats Let's Encrypt avec Certbot

```bash
# Installer certbot
apt install certbot python3-certbot-nginx

# Obtenir et installer un certificat (mode automatique Nginx)
certbot --nginx -d example.com -d www.example.com

# Renouvellement manuel
certbot renew --dry-run    # Tester
certbot renew               # Renouveler

# Renouvellement automatique (cron)
0 3 * * * certbot renew --quiet --post-hook "systemctl reload nginx"
```

## Headers de sécurité TLS

```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    # Versions et ciphers recommandés
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;

    # Session cache (performance)
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;

    # OCSP Stapling (validation certificat rapide)
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 8.8.8.8 valid=300s;

    # HSTS — force HTTPS pendant 1 an
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
}

# Redirect HTTP → HTTPS
server {
    listen 80;
    server_name example.com www.example.com;
    return 301 https://$host$request_uri;
}
```

## Tester la configuration TLS

```bash
# Test rapide
curl -I https://example.com

# Inspecter le certificat
openssl s_client -connect example.com:443 -servername example.com

# Vérifier la date d'expiration
echo | openssl s_client -connect example.com:443 2>/dev/null \
  | openssl x509 -noout -dates

# Score SSL Labs (via CLI)
curl "https://api.ssllabs.com/api/v3/analyze?host=example.com" | jq '.grade'
```

## Liens

- [[Handshake]]
- [[Certificates]]
- [[Cipher suites]]
- [[Mutual TLS]]
