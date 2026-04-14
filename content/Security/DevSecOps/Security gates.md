---
title: Security gates
tags: [security, intermediate]
---

# Security gates

## Définition

Les security gates (portes de sécurité) sont des points de contrôle dans le pipeline CI/CD qui bloquent automatiquement le déploiement si des vulnérabilités critiques sont détectées.

> [!warning] Équilibre sécurité/vélocité
> Des gates trop stricts bloquent la production pour des vulnérabilités mineures. Calibrer les seuils (CRITICAL only, CVSS > 7) pour bloquer les vraies menaces sans paralyser les équipes.

## Exemple de gate dans GitHub Actions

```yaml
- name: Image vulnerability gate
  run: |
    trivy image       --exit-code 1       --severity CRITICAL       --ignore-unfixed       myapp:${{ github.sha }}
  # exit-code 1 = échec du job si vulnérabilité CRITICAL trouvée
```

## Gate avec politique OPA

```rego
# policy/image_scan.rego
package main

deny[msg] {
  vuln := input.vulnerabilities[_]
  vuln.severity == "CRITICAL"
  msg := sprintf("CRITICAL CVE: %v", [vuln.vulnerabilityID])
}
```

## Seuils recommandés

| Environnement | Bloquer sur |
|--------------|-------------|
| PR/feature | HIGH + CRITICAL |
| Main branch | CRITICAL seulement |
| Production | CRITICAL avec patch disponible |

## Liens

- [[DevSecOps]]
- [[Shift left security]]
- [[Vulnerability scanning]]
- [[Image scanning]]
