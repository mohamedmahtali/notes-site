---
title: Chaos engineering
tags:
  - reliability
  - advanced
---

# Chaos engineering

## Définition

Le chaos engineering est la pratique d'injecter intentionnellement des défaillances dans un système en production (ou [[Staging]]) pour tester sa résilience et identifier les faiblesses avant qu'un incident réel ne les révèle.

> [!tip] Principe fondateur
> "La meilleure façon de tester la résilience d'un système est de le casser intentionnellement dans un environnement contrôlé." — Netflix, créateurs de Chaos Monkey (2010).

## Principes du chaos engineering

```
1. Définir l'état stable du système (métriques de référence)
2. Formuler l'hypothèse : "Si X tombe, le système reste stable"
3. Injecter la défaillance (petit périmètre d'abord)
4. Observer et mesurer l'impact
5. Corriger les faiblesses trouvées
6. Répéter (augmenter progressivement la portée)
```

## Types de défaillances à injecter

| Catégorie | Exemples |
|-----------|---------|
| **Réseau** | Latence artificielle, perte de paquets, partition réseau |
| **Ressources** | CPU spike, memory pressure, disk full |
| **Processus** | Kill aléatoire de [[Pods]]/[[Containers]], [[restart]] |
| **Infrastructure** | Arrêt d'une VM, d'une AZ entière |
| **Application** | Injection d'erreurs HTTP 500, timeouts |

## Chaos Mesh — injection sur Kubernetes

```yaml
# Tuer 30% des pods d'un déploiement aléatoirement
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: kill-pods
  namespace: production
spec:
  action: pod-kill
  mode: fixed-percent
  value: "30"
  selector:
    namespaces:
      - production
    labelSelectors:
      app: myapp
  scheduler:
    cron: "@every 10m"
```

```yaml
# Injecter 200ms de latence réseau sur un service
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-latency
spec:
  action: delay
  mode: all
  selector:
    namespaces: [production]
    labelSelectors:
      app: payment-service
  delay:
    latency: "200ms"
    jitter: "50ms"
  duration: "5m"
```

## Checklist avant un test de chaos

- [ ] Alertes [[Prometheus]]/[[Grafana]] actives et vérifiées
- [ ] Runbook de [[Rollback]] prêt
- [ ] Équipe on-call notifiée
- [ ] Fenêtre de maintenance hors heures de pointe
- [ ] Démarrer en staging avant production
- [ ] Périmètre limité (1 service, 1 région)

> [!danger] Chaos en production
> Toujours commencer par du chaos contrôlé en staging. En production, utiliser des Game Days planifiés avec toute l'équipe disponible.

## Liens

- [[Chaos Monkey]]
- [[Failure injection]]
- [[Game days]]
- [[Disaster Recovery]]
