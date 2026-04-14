---
title: Ingress controller
tags:
  - intermediate
---
# Ingress controller

## Parent
- [[Ingress]]

---

## Définition

L'Ingress controller est le composant qui implémente les règles définies dans les objets Ingress. Kubernetes fournit l'API Ingress, mais c'est le controller qui fait réellement le proxy, la terminaison TLS et le routing.

---

## Controllers populaires

| Controller | Points forts |
|---|---|
| nginx-ingress (officiel K8s) | Standard, stable, bien documenté |
| ingress-nginx (community) | Le plus répandu |
| Traefik | Auto-discovery, dashboard, Let's Encrypt natif |
| HAProxy Ingress | Hautes performances |
| AWS ALB Controller | Intégration native AWS |
| Istio Gateway | Service mesh complet |

---

## Installation nginx-ingress

```bash
# Helm
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx   --namespace ingress-nginx --create-namespace

# Voir le pod et le LoadBalancer créé
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

---

## Annotations courantes

```yaml
metadata:
  annotations:
    # Rate limiting
    nginx.ingress.kubernetes.io/limit-rps: "10"
    # Timeout
    nginx.ingress.kubernetes.io/proxy-read-timeout: "60"
    # HTTPS redirect
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    # Basic auth
    nginx.ingress.kubernetes.io/auth-type: basic
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
```

---

> [!tip]
> Sur un cloud provider, l'Ingress controller crée automatiquement un LoadBalancer cloud avec l'IP externe. Sur bare-metal, utiliser MetalLB pour obtenir une IP externe.
