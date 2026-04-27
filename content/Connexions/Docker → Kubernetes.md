---
title: "Docker → Kubernetes : du conteneur à l'orchestration"
tags:
  - connexion
  - docker
  - kubernetes
  - intermediate
---

# Docker → Kubernetes : du conteneur à l'orchestration

## La progression naturelle

[[Docker]] permet de créer et faire tourner des conteneurs sur une machine. [[Kubernetes]] orchestre des centaines de ces conteneurs sur un cluster de machines. Docker sans Kubernetes fonctionne en dev ; en production, Kubernetes est presque incontournable.

```
Machine locale                    Cluster Kubernetes
─────────────────                 ──────────────────────────────────
docker build → image              
docker run → conteneur            Node 1    Node 2    Node 3
                                  ┌──────┐  ┌──────┐  ┌──────┐
                                  │Pod   │  │Pod   │  │Pod   │
image poussée sur registry   ──►  │app:v2│  │app:v2│  │app:v2│
(Docker Hub, ECR, GCR...)         └──────┘  └──────┘  └──────┘
                                       ↑          ↑
                                  Kubernetes décide où les placer,
                                  les redémarre si crash, les scale
```

## Ce que Kubernetes ajoute à Docker

| Besoin | Docker seul | Kubernetes |
|--------|-------------|------------|
| Redémarrage auto | Manuel / Docker restart | [[Deployments]] (self-healing) |
| Scaling | `docker run` × N fois | `kubectl scale` ou [[Autoscaling]] |
| Load balancing | Nginx manuel | [[Services]] K8s natif |
| Config & secrets | `-e VAR=val` | [[ConfigMaps]] & [[Secrets]] |
| Rollback | Relancer ancienne image | `kubectl rollout undo` |
| Multi-nœuds | Docker Swarm (limité) | Kubernetes natif |

## Le workflow complet

```
1. Développeur écrit Dockerfile
       │
       ▼
2. CI/CD build l'image
   docker build -t app:v2.1.0 .
       │
       ▼
3. Push sur le registry
   docker push registry/app:v2.1.0
       │
       ▼
4. Kubernetes pull l'image
   (spec: image: registry/app:v2.1.0)
       │
       ▼
5. Scheduler place les Pods sur les nœuds
       │
       ▼
6. Kubernetes maintient l'état souhaité
   (3 replicas toujours actifs)
```

## Dockerfile → Manifeste Kubernetes

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: registry/app:v2.1.0   # ← l'image Docker
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
```

## Points d'attention

> [!warning] Image légère = Pod léger
> Une image Docker de 2 Go ralentit chaque démarrage de Pod. Utiliser des images slim, multi-stage builds, et `.dockerignore` — ce qui est une bonne pratique Docker devient critique à l'échelle Kubernetes.

> [!tip] Tag explicite obligatoire en prod
> `image: app:latest` est dangereuse en Kubernetes : Kubernetes ne sait pas quand l'image a changé et peut ne pas la repuller. Toujours tagger avec un SHA ou une version sémantique.

## Pour aller plus loin

- [[Dockerfile]] — multi-stage builds, optimisation des layers
- [[Docker Registry]] — Docker Hub, ECR, GCR, Harbor
- [[Deployments]] — stratégies rolling update, blue/green
- [[Kubernetes]] — architecture cluster, scheduler, kubelet
- [[Autoscaling]] — HPA basé sur les métriques
