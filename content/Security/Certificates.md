---
title: Certificates
tags:
  - security
  - intermediate
---

# Certificates

## Définition

Un certificat numérique est un fichier électronique qui lie une clé publique à une identité (domaine, organisation, personne). Il est signé par une autorité de certification (CA) pour garantir son authenticité.

> [!tip] Pourquoi c'est important
> Les certificats sont la base du chiffrement TLS/HTTPS. Sans eux, impossible de garantir l'identité d'un serveur ni de sécuriser les communications.

## Structure d'un certificat X.509

```
Subject: CN=example.com, O=My Org, C=FR
Issuer: CN=Let's Encrypt R3
Validity: 2024-01-01 → 2024-04-01
Public Key: RSA 2048 bits
Signature: SHA256withRSA
```

## Commandes utiles

```bash
# Afficher un certificat
openssl x509 -in cert.pem -text -noout

# Vérifier la date d'expiration
openssl x509 -in cert.pem -noout -dates

# Tester un certificat en live
openssl s_client -connect example.com:443

# Vérifier la chaîne de certification
openssl verify -CAfile ca.pem cert.pem
```

## Liens

- [[CA]]
- [[CSR]]
- [[Certificate renewal]]
- [[Self signed certificate]]
- [[TLS]]
