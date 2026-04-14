---
title: Container logs
tags:
  - beginner
---

# Container logs

## Parent
- [[Containers]]

---

## Définition

Docker capture automatiquement la sortie standard (`stdout`) et l'erreur standard (`stderr`) de chaque conteneur. `docker logs` permet d'inspecter ces logs. Les logs sont par défaut stockés en JSON sur le filesystem de l'hôte.

---

## Commandes

```bash
# Voir tous les logs
docker logs mon-app

# Suivre en temps réel
docker logs -f mon-app

# Dernières N lignes
docker logs --tail 100 mon-app

# Avec timestamps
docker logs -t mon-app

# Depuis un moment précis
docker logs --since 1h mon-app
docker logs --since 2024-01-15T10:00:00 mon-app

# Combiner les options
docker logs -f --tail 50 mon-app
```

---

## Log drivers

```bash
# Voir le log driver configuré
docker info | grep "Logging Driver"

# Changer le log driver au run
docker run --log-driver=journald mon-app
docker run --log-driver=fluentd mon-app
docker run --log-driver=awslogs mon-app
```

| Driver | Usage |
|---|---|
| `json-file` (défaut) | Fichiers JSON sur l'hôte |
| `journald` | Systemd journal |
| `fluentd` | Centralisation Fluentd |
| `awslogs` | CloudWatch Logs |
| `none` | Désactiver les logs |

---

> [!tip] En production
> Configurer un log driver centralisé (ELK, CloudWatch, Loki) plutôt que de lire les logs par `docker logs` sur chaque hôte.
