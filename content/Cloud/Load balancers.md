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
aws elbv2 create-load-balancer   --name myapp-alb   --type application   --subnets subnet-abc123 subnet-def456   --security-groups sg-abc123

# Target Group
aws elbv2 create-target-group   --name myapp-tg   --protocol HTTP   --port 8080   --vpc-id vpc-abc123   --health-check-path /health

# Listener
aws elbv2 create-listener   --load-balancer-arn arn:aws:elasticloadbalancing:...   --protocol HTTPS   --port 443   --certificates CertificateArn=arn:aws:acm:...   --default-actions Type=forward,TargetGroupArn=arn:aws:...
```
