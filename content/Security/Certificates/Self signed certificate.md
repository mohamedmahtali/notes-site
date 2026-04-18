---
title: Self-signed certificate
tags: [security, beginner]
---

# Self-signed certificate

## Définition

Un certificat auto-signé est signé par sa propre clé privée, sans CA externe. Il est utile pour les environnements de développement et les réseaux internes.

> [!warning] Limitation
> Les navigateurs et clients font confiance aux CA reconnues. Un certificat auto-signé génère des avertissements de sécurité. Ne jamais utiliser en production publique.

## Créer un certificat auto-signé

```bash
# Certificat auto-signé simple (1 commande)
openssl req -x509 -newkey rsa:2048 -nodes   -keyout key.pem   -out cert.pem   -days 365   -subj "/CN=localhost/O=Dev/C=FR"

# Avec SAN pour localhost
openssl req -x509 -newkey rsa:2048 -nodes   -keyout key.pem   -out cert.pem   -days 365   -extensions v3_req   -subj "/CN=localhost"   -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
```

## mkcert — alternative simple pour le dev local

`mkcert` crée une CA locale et génère des certificats de confiance en une commande, sans les warnings navigateur.

```bash
# Installation
brew install mkcert        # macOS
apt install mkcert         # Linux

# Installer la CA locale dans les stores système + navigateurs
mkcert -install

# Générer un certificat pour localhost et domaines locaux
mkcert localhost 127.0.0.1 myapp.local "*.myapp.local"
# → génère localhost+3.pem et localhost+3-key.pem
```

## Faire confiance au certificat manuellement

```bash
# Linux — ajouter au store système
sudo cp cert.pem /usr/local/share/ca-certificates/myapp.crt
sudo update-ca-certificates

# macOS
sudo security add-trusted-cert -d -r trustRoot \
  -k /Library/Keychains/System.keychain cert.pem

# Vérifier qu'un certificat est valide
openssl verify -CAfile ca.crt cert.pem
openssl s_client -connect localhost:443 -CAfile ca.crt
```

## Utiliser dans Docker Compose

```yaml
services:
  nginx:
    image: nginx
    volumes:
      - ./cert.pem:/etc/nginx/ssl/cert.pem
      - ./key.pem:/etc/nginx/ssl/key.pem
    ports:
      - "443:443"
```

## Liens

- [[Certificates]]
- [[CA]]
- [[TLS]]
