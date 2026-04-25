---
title: Automated release
tags:
  - intermediate
---
# Automated release

---

## Définition

L'automated release génère automatiquement les notes de release, les changelogs, et les tags de version à partir des [[Commit]] (Conventional Commits). Élimine la maintenance manuelle des changelogs.

---

## semantic-release

```yaml
# .github/workflows/release.yml
release:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Semantic Release
      uses: cycjimmy/semantic-release-action@v4
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

```json
// .releaserc.json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/github"
  ]
}
```

---

## Versioning automatique depuis les commits

```
feat: add user authentication   → v1.1.0 (minor bump)
fix: correct null pointer       → v1.0.1 (patch bump)
feat!: redesign API             → v2.0.0 (major bump, breaking change)
```

---

> [!tip]
> Combine avec [[Conventional Commits]] pour un [[Versioning]] sémantique entièrement automatisé.
