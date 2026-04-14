---
title: Host
tags:
  - intermediate
---

# Host

## Parent
- [[Docker networks]]

---

## Définition

Avec le driver `host`, le conteneur partage directement l'interface réseau de l'hôte. Il n'y a pas d'isolation réseau — le conteneur voit et utilise les ports de l'hôte directement. Pas de NAT, pas de port mapping nécessaire.

---

## Commandes

```bash
# Lancer avec le réseau host
docker run -d --network host nginx
# → nginx écoute sur le port 80 de l'hôte directement

# Pas besoin de -p
docker run --network host mon-app
```

---

## Avantages et limitations

| Critère | Host network | Bridge |
|---|---|---|
| Performance réseau | ✅ Maximale (pas de NAT) | Overhead NAT |
| Isolation | ❌ Aucune | ✅ Isolé |
| Port mapping | Non nécessaire | Requis |
| Disponible sur | Linux uniquement | Tous OS |

---

## Cas d'usage

> [!tip] Quand utiliser host networking
> - Services nécessitant des performances réseau maximales (monitoring, proxies)
> - Conteneurs qui doivent écouter sur de nombreux ports dynamiques
> - Applications de monitoring réseau (Prometheus node_exporter)

> [!warning]
> Le mode host n'est disponible que sur Linux. Sur macOS/Windows avec Docker Desktop, le comportement est émulé et n'offre pas les mêmes performances.
