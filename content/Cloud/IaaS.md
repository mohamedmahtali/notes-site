---
title: IaaS
tags:
  - beginner
---
# IaaS

## Parent
- [[Cloud]]

---

## Définition

Infrastructure as a Service : le provider fournit les ressources informatiques virtualisées (VMs, réseau, stockage). Tu gères l'OS, le runtime, les applications, et les données. Tu as le contrôle maximum.

---

## Exemples IaaS

| Provider | Service |
|---|---|
| AWS | EC2, EBS, VPC |
| GCP | Compute Engine, Persistent Disk, VPC |
| Azure | Virtual Machines, Managed Disks, VNet |

---

## Quand utiliser IaaS

- Contrôle total de l'OS et des configurations système
- Workloads legacy qui ne peuvent pas être containerisés
- Besoin de configurations réseau spécifiques
- Conformité qui exige un contrôle complet

---

## Exemple

```bash
# Lancer une VM EC2 (IaaS)
aws ec2 run-instances   --image-id ami-0c55b159cbfafe1f0 \   # Ubuntu 22.04
  --instance-type t3.medium   --key-name my-keypair   --security-group-ids sg-abc123   --subnet-id subnet-def456   --count 1

# Connexion SSH (tu gères l'OS)
ssh -i my-keypair.pem ubuntu@54.123.45.67
sudo apt update && sudo apt upgrade -y
```

---

> [!note]
> Avec IaaS, tu es responsable de patcher l'OS, configurer le firewall, gérer les utilisateurs, etc. Pour moins de gestion, envisager PaaS ou containers.
