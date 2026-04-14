---
title: Artifacts
tags:
  - intermediate
---
# Artifacts

## Parent
- [[CI-CD]]

## Enfants
- [[Build outputs]]
- [[Versioning]]
- [[Artifact repositories]]

---

## Définition

Les artifacts CI/CD sont les fichiers produits par le pipeline (binaires compilés, images Docker, packages, rapports de tests) et conservés pour utilisation dans les stages suivants ou pour déploiement.

---

## Pourquoi c'est important

> [!tip] Build once, deploy many
> Un artefact est construit une seule fois et promu à travers les environnements (staging → production). Jamais rebuilt. Ça garantit que ce qui est testé est exactement ce qui est déployé.

---

## GitHub Actions

```yaml
# Produire un artefact
- name: Build
  run: npm run build

- name: Upload artifact
  uses: actions/upload-artifact@v4
  with:
    name: build-${{ github.sha }}
    path: dist/
    retention-days: 30

# Consommer dans un autre job
download:
  needs: build
  steps:
    - uses: actions/download-artifact@v4
      with:
        name: build-${{ github.sha }}
        path: dist/
```

---

## GitLab CI

```yaml
build:
  artifacts:
    paths:
      - dist/
    reports:
      junit: test-results.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
    expire_in: 1 week
    when: always    # conserver même en cas d'échec
```

---

> [!note]
> Voir [[Artifact repositories]] pour stocker dans Nexus, JFrog Artifactory, ou GitHub Packages.
