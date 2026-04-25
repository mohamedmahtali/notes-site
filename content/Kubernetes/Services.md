---
title: Services
tags:
  - beginner
---
# Services

---

## Définition

Un Service [[Kubernetes]] [[EXPOSE]] un ensemble de [[Pods]] sous une adresse IP stable et un nom [[DNS]]. Les pods étant éphémères (IPs qui changent), les Services fournissent une abstraction réseau stable qui fait du [[Load balancing]] vers les pods correspondants.

---

## Pourquoi c'est important

> [!tip] L'abstraction réseau de Kubernetes
> Sans Services, impossible de communiquer de façon fiable avec des pods — leurs IPs changent à chaque recréation. Le Service est l'adresse stable que les autres composants utilisent.

---

## Types de Services

| Type | Accessibilité | Usage |
|---|---|---|
| [[ClusterIP]] | Interne [[Cluster]] | Communication inter-services |
| [[NodePort]] | Externe via port [[Node]] | Dev/test |
| [[LoadBalancer]] | Externe via LB [[Cloud]] | Production (cloud) |
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
> Voir [[Ingress]] pour exposer plusieurs services HTTP/HTTPS via un seul point d'entrée avec [[Routing]] par path/hostname.
