---
title: CSR (Certificate Signing Request)
tags: [security, intermediate]
---

# CSR (Certificate Signing Request)

## Définition

Un CSR est une demande de certificat envoyée à une CA. Il contient la clé publique et les informations d'identité du demandeur, sans la clé privée.

> [!tip] Pourquoi c'est important
> Le CSR est l'étape obligatoire pour obtenir un certificat signé par une CA. La clé privée ne quitte jamais le serveur.

## Générer un CSR

```bash
# Générer clé privée + CSR en une commande
openssl req -newkey rsa:2048 -nodes   -keyout server.key   -out server.csr   -subj "/CN=example.com/O=MyOrg/C=FR"

# Vérifier le contenu du CSR
openssl req -in server.csr -text -noout

# CSR avec Subject Alternative Names (SAN)
openssl req -newkey rsa:2048 -nodes   -keyout server.key   -out server.csr   -config san.cnf
```

## Fichier san.cnf

```ini
[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req

[req_distinguished_name]
CN = example.com

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = example.com
DNS.2 = www.example.com
```

## Liens

- [[CA]]
- [[Certificates]]
- [[TLS]]
