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

## Faire confiance au certificat (Linux)

```bash
# Copier dans les CA système
sudo cp cert.pem /usr/local/share/ca-certificates/myapp.crt
sudo update-ca-certificates
```

## Liens

- [[Certificates]]
- [[CA]]
- [[TLS]]
