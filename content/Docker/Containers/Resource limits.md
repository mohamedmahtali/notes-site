---
title: Resource limits
tags:
  - intermediate
---

# Resource limits

## Parent
- [[Containers]]

## Enfants
- [[CPU limits]]
- [[Memory limits]]

---

## Définition

Par défaut, un conteneur Docker peut utiliser toutes les ressources CPU et mémoire de l'hôte. Les resource limits définissent des plafonds qui protègent les autres conteneurs et l'hôte d'un conteneur défaillant ou malveillant.

---

## Commandes

```bash
# Limiter mémoire et CPU
docker run -d   --memory=512m   --memory-swap=512m   --cpus=0.5   --name api   mon-app

# Voir les ressources en temps réel
docker stats

# Voir les limites d'un conteneur
docker inspect mon-app | grep -A5 '"HostConfig"'
```

---

## Résumé des options

| Option | Description |
|---|---|
| `--memory=512m` | Limite RAM à 512 Mo |
| `--memory-swap=512m` | = mémoire → pas de swap |
| `--cpus=1.5` | Limite à 1.5 CPUs |
| `--cpu-shares=512` | Poids relatif (512 = 50% vs 1024 par défaut) |
| `--pids-limit=100` | Limite le nombre de processus |

---

> [!warning] OOMKilled
> Quand un conteneur dépasse sa limite mémoire, le kernel le tue avec le signal OOMKill. Visible dans `docker inspect` :
> ```bash
> docker inspect mon-app | grep OOMKilled
> # "OOMKilled": true
> ```
