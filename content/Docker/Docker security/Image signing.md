---
title: Image signing
tags:
  - advanced
---

# Image signing

## Parent
- [[Docker security]]

---

## Définition

La signature d'images Docker garantit l'**authenticité et l'intégrité** d'une image — elle certifie que l'image vient bien de la source attendue et n'a pas été modifiée. C'est un contrôle de supply chain essentiel.

---

## Outils

| Outil | Description |
|---|---|
| Docker Content Trust (DCT) | Signing intégré à Docker |
| Cosign (Sigstore) | Standard moderne, CNCF |
| Notary v2 | Successeur de DCT |

---

## Cosign (recommandé)

```bash
# Installer cosign
brew install cosign   # macOS
# ou depuis les releases GitHub

# Générer une paire de clés
cosign generate-key-pair

# Signer une image
cosign sign --key cosign.key ghcr.io/org/app:1.0

# Vérifier une image
cosign verify --key cosign.pub ghcr.io/org/app:1.0

# Signature keyless (via OIDC, recommandé en CI)
cosign sign --yes ghcr.io/org/app:1.0   # utilise OIDC GitHub Actions
```

---

## Docker Content Trust

```bash
# Activer la vérification des signatures
export DOCKER_CONTENT_TRUST=1

# Pull d'une image signée seulement
docker pull nginx:latest
```

---

> [!tip]
> Cosign avec signature keyless (Sigstore/Rekor) est l'approche moderne recommandée. La signature est liée à l'identité OIDC du pipeline CI (GitHub Actions, GitLab CI) sans gestion de clés manuelles.
