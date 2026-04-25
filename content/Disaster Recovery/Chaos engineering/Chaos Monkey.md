---
title: Chaos Monkey
tags:
  - reliability
  - advanced
---

# Chaos Monkey

## Définition

Chaos Monkey est l'outil de chaos engineering créé par Netflix. Il termine aléatoirement des instances [[EC2]] en production pour forcer les équipes à construire des [[Services]] résilients capables de survivre à la perte d'instances.

> [!note] La Simian Army
> Netflix a étendu Chaos Monkey en une "Simian Army" : Chaos Gorilla (zone de disponibilité entière), Chaos Kong (région entière), Latency Monkey (latence artificielle), Conformity Monkey (non-conformités)...

## Simuler Chaos Monkey sur Kubernetes

```bash
# Supprimer des pods aléatoirement (simuler Chaos Monkey)
kubectl get pods -n production -o name   | shuf -n 3   | xargs kubectl delete -n production

# Observer l'auto-récupération
watch kubectl get pods -n production
```

## Outils de chaos pour Kubernetes

```bash
# Chaos Mesh (CNCF)
helm install chaos-mesh chaos-mesh/chaos-mesh   --namespace chaos-testing

# Expérience : killer des pods nginx aléatoirement
cat <<EOF | kubectl apply -f -
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: pod-kill-nginx
  namespace: chaos-testing
spec:
  action: pod-kill
  mode: random-max-percent
  value: "30"                 # Tuer 30% des pods
  selector:
    namespaces:
      - production
    labelSelectors:
      app: nginx
  scheduler:
    cron: "@every 10m"        # Toutes les 10 minutes
EOF
```

## Liens

- [[Chaos engineering]]
- [[Failure injection]]
- [[Game days]]
