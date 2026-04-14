---
title: Package
tags:
  - intermediate
---
# Package

## Parent
- [[Build stage]]

---

## Définition

Le packaging produit une archive distribuable (`.tar.gz`, `.zip`, `.deb`, `.rpm`, `.whl`, `.jar`) qui peut être publiée dans un artifact repository ou déployée directement.

---

## Exemples

```yaml
# Node.js — package npm
- name: Package
  run: |
    npm ci
    npm run build
    npm pack    # produit un .tgz

# Python — wheel
- name: Build wheel
  run: |
    pip install build
    python -m build    # produit dist/*.whl et dist/*.tar.gz

# Debian package
- name: Build .deb
  run: |
    dpkg-buildpackage -us -uc

# Archive binaire avec version
- name: Create release archive
  run: |
    VERSION=${{ github.ref_name }}
    tar -czf myapp-${VERSION}-linux-amd64.tar.gz -C ./bin .
```

---

## Upload vers GitHub Releases

```yaml
- name: Upload artifact
  uses: actions/upload-artifact@v4
  with:
    name: myapp-${{ github.sha }}
    path: dist/
    retention-days: 30
```

---

> [!note]
> Voir [[Artifact repositories]] pour stocker les packages dans Nexus, JFrog, ou GitHub Packages.
