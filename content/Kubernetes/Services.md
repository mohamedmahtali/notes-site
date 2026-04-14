---
title: Services
tags:
  - beginner
---
# Services

## Parent
- [[Kubernetes]]

## Enfants
- [[ClusterIP]]
- [[NodePort]]
- [[LoadBalancer]]
- [[Ingress]]

---

## Définition

Un Service Kubernetes expose un ensemble de pods sous une adresse IP stable et un nom DNS. Les pods étant éphémères (IPs qui changent), les Services fournissent une abstraction réseau stable qui fait du load balancing vers les pods correspondants.

---

## Pourquoi c'est important

> [!tip] L'abstraction réseau de Kubernetes
> Sans Services, impossible de communiquer de façon fiable avec des pods — leurs IPs changent à chaque recréation. Le Service est l'adresse stable que les autres composants utilisent.

---

## Types de Services

| Type | Accessibilité | Usage |
|---|---|---|
| ClusterIP | Interne cluster | Communication inter-services |
| NodePort | Externe via port node | Dev/test |
| LoadBalancer | Externe via LB cloud | Production (cloud) |
| ExternalName | Alias DNS externe | Intégrer des services externes |

---

## Manifeste basique

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp          # cible les pods avec ce label
  ports:
  - port: 80            # port du Service
    targetPort: 8080    # port du container
  type: ClusterIP       # défaut
```

---

## Commandes

```bash
kubectl get services
kubectl get svc
kubectl describe svc myapp

# Tester un service depuis un pod
kubectl run test --image=busybox --rm -it -- wget -qO- http://myapp/health
```

---

> [!note]
> Voir [[Ingress]] pour exposer plusieurs services HTTP/HTTPS via un seul point d'entrée avec routing par path/hostname.
