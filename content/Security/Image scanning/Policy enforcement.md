---
title: Policy enforcement
tags: [security, advanced]
---

# Policy enforcement

## Définition

L'enforcement de politique automatise le blocage des images qui ne respectent pas les règles de sécurité définies (vulnérabilités critiques, images non signées, images non approuvées).

> [!tip] Pourquoi c'est important
> Sans enforcement, les développeurs peuvent ignorer les alertes de sécurité. L'enforcement rend les règles non-contournables dans le pipeline et au niveau Kubernetes.

## Admission controllers Kubernetes

```yaml
# OPA Gatekeeper : politique d'images signées
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sAllowedRepos
metadata:
  name: allowed-repos
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
  parameters:
    repos:
      - "gcr.io/myorg/"
      - "registry.internal/"
```

## Cosign (signature d'images)

```bash
# Signer une image
cosign sign --key cosign.key myrepo/myapp:latest

# Vérifier la signature
cosign verify --key cosign.pub myrepo/myapp:latest

# Politique Sigstore dans Kubernetes
# (via policy-controller de Sigstore)
```

## Liens

- [[Image scanning]]
- [[CVE detection]]
- [[DevSecOps]]
- [[Security gates]]
