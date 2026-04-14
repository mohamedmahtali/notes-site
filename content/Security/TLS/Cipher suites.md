---
title: Cipher suites
tags: [security, advanced]
---

# Cipher suites

## Définition

Une cipher suite est un ensemble d'algorithmes cryptographiques utilisés pour sécuriser une connexion TLS : échange de clés, authentification, chiffrement et intégrité.

> [!warning] Ciphers obsolètes
> DES, RC4, MD5, SHA-1 sont dangereux. Toujours utiliser des suites modernes avec Perfect Forward Secrecy (ECDHE).

## Format d'une cipher suite TLS 1.2

```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
│    │     │        │       │    │
│    │     │        │       │    └── MAC (intégrité)
│    │     │        │       └─────── Mode de chiffrement
│    │     │        └─────────────── Algo de chiffrement
│    │     └──────────────────────── Authentification
│    └────────────────────────────── Échange de clés
└─────────────────────────────────── Protocole
```

## Suites recommandées

```nginx
# TLS 1.3 (suites fixes, non configurables)
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256

# TLS 1.2 recommandées
ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305;
```

## Tester les ciphers

```bash
# Lister les ciphers supportés par un serveur
nmap --script ssl-enum-ciphers -p 443 example.com

# Test avec ssllabs (en ligne)
# https://www.ssllabs.com/ssltest/
```

## Liens

- [[TLS]]
- [[Handshake]]
