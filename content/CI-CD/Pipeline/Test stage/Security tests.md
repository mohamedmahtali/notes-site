---
title: Security tests
tags:
  - intermediate
---
# Security tests

## Parent
- [[Test stage]]

---

## Définition

Les security tests automatisés dans le pipeline détectent les vulnérabilités avant qu'elles n'atteignent la production : SAST (analyse statique), SCA (dépendances vulnérables), et scan d'images Docker.

---

## Types de security tests CI

| Type | Outil | Ce qu'il détecte |
|---|---|---|
| SAST | Semgrep, CodeQL | Bugs de sécurité dans le code |
| SCA | Trivy, Snyk, Dependabot | Dépendances vulnérables |
| Image scan | Trivy, Grype | CVE dans les images Docker |
| Secrets scan | TruffleHog, gitleaks | Secrets committés par erreur |

---

## Exemple pipeline

```yaml
security:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    # SAST avec CodeQL
    - uses: github/codeql-action/analyze@v3

    # Scan de dépendances
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: fs
        severity: HIGH,CRITICAL
        exit-code: 1

    # Scan image Docker
    - name: Scan Docker image
      run: |
        trivy image --severity HIGH,CRITICAL           --exit-code 1 myapp:${{ github.sha }}

    # Secrets scan
    - name: Scan for secrets
      uses: trufflesecurity/trufflehog@main
      with:
        path: ./
        base: ${{ github.event.repository.default_branch }}
```

---

> [!warning]
> Configurer `exit-code: 1` pour les vulnérabilités CRITICAL/HIGH afin de bloquer le pipeline. Pour les LOW/MEDIUM, créer des issues sans bloquer.
