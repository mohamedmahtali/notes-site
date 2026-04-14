---
title: CPU limits
tags:
  - intermediate
---

# CPU limits

## Parent
- [[Resource limits]]

---

## Définition

Les CPU limits contrôlent la quantité de puissance CPU qu'un conteneur peut utiliser. Docker expose les cgroups Linux pour définir des quotas CPU précis.

---

## Options

```bash
# Limiter à 1.5 CPUs (150% d'un core)
docker run --cpus=1.5 mon-app

# Limiter à 50% d'un CPU
docker run --cpus=0.5 mon-app

# Affecter à des CPUs spécifiques (0 et 1)
docker run --cpuset-cpus=0,1 mon-app

# Poids relatif (défaut 1024 = priorité normale)
docker run --cpu-shares=512 mon-app   # 50% de priorité relative
```

---

## En Docker Compose

```yaml
services:
  api:
    image: mon-app:latest
    deploy:
      resources:
        limits:
          cpus: '0.50'
        reservations:
          cpus: '0.25'
```

---

> [!tip]
> Sur un hôte avec 4 CPUs, `--cpus=0.5` limite le conteneur à utiliser 50% d'un core en moyenne, quelle que soit la charge globale.
