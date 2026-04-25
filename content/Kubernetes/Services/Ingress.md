---
title: Ingress
tags:
  - intermediate
---
# Ingress

---

## Définition

Un Ingress est un objet [[Kubernetes]] qui gère l'accès HTTP/HTTPS externe à des [[Services]] dans le [[Cluster]]. Il permet le [[Routing]] basé sur les paths et les hostnames, la terminaison [[TLS]], et le virtual hosting — le tout via un seul load balancer.

---

## Pourquoi Ingress plutôt que LoadBalancer

```
Sans Ingress : 5 services → 5 load balancers cloud → 5 IPs publiques → $$$
Avec Ingress : 5 services → 1 load balancer → routing par hostname/path → $
```

---

## Manifeste

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.com
    secretName: myapp-tls
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
  - host: admin.myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin
            port:
              number: 80
```

---

> [!note]
> L'Ingress nécessite un [[Ingress controller]] installé dans le cluster ([[Nginx]]-ingress, [[Traefik]], etc.) — sans lui, l'objet Ingress est ignoré.
