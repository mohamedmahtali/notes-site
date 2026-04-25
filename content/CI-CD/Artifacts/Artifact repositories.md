---
title: Artifact repositories
tags:
  - intermediate
---
# Artifact repositories

---

## Définition

Les artifact repositories sont des systèmes de stockage dédiés aux artefacts de build : [[Package]], images [[Docker]], binaires. Ils gèrent le [[Versioning]], l'accès, la rétention, et la promotion entre environnements.

---

## Solutions populaires

| Solution | Type | Hébergement |
|---|---|---|
| JFrog Artifactory | Universal | Self-hosted / [[Cloud]] |
| Nexus [[Repository]] | Universal | Self-hosted |
| GitHub Packages | npm, Docker, Maven | Cloud (GitHub) |
| [[AWS]] ECR | Docker uniquement | AWS |
| Google Artifact Registry | Docker, npm, Maven | GCP |

---

## GitHub Packages — Docker registry

```yaml
- name: Login to GitHub Container Registry
  uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}

- name: Build and push
  uses: docker/build-push-action@v5
  with:
    push: true
    tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

---

## Nexus — configuration Maven

```xml
<!-- pom.xml -->
<distributionManagement>
  <repository>
    <id>nexus</id>
    <url>https://nexus.mycompany.com/repository/maven-releases/</url>
  </repository>
</distributionManagement>
```

---

> [!note]
> Configurer des politiques de rétention pour éviter que les repositories ne grossissent indéfiniment. Garder les 10 derniers builds par branche, et toutes les versions taggées.
