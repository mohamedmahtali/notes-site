---
title: Failure injection
tags: [reliability, advanced]
---

# Failure injection

## Définition

La failure injection (injection de pannes) est la technique consistant à introduire délibérément des défaillances dans un système : latence réseau, erreurs CPU, perte de paquets, remplissage du disque. Elle teste la résilience du système face à des conditions dégradées.

> [!tip] Différence avec Chaos Monkey
> Chaos Monkey tue des instances. La failure injection est plus fine : elle simule une dégradation partielle (latence de 500ms, 5% de perte de paquets) plutôt qu'une panne totale.

## Types de pannes à injecter

| Catégorie | Exemples |
|-----------|---------|
| Réseau | Latence, perte de paquets, partition réseau |
| CPU | Saturation CPU à 100% |
| Mémoire | OOM (Out of Memory) |
| Disque | Disque plein, I/O lent |
| Dépendances | Base de données lente, API externe down |
| Processus | Kill du processus applicatif |

## Avec tc (Linux traffic control)

```bash
# Ajouter 500ms de latence sur eth0
tc qdisc add dev eth0 root netem delay 500ms

# Ajouter 20% de perte de paquets
tc qdisc add dev eth0 root netem loss 20%

# Simuler une connexion dégradée (latence + perte)
tc qdisc add dev eth0 root netem delay 200ms loss 5%

# Supprimer la règle
tc qdisc del dev eth0 root
```

## Avec Chaos Mesh (Kubernetes)

```yaml
# Injection de latence réseau sur un service
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-delay
spec:
  action: delay
  mode: all
  selector:
    namespaces:
      - production
    labelSelectors:
      app: payment-service
  delay:
    latency: "300ms"
    jitter: "50ms"
  duration: "10m"
```

## Liens

- [[Chaos engineering]]
- [[Chaos Monkey]]
- [[Game days]]
