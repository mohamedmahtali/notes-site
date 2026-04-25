---
title: Shift left security
tags:
  - security
  - intermediate
---

# Shift left security

## Définition

"Shift left" signifie déplacer les contrôles de sécurité vers la gauche du cycle de vie (vers le développement), plutôt que de les effectuer uniquement en fin de cycle.

> [!tip] Pourquoi c'est important
> Plus une vulnérabilité est détectée tôt, moins elle est coûteuse à corriger. Détecter dans l'IDE coûte quasi rien ; en production, cela peut coûter des millions.

## Niveaux de shift left

```
IDE          → Plugins de sécurité (SonarLint, Snyk)
Pre-commit   → git hooks (gitleaks, detect-secrets)
CI/CD        → SAST, dependency scanning, image scan
Staging      → DAST, pen tests
Production   → Runtime security, monitoring
```

## Pre-commit hooks de sécurité

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/zricethezav/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

## SAST en CI (analyse statique)

```yaml
# GitHub Actions — SAST avec Semgrep
- name: SAST Scan
  uses: returntocorp/semgrep-action@v1
  with:
    config: >-
      p/owasp-top-ten
      p/secrets
      p/docker

# Ou avec Trivy (code + dépendances + IaC)
- name: Trivy scan
  uses: aquasecurity/trivy-action@master
  with:
    scan-type: 'fs'
    scan-ref: '.'
    format: 'sarif'
    output: 'trivy-results.sarif'
    severity: 'HIGH,CRITICAL'

- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: 'trivy-results.sarif'
```

## Dependency scanning

```yaml
# Snyk — vulnérabilités dans les dépendances
- name: Snyk test
  uses: snyk/actions/node@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
  with:
    args: --severity-threshold=high

# OWASP Dependency-Check (Java/Maven)
- name: Dependency Check
  uses: dependency-check/Dependency-Check_Action@main
  with:
    project: 'myapp'
    path: '.'
    format: 'HTML'
    args: --failOnCVSS 7
```

## Security gate en pipeline complet

```yaml
jobs:
  security:
    steps:
    - name: Secret scanning    # gitleaks
    - name: SAST               # semgrep/trivy fs
    - name: Dependency scan    # snyk/trivy
    - name: Build image
    - name: Image scan         # trivy image, grype
    - name: IaC scan           # checkov, tfsec
    # Bloque le déploiement si HIGH/CRITICAL trouvé
```

> [!tip] SARIF → GitHub [[Security]] tab
> Les outils compatibles SARIF (Semgrep, Trivy, CodeQL) remontent leurs résultats directement dans l'onglet "Security" du repo GitHub — pas besoin d'un outil externe pour visualiser.

## Liens

- [[DevSecOps]]
- [[Secure SDLC]]
- [[Security gates]]
- [[Vulnerability scanning]]
