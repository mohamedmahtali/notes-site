---
title: Secure SDLC
tags:
  - security
  - intermediate
---

# Secure SDLC

## Définition

Le Secure Software Development Lifecycle (SSDLC) intègre des activités de sécurité à chaque phase du développement logiciel : conception, développement, test, déploiement et maintenance.

> [!note] Frameworks de référence
> Microsoft SDL, OWASP SAMM, BSIMM sont les frameworks les plus utilisés pour structurer un Secure SDLC.

## Phases et activités sécurité

| Phase | Activités sécurité |
|-------|-------------------|
| Conception | Threat modeling, revue d'architecture |
| Développement | Coding standards, [[SAST]], peer review |
| Test | [[DAST]], pen test, fuzzing |
| Déploiement | Hardening, [[Secrets]] scan, SBOM |
| Maintenance | Patch management, [[Monitoring]], IR |

## Threat modeling (STRIDE)

```
S - Spoofing (usurpation d'identité)
T - Tampering (altération de données)
R - Repudiation (déni d'action)
I - Information disclosure (fuite)
D - Denial of Service
E - Elevation of privilege
```

## SBOM (Software Bill of Materials)

```bash
# Générer un SBOM avec Syft
syft myapp:latest -o cyclonedx-json > sbom.json

# Analyser le SBOM avec Grype
grype sbom:./sbom.json
```

## Liens

- [[DevSecOps]]
- [[Shift left security]]
- [[Vulnerability scanning]]
