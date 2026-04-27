---
title: Private registry
tags:
  - intermediate
---

# Private registry

## Définition

Un registry privé est un registry d'images Docker accessible uniquement à une organisation ou équipe. Il peut être hébergé dans le cloud (ECR, GCR, GHCR) ou auto-hébergé avec Harbor ou le registry officiel Docker.

## Registry cloud — comparaison

| Registry | Provider | Authentification | Scanning intégré |
|----------|----------|-----------------|-----------------|
| ECR | AWS | `aws ecr get-login-password` | ✅ (Inspector) |
| GCR / Artifact Registry | GCP | `gcloud auth configure-docker` | ✅ (Container Analysis) |
| GHCR | GitHub | `ghcr.io`, token GitHub | ❌ (via Trivy) |
| GitLab Registry | GitLab | `$CI_REGISTRY_PASSWORD` | ✅ (intégré) |
| Docker Hub | Docker | `docker login` | ✅ (payant) |

## AWS ECR

```bash
# Authentification (token valable 12h)
aws ecr get-login-password --region eu-west-1 | \
  docker login --username AWS --password-stdin \
  123456789.dkr.ecr.eu-west-1.amazonaws.com

# Créer un repo
aws ecr create-repository --repository-name mon-app --region eu-west-1

# Build, tag et push
docker build -t mon-app:1.0 .
docker tag mon-app:1.0 123456789.dkr.ecr.eu-west-1.amazonaws.com/mon-app:1.0
docker push 123456789.dkr.ecr.eu-west-1.amazonaws.com/mon-app:1.0
```

## GitHub Container Registry (GHCR)

```bash
# Authentification avec un PAT (Personal Access Token)
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Push
docker tag mon-app:1.0 ghcr.io/myorg/mon-app:1.0
docker push ghcr.io/myorg/mon-app:1.0
```

```yaml
# GitHub Actions — push automatique à chaque merge
- name: Login to GHCR
  uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}  # token automatique, pas besoin de secret manuel

- name: Build and push
  uses: docker/build-push-action@v5
  with:
    push: true
    tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

## Registry Docker auto-hébergé

```bash
# Lancer un registry local (dev)
docker run -d \
  -p 5000:5000 \
  --name registry \
  -v registry-data:/var/lib/registry \
  registry:2

# Utiliser le registry local
docker tag mon-app:1.0 localhost:5000/mon-app:1.0
docker push localhost:5000/mon-app:1.0
docker pull localhost:5000/mon-app:1.0
```

## Harbor — registry enterprise

Harbor est un registry open source avec UI, RBAC, scanning, et réplication entre registries.

```bash
# Installation via Helm
helm repo add harbor https://helm.goharbor.io
helm install harbor harbor/harbor \
  --set expose.type=ingress \
  --set expose.tls.enabled=true \
  --set externalURL=https://registry.example.com \
  --set harborAdminPassword=MyPassword
```

Fonctionnalités clés : scanning Trivy/Clair intégré, réplication inter-registries, webhooks, audit logs, quotas par projet.

## Utiliser un registry privé dans Kubernetes

```bash
# Créer un Secret avec les credentials registry
kubectl create secret docker-registry registry-creds \
  --docker-server=ghcr.io \
  --docker-username=myuser \
  --docker-password=$GITHUB_TOKEN \
  --namespace=production
```

```yaml
# Référencer le secret dans le Pod
spec:
  imagePullSecrets:
    - name: registry-creds
  containers:
    - name: app
      image: ghcr.io/myorg/mon-app:1.0
```

> [!tip]
> Sur AWS EKS avec ECR, utiliser le plugin `amazon-ecr-credential-helper` ou une `ServiceAccount` avec IRSA pour éviter de gérer les credentials manuellement.

## Explorer

- **[[Docker registry]]** — concepts generaux, Docker Hub
- **[[Image scanning]]** — scan des images avant push (Trivy)
- **[[IAM]]** — permissions ECR, rôles pour les services
- **[[Kubernetes]]** — imagePullSecrets, IRSA pour ECR
