---
title: Vertical scaling
tags:
  - beginner
---
# Vertical scaling

## Parent
- [[Autoscaling]]

---

## Définition

Le scaling vertical (scale up/down) change le type d'instance pour une instance plus ou moins puissante. Nécessite généralement un redémarrage. Limité par les tailles d'instances disponibles.

---

## Quand utiliser

- Bases de données (souvent difficiles à scaler horizontalement)
- Applications legacy non-distribuées
- Workloads avec état qui ne peuvent pas être facilement répliqués

---

```bash
# AWS — redimensionner une instance EC2
# 1. Arrêter l'instance
aws ec2 stop-instances --instance-ids i-abc123

# 2. Changer le type
aws ec2 modify-instance-attribute   --instance-id i-abc123   --instance-type '{"Value":"m5.xlarge"}'

# 3. Redémarrer
aws ec2 start-instances --instance-ids i-abc123

# RDS — scaling vertical sans interruption (quelques minutes)
aws rds modify-db-instance   --db-instance-identifier mydb   --db-instance-class db.r5.xlarge   --apply-immediately
```

---

> [!tip]
> Pour RDS, le scaling vertical est l'approche principale. Un Multi-AZ RDS effectue le resize avec failover automatique — downtime de ~1-2 minutes.
