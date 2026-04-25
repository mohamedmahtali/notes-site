---
title: EC2
tags:
  - intermediate
---
# EC2

---

## Définition

Amazon EC2 (Elastic Compute [[Cloud]]) fournit des machines virtuelles redimensionnables dans le cloud [[AWS]]. Chaque instance tourne sur un hyperviseur Xen ou Nitro avec des caractéristiques configurables (CPU, RAM, réseau, stockage).

---

## Familles d'instances

| Famille | Optimisation | Exemple | Usage |
|---|---|---|---|
| t3/t4g | Usage général (burstable) | t3.micro | Dev, sites web |
| m5/m6 | Usage général | m5.large | Apps générales |
| c5/c6 | Compute-optimized | c5.xlarge | Batch, HPC |
| r5/r6 | Memory-optimized | r5.xlarge | BDD en mémoire |
| p3/p4 | GPU | p3.2xlarge | ML, rendu |

---

## Commandes essentielles

```bash
# Lancer une instance
aws ec2 run-instances   --image-id ami-0c55b159cbfafe1f0   --instance-type t3.micro   --key-name my-key   --security-group-ids sg-abc123   --subnet-id subnet-def456

# Lister les instances
aws ec2 describe-instances   --query 'Reservations[*].Instances[*].[InstanceId,State.Name,PublicIpAddress]'   --output table

# Démarrer/arrêter
aws ec2 start-instances --instance-ids i-1234567890abcdef0
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

---

> [!tip]
> Toujours utiliser des instances Spot pour les workloads tolérants aux interruptions (batch, CI/CD [[Runners]], dev) — jusqu'à 90% moins cher que les instances On-Demand.
