---
title: Private registry
tags:
  - intermediate
---

# Private registry

---

## Définition

Un registry privé est un registry accessible uniquement à une organisation ou équipe. Il peut être hébergé dans le [[Cloud]] (ECR, GCR, GHCR) ou auto-hébergé avec des outils comme Harbor ou le registry officiel [[Docker]].

---

## Registry Docker auto-hébergé

```bash
# Lancer un registry local
docker run -d   -p 5000:5000   --name registry   -v registry-data:/var/lib/registry   registry:2

# Pousser une image
docker tag mon-app:1.0 localhost:5000/mon-app:1.0
docker push localhost:5000/mon-app:1.0

# Tirer depuis le registry local
docker pull localhost:5000/mon-app:1.0
```

---

## Harbor (registry enterprise)

Harbor est un registry open source avec interface web, [[RBAC]], scanning de vulnérabilités, et réplication.

```bash
# Installation via Helm
helm install harbor harbor/harbor   --set expose.type=ingress   --set expose.tls.enabled=true   --set externalURL=https://registry.example.com
```

---

## AWS ECR

```bash
# Authentification (expire toutes les 12h)
aws ecr get-login-password --region eu-west-1 |   docker login --username AWS --password-stdin   123456789.dkr.ecr.eu-west-1.amazonaws.com

# Push
docker tag mon-app:1.0 123456789.dkr.ecr.eu-west-1.amazonaws.com/mon-app:1.0
docker push 123456789.dkr.ecr.eu-west-1.amazonaws.com/mon-app:1.0
```
