---
title: CA (Certificate Authority)
tags: [security, intermediate]
---

# CA (Certificate Authority)

## Définition

Une CA (Autorité de Certification) est une entité de confiance qui signe et émet des certificats numériques. Elle garantit l'identité du détenteur du certificat.

> [!tip] Pourquoi c'est important
> La CA est le pilier de confiance du système PKI. Les navigateurs et OS embarquent une liste de CA racines de confiance (Let's Encrypt, DigiCert, etc.).

## Hiérarchie PKI

```
Root CA (auto-signé, hors ligne)
  └── Intermediate CA
        └── Leaf certificate (serveur, client)
```

## Créer une CA interne

```bash
# Générer la clé privée de la CA
openssl genrsa -out ca.key 4096

# Créer le certificat racine auto-signé
openssl req -new -x509 -days 3650   -key ca.key   -out ca.crt   -subj "/CN=Internal CA/O=MyOrg/C=FR"

# Signer un certificat avec la CA
openssl x509 -req -in server.csr   -CA ca.crt -CAkey ca.key   -CAcreateserial   -out server.crt -days 365
```

## Liens

- [[Certificates]]
- [[CSR]]
- [[Self signed certificate]]
