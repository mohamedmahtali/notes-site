---
title: Layer 4
tags:
  - intermediate
---
# Layer 4

## Parent
- [[Load balancers]]

---

## Définition

Un load balancer Layer 4 (transport) route le trafic basé sur les adresses IP et les ports TCP/UDP, sans inspecter le contenu des paquets. Plus rapide qu'un L7 LB car pas de déchiffrement/réassemblage des paquets.

---

## Quand utiliser L4

- Haute performance (millions de connexions)
- Protocoles non-HTTP (MQTT, gRPC raw, gaming)
- IP statique requise (NLB AWS a des IPs statics)
- Latence ultra-faible

---

## AWS NLB

```bash
aws elbv2 create-load-balancer   --name myapp-nlb   --type network   --subnets subnet-abc123 subnet-def456

# NLB Target Group TCP
aws elbv2 create-target-group   --name myapp-nlb-tg   --protocol TCP   --port 443   --vpc-id vpc-abc123   --target-type instance

# Health check TCP simple
aws elbv2 modify-target-group   --target-group-arn arn:aws:...   --health-check-protocol TCP
```

---

> [!note]
> Le NLB préserve l'IP source du client (pas besoin de X-Forwarded-For). L'ALB (L7) masque l'IP source — l'application reçoit l'IP du LB, pas du client.
