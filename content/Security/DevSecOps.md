---
title: DevSecOps
tags: [security, intermediate]
---

# DevSecOps

## Définition

DevSecOps intègre la sécurité dans chaque étape du cycle de développement (DevOps). Plutôt qu'un audit final, la sécurité devient une responsabilité partagée dès le début.

> [!tip] Pourquoi c'est important
> Les vulnérabilités détectées en production coûtent 30x plus à corriger qu'en phase de développement. DevSecOps réduit ce coût en détectant les problèmes tôt.

## Pipeline DevSecOps

```
Code → SAST → Build → Image Scan → Deploy → DAST → Monitor
  ↑                                                     |
  └─────────────── Feedback loop ──────────────────────┘
```

## Intégration dans CI/CD

```yaml
# GitHub Actions - pipeline sécurisé
name: DevSecOps Pipeline
on: [push]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # SAST
      - name: Run Semgrep
        run: semgrep --config=auto .

      # Dependency scanning
      - name: Check dependencies
        run: trivy fs --security-checks vuln .

      # Build & image scan
      - name: Build and scan image
        run: |
          docker build -t myapp:${{ github.sha }} .
          trivy image myapp:${{ github.sha }}
```

## Liens

- [[Shift left security]]
- [[Secure SDLC]]
- [[Security gates]]
- [[Vulnerability scanning]]
- [[Image scanning]]
