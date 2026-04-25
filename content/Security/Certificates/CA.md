---
title: CA (Certificate Authority)
tags:
  - security
  - intermediate
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
# 1. Générer la clé privée de la CA
openssl genrsa -out ca.key 4096

# 2. Créer le certificat racine auto-signé (valide 10 ans)
openssl req -new -x509 -days 3650 \
  -key ca.key -out ca.crt \
  -subj "/CN=Internal CA/O=MyOrg/C=FR"
```

## Générer et signer un certificat serveur

```bash
# 1. Générer la clé privée du serveur
openssl genrsa -out server.key 2048

# 2. Générer une CSR (Certificate Signing Request)
openssl req -new \
  -key server.key \
  -out server.csr \
  -subj "/CN=myapp.internal/O=MyOrg/C=FR"

# 3. Créer un fichier d'extensions (SAN obligatoire pour Chrome/Firefox)
cat > server.ext <<EOF
subjectAltName = DNS:myapp.internal, DNS:*.myapp.internal, IP:10.0.0.1
EOF

# 4. Signer avec la CA
openssl x509 -req -days 365 \
  -in server.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial \
  -extfile server.ext \
  -out server.crt
```

## Inspecter et vérifier

```bash
# Afficher les détails d'un certificat
openssl x509 -in server.crt -text -noout

# Vérifier la chaîne de confiance
openssl verify -CAfile ca.crt server.crt

# Voir les dates d'expiration
openssl x509 -in server.crt -noout -dates

# Tester un serveur TLS
openssl s_client -connect myapp.internal:443 -CAfile ca.crt
```

> [!warning] CA racine hors ligne
> En production, la clé privée de la Root CA doit rester hors ligne (HSM ou stockage chiffré). Utiliser une Intermediate CA pour les opérations courantes.

## Liens

- [[Certificates]]
- [[CSR]]
- [[Self signed certificate]]
