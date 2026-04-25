---
title: Build outputs
tags:
  - intermediate
---
# Build outputs

---

## Définition

Les build outputs sont les fichiers générés par l'étape de compilation/build : binaires, archives, images [[Docker]], [[Package]]. Ils sont les livrables concrets du [[Pipeline]].

---

## Types par technologie

| Technologie | Output | Extension |
|---|---|---|
| [[Node]].js | Bundle webpack/vite | `.js`, `dist/` |
| Python | Package | `.whl`, `.tar.gz` |
| Go | Binaire statique | aucune |
| Java | Archive exécutable | `.jar`, `.war` |
| Docker | Image | registry tag |
| [[Helm]] | Chart | `.tgz` |

---

## Conservation et partage

```yaml
# GitHub Actions — upload build pour le job suivant
- uses: actions/upload-artifact@v4
  with:
    name: myapp-${{ github.sha }}
    path: |
      dist/
      !dist/**/*.map    # exclure les source maps

# Télécharger dans un autre job
- uses: actions/download-artifact@v4
  with:
    name: myapp-${{ github.sha }}
    path: ./artifacts
```

---

> [!tip]
> Toujours inclure le SHA du [[Commit]] dans le nom de l'artefact. Ça permet de tracer exactement quel code a produit quel artefact, et de [[Rollback]] vers n'importe quelle version précédente.
