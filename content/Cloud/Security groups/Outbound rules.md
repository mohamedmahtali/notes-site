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

## Règles outbound typiques par cas d'usage

```bash
# Serveur applicatif — accès minimal nécessaire
# (base de données, HTTPS externe, DNS)

# Vers la base de données interne
aws ec2 authorize-security-group-egress \
  --group-id sg-app \
  --protocol tcp --port 5432 \
  --destination-group sg-db

# HTTPS vers internet (APIs externes, mises à jour)
aws ec2 authorize-security-group-egress \
  --group-id sg-app \
  --protocol tcp --port 443 --cidr 0.0.0.0/0

# DNS (résolution de noms)
aws ec2 authorize-security-group-egress \
  --group-id sg-app \
  --protocol udp --port 53 --cidr 0.0.0.0/0
```

## Quand restreindre les règles outbound

| Contexte | Recommandation |
|----------|---------------|
| Workload standard | Laisser "tout autorisé" (valeur dans l'inbound) |
| Traitement de données sensibles | Restreindre — éviter l'exfiltration |
| Compliance (PCI-DSS, SOC2) | Souvent obligatoire de restreindre |
| Instances dans subnet privé | Gérer via NAT Gateway + VPC Endpoints |

> [!note]
> Restreindre les règles outbound est une pratique de sécurité avancée (defense in depth). Pour la plupart des workloads, laisser les règles outbound par défaut (tout autorisé) est acceptable — la valeur est dans les règles inbound.
