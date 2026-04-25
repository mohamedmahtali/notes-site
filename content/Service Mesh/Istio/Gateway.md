---
title: Gateway (Istio)
tags:
  - kubernetes
  - networking
  - advanced
---

# Gateway (Istio)

## Définition

Une `Gateway` Istio configure le **point d'entrée du trafic externe** dans le mesh. Elle s'exécute sur l'Istio [[Ingress]] Gateway (un pod Envoy dédié) et remplace l'[[Ingress controller]] [[Kubernetes]] pour les architectures [[Service Mesh]].

> [!note] Gateway vs Ingress K8s
> L'Ingress Kubernetes route le trafic mais ne comprend pas le mesh. La Gateway Istio s'intègre nativement avec les VirtualServices, supportant [[TLS]], mTLS, SNI, et des règles avancées qu'un Ingress standard ne peut pas exprimer.

## Architecture

```
Internet
    │
    ▼
Istio Ingress Gateway (pod Envoy)
    │  ← configuré par Gateway + VirtualService
    ▼
Services dans le mesh
```

## Configuration basique (HTTP)

```yaml
# Gateway — écoute sur le port 80
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: my-gateway
  namespace: production
spec:
  selector:
    istio: ingressgateway      # Label de l'Istio Ingress Gateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "myapp.example.com"
---
# VirtualService — associé à la Gateway
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp
  namespace: production
spec:
  hosts:
  - "myapp.example.com"
  gateways:
  - my-gateway
  http:
  - route:
    - destination:
        host: myapp
        port:
          number: 8080
```

## TLS termination

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: my-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  # Redirect HTTP → HTTPS
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "myapp.example.com"
    tls:
      httpsRedirect: true
  # HTTPS avec terminaison TLS
  - port:
      number: 443
      name: https
      protocol: HTTPS
    hosts:
    - "myapp.example.com"
    tls:
      mode: SIMPLE
      credentialName: myapp-tls    # Nom du Secret K8s contenant le cert
```

```bash
# Créer le secret TLS dans le namespace istio-system
kubectl create secret tls myapp-tls \
  --cert=cert.pem \
  --key=key.pem \
  -n istio-system
```

## Obtenir l'IP de l'Ingress Gateway

```bash
# Récupérer l'IP externe
kubectl get svc istio-ingressgateway -n istio-system

export INGRESS_IP=$(kubectl get svc istio-ingressgateway \
  -n istio-system \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

# Tester
curl -H "Host: myapp.example.com" http://$INGRESS_IP/
```

## Liens

- [[Istio]]
- [[VirtualService]]
- [[DestinationRule]]
- [[mTLS]]
