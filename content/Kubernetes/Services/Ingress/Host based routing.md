---
title: Host based routing
tags:
  - intermediate
---
# Host based routing

## Parent
- [[Ingress]]

---

## Définition

Le host-based routing (virtual hosting) dirige les requêtes vers des services différents selon le hostname HTTP. `api.myapp.com` → service API, `admin.myapp.com` → service admin, `myapp.com` → frontend.

---

## Configuration

```yaml
spec:
  tls:
  - hosts: [api.myapp.com, admin.myapp.com, myapp.com]
    secretName: myapp-wildcard-tls

  rules:
  - host: api.myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80

  - host: admin.myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin-service
            port:
              number: 80

  - host: myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
```

---

## Wildcard

```yaml
# Wildcard — tous les sous-domaines
- host: "*.myapp.com"
  http:
    paths:
    - path: /
      pathType: Prefix
      backend:
        service:
          name: wildcard-handler
          port:
            number: 80
```

---

> [!tip]
> Combiner host-based et path-based routing sur le même Ingress pour une architecture propre : un seul point d'entrée gère tous les services frontend, API, et admin.
