---
title: Outbound rules
tags:
  - beginner
---
# Outbound rules

## Parent
- [[Security groups]]

---

## Définition

Les règles outbound contrôlent le trafic sortant d'une instance vers d'autres destinations. Par défaut, tout le trafic sortant est autorisé — restreindre si la sécurité l'exige.

---

## Règles outbound restrictives

```bash
# Supprimer la règle "allow all" par défaut
aws ec2 revoke-security-group-egress   --group-id sg-abc123   --protocol -1   --cidr 0.0.0.0/0

# Autoriser seulement HTTPS sortant
aws ec2 authorize-security-group-egress   --group-id sg-abc123   --protocol tcp   --port 443   --cidr 0.0.0.0/0

# Autoriser DNS
aws ec2 authorize-security-group-egress   --group-id sg-abc123   --protocol udp   --port 53   --cidr 0.0.0.0/0
```

---

> [!note]
> Restreindre les règles outbound est une pratique de sécurité avancée (defense in depth). Pour la plupart des workloads, laisser les règles outbound par défaut (tout autorisé) est acceptable — la valeur est dans les règles inbound.
