---
title: Resource limits
tags:
  - intermediate
---

# Resource limits

## Définition

Par défaut, un conteneur Docker peut utiliser toutes les ressources CPU et mémoire de l'hôte. Les resource limits définissent des plafonds qui protègent les autres conteneurs et l'hôte d'un conteneur défaillant ou malveillant.

## docker run

```bash
# Limiter mémoire et CPU
docker run -d \
  --memory=512m \
  --memory-swap=512m \   # = memory → pas de swap
  --cpus=0.5 \           # 50% d'un CPU
  --name api \
  mon-app

# Voir les ressources en temps réel
docker stats
docker stats --no-stream  # snapshot unique

# Voir les limites configurées
docker inspect mon-app | grep -A 10 '"HostConfig"'
```

## Options disponibles

| Option | Description | Exemple |
|---|---|---|
| `--memory` | Limite RAM | `--memory=512m` |
| `--memory-swap` | RAM + swap total (= memory → pas de swap) | `--memory-swap=512m` |
| `--memory-reservation` | Soft limit (best-effort) | `--memory-reservation=256m` |
| `--cpus` | Nombre de CPUs | `--cpus=1.5` |
| `--cpu-shares` | Poids relatif (1024 = défaut) | `--cpu-shares=512` |
| `--pids-limit` | Limite processus (anti fork-bomb) | `--pids-limit=100` |

## Docker Compose

```yaml
services:
  api:
    image: mon-app:latest
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

## OOMKilled — diagnostic

Quand un conteneur dépasse sa limite mémoire, le kernel Linux le tue via OOMKill (Out Of Memory Killer).

```bash
# Détecter un OOMKill
docker inspect mon-app --format '{{.State.OOMKilled}}'
# → true

# Logs du kernel (sur l'hôte)
dmesg | grep -i "oom"
dmesg | grep -i "killed process"

# Remontée dans les événements Docker
docker events --filter event=oom
```

Symptômes : le conteneur se redémarre avec exit code 137 (128 + SIGKILL).

## Équivalent Kubernetes

Dans Kubernetes, les limites s'expriment au niveau du container dans le Pod :

```yaml
spec:
  containers:
    - name: api
      image: mon-app:latest
      resources:
        requests:          # minimum garanti (pour le scheduling)
          memory: "256Mi"
          cpu: "250m"      # 250 millicores = 0.25 CPU
        limits:            # maximum absolu (OOMKill si dépassé)
          memory: "512Mi"
          cpu: "500m"
```

Différence importante : `requests` influence le scheduling (le pod sera placé sur un node avec assez de ressources libres), `limits` est le plafond dur.

## Explorer

- **[[CPU limits]]** — détail du throttling CPU, cpu-shares vs cpus
- **[[Containers]]** — cycle de vie des conteneurs Docker
- **[[Kubernetes]]** — requests/limits dans les workloads K8s
