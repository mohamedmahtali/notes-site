---
title: Mutual TLS (mTLS)
tags: [security, advanced]
---

# Mutual TLS (mTLS)

## Définition

Le mTLS (Mutual TLS) est une extension de TLS où le client ET le serveur s'authentifient mutuellement via certificats. Contrairement au TLS standard, le serveur vérifie aussi l'identité du client.

> [!tip] Pourquoi c'est important
> mTLS est la base de la sécurité zero-trust entre services. Il est utilisé dans les service meshes (Istio, Linkerd) pour sécuriser les communications inter-services dans Kubernetes.

## Flux mTLS

```
Client                          Serveur
  |-- ClientHello --------------->|
  |<-- ServerHello + Cert --------|
  |-- Client Certificate -------->|  ← spécifique mTLS
  |-- CertificateVerify --------->|
  |<-- Finished ------------------|
  |=== Données chiffrées ========>|
```

## Configuration Nginx (mTLS)

```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/ssl/server.crt;
    ssl_certificate_key /etc/ssl/server.key;

    # Demander et valider le certificat client
    ssl_client_certificate /etc/ssl/ca.crt;
    ssl_verify_client on;
    ssl_verify_depth 2;
}
```

## Test mTLS avec curl

```bash
curl --cert client.crt      --key client.key      --cacert ca.crt      https://api.example.com
```

## Liens

- [[TLS]]
- [[Handshake]]
- [[Zero trust]]
