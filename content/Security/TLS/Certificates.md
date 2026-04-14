---
title: TLS Certificates
tags: [security, intermediate]
---

# TLS Certificates

## Définition

Les certificats TLS sont les certificats X.509 utilisés spécifiquement pour sécuriser les connexions TLS/HTTPS. Ils lient un nom de domaine à une clé publique.

> [!tip] Pourquoi c'est important
> Sans certificat TLS valide, les navigateurs affichent une erreur de sécurité et les utilisateurs ne peuvent pas accéder au service en toute sécurité.

## Types de certificats

| Type | Validation | Usage |
|------|-----------|-------|
| DV (Domain Validated) | Domaine seulement | Sites standards |
| OV (Organization Validated) | Domaine + org | Services pro |
| EV (Extended Validation) | Audit complet | Banques |
| Wildcard | *.example.com | Multi-sous-domaines |
| Multi-SAN | Plusieurs domaines | Flexibilité |

## Vérifier un certificat TLS

```bash
# Certificat d'un serveur
openssl s_client -connect example.com:443 -showcerts

# Expiration
echo | openssl s_client -connect example.com:443 2>/dev/null   | openssl x509 -noout -dates

# Informations complètes
curl -vI https://example.com 2>&1 | grep -A5 "SSL"
```

## Liens

- [[TLS]]
- [[Handshake]]
- [[Mutual TLS]]
- [[Certificates]]
