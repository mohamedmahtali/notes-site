---
title: OCI
tags:
  - advanced
---

# OCI

## Parent
- [[Container runtime]]

---

## Définition

L'OCI (Open Container Initiative) est une organisation qui maintient des **spécifications ouvertes** pour les conteneurs : le format d'image (`image-spec`) et le runtime (`runtime-spec`). L'OCI garantit l'interopérabilité entre les différents outils de conteneurisation.

---

## Spécifications OCI

| Spec | Description |
|---|---|
| `image-spec` | Format d'une image (layers, manifest, config) |
| `runtime-spec` | Interface pour créer et lancer un conteneur |
| `distribution-spec` | API d'un registry (pull/push) |

---

## Pourquoi c'est important

> [!tip] Interopérabilité
> Une image buildée avec Docker peut être lancée par containerd, Podman, ou kata-containers. Un registry compatible OCI (Docker Hub, GHCR, ECR) accepte les images de n'importe quel builder OCI-compliant.

---

## Outils OCI-compatibles

```
Build :   docker build, buildah, kaniko, ko
Runtime : runc, crun, kata-containers, gVisor
Registry : Docker Hub, GHCR, ECR, GCR, Harbor
CLI :     docker, podman, nerdctl, crictl
```

---

> [!note]
> Toutes les images Docker sont des images OCI. Depuis Docker 1.12, Docker utilise la spécification OCI pour ses images et son runtime.
