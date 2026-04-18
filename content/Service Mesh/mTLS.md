---
title: mTLS (Mutual TLS)
tags: [security, networking, advanced]
---

# mTLS (Mutual TLS)

## Définition

mTLS (Mutual TLS) est une extension de TLS où **les deux parties** (client et serveur) s'authentifient mutuellement via des certificats. Contrairement au TLS standard (seul le serveur présente un certificat), mTLS garantit l'identité des deux côtés.

> [!tip] mTLS en service mesh
> Dans Istio ou Linkerd, mTLS est activé automatiquement entre tous les sidecars. Chaque pod reçoit un certificat SPIFFE (basé sur son ServiceAccount K8s). Aucun changement de code n'est nécessaire.

## TLS standard vs mTLS

```
TLS standard :
Client ──────── "Qui es-tu ?" ──────→ Serveur
Client ←─── "Je suis server.com" ──── Serveur
Client ──── trafic chiffré ──────────→ Serveur

mTLS :
Client ──── "Qui es-tu ?" ───────────→ Serveur
Client ←─── "Je suis server.com" ───── Serveur
Client ──── "Et moi je suis client" ──→ Serveur
Client ────── trafic chiffré ──────────→ Serveur
```

## SPIFFE — identité des workloads

Istio et Linkerd utilisent le standard **SPIFFE** (Secure Production Identity Framework For Everyone) pour identifier les services.

```
Format SPIFFE URI : spiffe://<trust-domain>/<path>
Exemple : spiffe://cluster.local/ns/production/sa/payment-service
```

Chaque pod reçoit un certificat X.509 signé par la CA du mesh, avec comme identité son SPIFFE URI.

## Configuration Istio

```yaml
# Activer mTLS STRICT sur tout le namespace "production"
# (rejette tout trafic non-mTLS)
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT
```

```yaml
# Mode PERMISSIVE — accepte mTLS et trafic en clair (migration progressive)
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: PERMISSIVE
```

```yaml
# AuthorizationPolicy — seul payment-service peut appeler order-service
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-payment-only
  namespace: production
spec:
  selector:
    matchLabels:
      app: order-service
  rules:
  - from:
    - source:
        principals:
          - "cluster.local/ns/production/sa/payment-service"
```

## Vérifier mTLS avec Istio

```bash
# Voir le statut mTLS de tous les services
istioctl x describe service payment-service.production

# Analyser la config d'un pod
istioctl x describe pod payment-service-xxx

# Dashboard Kiali — visualisation du mesh et du statut mTLS
istioctl dashboard kiali
```

> [!warning] mTLS STRICT vs PERMISSIVE
> Commencer toujours en mode **PERMISSIVE** lors de la migration. Passer en **STRICT** seulement après avoir vérifié que tout le trafic passe bien par le mesh (via Kiali ou les métriques Envoy).

## Liens

- [[Service Mesh]]
- [[Istio]]
- [[TLS]]
