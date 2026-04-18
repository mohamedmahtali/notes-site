---
title: Load balancers
tags:
  - intermediate
---
# Load balancers

## Parent
- [[Cloud]]

## Enfants
- [[Layer 4]]
- [[Layer 7]]
- [[Health checks]]

---

## Définition

Un load balancer distribue le trafic réseau entrant entre plusieurs instances backend. Il améliore la disponibilité (si une instance tombe, le trafic est redirigé) et la scalabilité (ajouter des instances pour absorber plus de charge).

---

## Types AWS

| LB | Niveau | Protocoles | Usage |
|---|---|---|---|
| ALB | L7 (HTTP/HTTPS) | HTTP, WebSocket, gRPC | Apps web, microservices |
| NLB | L4 (TCP/UDP) | TCP, UDP, TLS | Haute performance, IP statique |
| CLB | L4/L7 | Legacy | Anciens projets |

---

## Créer un ALB

```bash
# Application Load Balancer
aws elbv2 create-load-balancer \
  --name myapp-alb \
  --type application \
  --subnets subnet-abc123 subnet-def456 \
  --security-groups sg-abc123

# Target Group avec health check
aws elbv2 create-target-group \
  --name myapp-tg \
  --protocol HTTP \
  --port 8080 \
  --vpc-id vpc-abc123 \
  --health-check-path /health \
  --health-check-interval-seconds 30 \
  --healthy-threshold-count 2 \
  --unhealthy-threshold-count 3

# Listener HTTPS avec certificat ACM
aws elbv2 create-listener \
  --load-balancer-arn arn:aws:elasticloadbalancing:... \
  --protocol HTTPS --port 443 \
  --certificates CertificateArn=arn:aws:acm:... \
  --default-actions Type=forward,TargetGroupArn=arn:aws:...

# Redirect HTTP → HTTPS
aws elbv2 create-listener \
  --load-balancer-arn arn:aws:elasticloadbalancing:... \
  --protocol HTTP --port 80 \
  --default-actions Type=redirect,RedirectConfig='{Protocol=HTTPS,Port=443,StatusCode=HTTP_301}'
```

## Routing rules (ALB)

```bash
# Règle : /api/* → target group API, /* → target group frontend
aws elbv2 create-rule \
  --listener-arn arn:aws:elasticloadbalancing:... \
  --priority 10 \
  --conditions '[{"Field":"path-pattern","Values":["/api/*"]}]' \
  --actions '[{"Type":"forward","TargetGroupArn":"arn:aws:...:targetgroup/api-tg/..."}]'
```

## Health check — comportement

```
Instance passe HEALTHY → ajoutée au pool après N succès consécutifs
Instance passe UNHEALTHY → retirée du pool après M échecs consécutifs
                         → nouvelles connexions ne lui sont plus envoyées
                         → connexions en cours sont drainées (deregistration delay)
```

> [!tip] Deregistration delay
> Par défaut 300s (5 min) — le temps que les connexions longues se terminent avant de retirer l'instance. À réduire (ex: 30s) pour les apps stateless avec connexions courtes.
