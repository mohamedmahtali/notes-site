---
title: Image scanning
tags: [security, intermediate]
---

# Image scanning

## Définition

L'image scanning analyse les images de conteneurs pour détecter les vulnérabilités CVE dans les paquets OS et les dépendances applicatives avant le déploiement.

> [!tip] Pourquoi c'est important
> Une image Docker peut embarquer des centaines de paquets avec des vulnérabilités connues. Scanner en CI/CD permet de bloquer les images dangereuses avant qu'elles n'atteignent la production.

## Trivy (outil recommandé)

```bash
# Scanner une image
trivy image nginx:latest

# Format JSON pour intégration CI
trivy image --format json nginx:latest > results.json

# Scanner seulement les vulnérabilités avec fix disponible
trivy image --ignore-unfixed nginx:latest

# Scanner le filesystem local
trivy fs .

# Scanner un repo git
trivy repo https://github.com/myorg/myapp
```

## Intégration CI/CD

```yaml
# GitLab CI
container_scan:
  image: aquasec/trivy:latest
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $CI_IMAGE
```

## Liens

- [[Base image vulnerabilities]]
- [[CVE detection]]
- [[Policy enforcement]]
- [[Container security]]
- [[DevSecOps]]
