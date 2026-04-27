---
title: EC2
tags:
  - intermediate
---
# EC2

## Définition

Amazon EC2 (Elastic Compute Cloud) fournit des machines virtuelles redimensionnables dans le cloud [[AWS]]. Chaque instance tourne sur un hyperviseur Xen ou Nitro avec des caractéristiques configurables (CPU, RAM, réseau, stockage).

## Familles d'instances

| Famille | Optimisation | Exemple | Usage |
|---|---|---|---|
| t3/t4g | Usage général burstable | t3.micro | Dev, tests, sites web |
| m5/m6i | Usage général | m5.large | Apps générales |
| c5/c6i | Compute-optimized | c5.xlarge | Batch, HPC, CI/CD |
| r5/r6i | Memory-optimized | r5.xlarge | BDD en mémoire, Redis |
| p3/p4d | GPU | p3.2xlarge | ML, rendu 3D |
| i3/i4i | Storage-optimized | i3.xlarge | Bases de données hautes perf |

## Modèles de prix

```
On-Demand  — tarif à la seconde, aucun engagement
Reserved   — engagement 1 ou 3 ans, -40 à -60%
Spot       — capacité excédentaire AWS, -70 à -90% (peut être interrompu)
Savings Plans — engagement usage horaire, flexible sur la famille

Règle : prod stable → Reserved | CI/CD/batch → Spot | reste → On-Demand
```

## Stockage attaché

| Type | Caractéristiques | Usage |
|------|-----------------|-------|
| EBS gp3 | SSD généraliste, 16 000 IOPS max | Root volume, apps |
| EBS io2 | SSD haute perf, 64 000 IOPS | BDD critiques |
| EBS st1 | HDD séquentiel | Data warehousing, Hadoop |
| Instance Store | Stockage éphémère sur l'hôte | Cache, scratch |

> [!warning] Instance Store
> Le stockage Instance Store est perdu si l'instance est stoppée ou terminée. Toujours utiliser EBS pour les données persistantes.

## Cycle de vie d'une instance

```bash
# Lancer une instance (avec User Data pour init automatique)
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.micro \
  --key-name my-keypair \
  --security-group-ids sg-abc123 \
  --subnet-id subnet-def456 \
  --user-data file://init-script.sh \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=web-1}]'

# Lister les instances running
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,PublicIpAddress,Tags[0].Value]' \
  --output table

# Démarrer / Arrêter / Terminer
aws ec2 start-instances --instance-ids i-1234567890abcdef0
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

## User Data — initialisation automatique

Le User Data est un script exécuté au premier démarrage de l'instance (cloud-init).

```bash
#!/bin/bash
# Exemple : installer nginx automatiquement
yum update -y
yum install -y nginx
systemctl enable --now nginx
echo "<h1>Instance $(hostname)</h1>" > /usr/share/nginx/html/index.html
```

## Connexion SSH

```bash
# Connexion standard
ssh -i ~/.ssh/my-keypair.pem ec2-user@<public-ip>

# Via AWS SSM Session Manager (sans port 22 ouvert)
aws ssm start-session --target i-1234567890abcdef0
```

Préférer SSM Session Manager en production : pas besoin d'ouvrir le port 22, logs de session automatiques dans CloudWatch.

## Instances Spot — utilisation optimale

```bash
# Vérifier le prix Spot actuel
aws ec2 describe-spot-price-history \
  --instance-types c5.xlarge \
  --product-descriptions "Linux/UNIX" \
  --max-items 5

# Lancer une instance Spot
aws ec2 run-instances \
  --instance-type c5.xlarge \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-market-options '{"MarketType":"spot","SpotOptions":{"MaxPrice":"0.10"}}'
```

## Explorer

- **[[AWS]]** — services AWS dans leur ensemble, IAM, VPC
- **[[VPC]]** — réseau dans lequel tourne EC2, security groups, subnets
- **[[IAM]]** — Instance Profiles (roles attachés aux instances EC2)
- **[[Object storage]]** — S3 pour le stockage objets (différent d'EBS)
