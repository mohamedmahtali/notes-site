---
title: TLS Certificates
tags:
  - security
  - intermediate
---

# TLS Certificates

## Définition

Les certificats TLS sont les certificats X.509 utilisés spécifiquement pour sécuriser les connexions TLS/HTTPS. Ils lient un nom de domaine à une clé publique.

> [!tip] Pourquoi c'est important
> Sans certificat TLS valide, les navigateurs affichent une erreur de sécurité et les utilisateurs ne peuvent pas accéder au service en toute sécurité.

## Types de certificats

| Type | Validation | Usage |
|------|-----------|-------|
| DV (Domain Validated) | Domaine seulement | Sites standards |
| OV (Organization Validated) | Domaine + org | [[Services]] pro |
| EV (Extended Validation) | Audit complet | Banques |
| Wildcard | *.example.com | Multi-sous-domaines |
| Multi-SAN | Plusieurs domaines | Flexibilité |

## Vérifier un certificat TLS

```bash
# Certificat d'un serveur
openssl s_client -connect example.com:443 -showcerts

# Date d'expiration
echo | openssl s_client -connect example.com:443 2>/dev/null \
  | openssl x509 -noout -dates

# Tous les détails (SAN, émetteur, algorithme)
openssl s_client -connect example.com:443 2>/dev/null \
  | openssl x509 -noout -text | grep -E "(Subject|DNS|Issuer|Not)"
```

## cert-manager — gestion automatique dans Kubernetes

cert-manager renouvelle automatiquement les certificats TLS dans K8s (Let's Encrypt, CA interne...).

```bash
# Installer cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
```

```yaml
# ClusterIssuer Let's Encrypt (production)
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
---
# Certificate — demander un cert pour myapp.example.com
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: myapp-tls
  namespace: production
spec:
  secretName: myapp-tls-secret
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  dnsNames:
  - myapp.example.com
  - www.myapp.example.com
```

```bash
# Vérifier l'état du certificat
kubectl get certificate -n production
kubectl describe certificate myapp-tls -n production

# Forcer le renouvellement
kubectl annotate certificate myapp-tls \
  cert-manager.io/issuer-kind=ClusterIssuer \
  --overwrite -n production
```

## Monitoring d'expiration

```bash
# Script de surveillance des certs (alerte si < 30 jours)
for domain in example.com api.example.com; do
  expiry=$(echo | openssl s_client -connect $domain:443 2>/dev/null \
    | openssl x509 -noout -enddate | cut -d= -f2)
  days=$(( ($(date -d "$expiry" +%s) - $(date +%s)) / 86400 ))
  echo "$domain : expire dans $days jours ($expiry)"
done
```

## Liens

- [[TLS]]
- [[Handshake]]
- [[Mutual TLS]]
- [[Certificates]]
