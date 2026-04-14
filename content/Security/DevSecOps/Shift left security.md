---
title: Shift left security
tags: [security, intermediate]
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

## Liens

- [[DevSecOps]]
- [[Secure SDLC]]
- [[Security gates]]
- [[Vulnerability scanning]]
