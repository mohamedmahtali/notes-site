---
title: Verify explicitly
tags:
  - security
  - intermediate
---

# Verify explicitly

## Définition

"Verify explicitly" signifie authentifier et autoriser chaque requête sur la base de toutes les données disponibles : identité, localisation, device, service, charge de travail. Jamais d'accès implicite basé sur le réseau ou l'IP.

> [!tip] Facteurs de vérification
> Identité (qui), appareil (quoi), localisation (d'où), heure (quand), comportement (comment). Plus on vérifie de facteurs, plus la confiance est élevée.

## Mécanismes de vérification

```
Utilisateurs : MFA (TOTP, hardware key), SSO/OIDC
Services      : mTLS, JWT signé, SPIFFE/SPIRE
Appareils     : Certificats device, posture check
APIs          : API keys + OAuth2, signed requests
```

## SPIFFE/SPIRE (identité de service)

```yaml
# Chaque workload obtient une identité SPIFFE
# URI format: spiffe://trust-domain/path

# SPIRE génère des SVIDs (SPIFFE Verifiable Identity Documents)
# sous forme de certificats X.509 avec durée de vie courte

# Exemple d'identité SPIFFE
spiffe://example.org/ns/default/sa/myapp
```

## Liens

- [[Zero trust]]
- [[Assume breach]]
- [[Least privilege access]]
- [[Mutual TLS]]
