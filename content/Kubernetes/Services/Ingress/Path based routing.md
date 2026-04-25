---
title: Path based routing
tags:
  - intermediate
---
# Path based routing

---

## Définition

Le path-based [[Routing]] dans un [[Ingress]] dirige les requêtes HTTP vers des [[Services]] différents selon le chemin URL. `/api/*` → service API, `/` → frontend, `/admin/*` → service admin.

---

## Configuration

```yaml
spec:
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /api
        pathType: Prefix          # /api, /api/users, /api/v2
        backend:
          service:
            name: api-service
            port:
              number: 80
      - path: /static
        pathType: Prefix
        backend:
          service:
            name: static-assets
            port:
              number: 80
      - path: /
        pathType: Prefix          # catch-all — doit être en dernier
        backend:
          service:
            name: frontend
            port:
              number: 80
```

---

## PathTypes

| PathType | Comportement |
|---|---|
| `Prefix` | Match sur le préfixe du chemin (`/api` match `/api/users`) |
| `Exact` | Match exact uniquement (`/api` ne match pas `/api/users`) |
| `ImplementationSpecific` | Comportement défini par le controller |

---

## Rewrite

```yaml
# Enlever le préfixe /api avant de passer au service
annotations:
  nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
  - http:
      paths:
      - path: /api(/|$)(.*)
        pathType: ImplementationSpecific
        backend:
          service:
            name: api-service
            port:
              number: 80
```
