---
title: CVE detection
tags: [security, intermediate]
---

# CVE detection

## Définition

CVE (Common Vulnerabilities and Exposures) est un référentiel standardisé de vulnérabilités connues. La détection CVE consiste à identifier quels CVEs affectent les composants d'une image ou d'une application.

> [!note] CVSS Score
> Chaque CVE a un score CVSS (0-10) : LOW (<4), MEDIUM (4-6.9), HIGH (7-8.9), CRITICAL (9-10). Prioriser les patches des CVEs HIGH et CRITICAL.

## Rechercher des CVEs

```bash
# Trivy : détection CVE dans une image
trivy image --severity HIGH,CRITICAL python:3.11

# Filtrer par CVE spécifique
trivy image --format json nginx:latest   | jq '.Results[].Vulnerabilities[] | select(.VulnerabilityID == "CVE-2023-XXXX")'

# Grype : alternative
grype nginx:latest

# OSV-scanner (Google)
osv-scanner --docker nginx:latest
```

## Bases de données CVE utilisées

| Base | Source |
|------|--------|
| NVD | NIST National Vulnerability Database |
| GitHub Advisory | Dépendances applicatives |
| OSV | Open Source Vulnerabilities |
| Vendor advisories | Red Hat, Debian, Alpine... |

## Liens

- [[Image scanning]]
- [[Base image vulnerabilities]]
- [[Vulnerability scanning]]
