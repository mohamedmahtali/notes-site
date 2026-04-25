---
title: Boot disks
tags:
  - intermediate
---
# Boot disks

---

## Définition

Le boot disk est le disque principal d'une VM contenant l'OS et les applications. Sur [[AWS]] c'est un EBS volume ; sur GCP c'est un Persistent Disk. Sa taille, son type (SSD/HDD), et ses performances ont un impact direct sur le démarrage et les I/O.

---

## Types de disques AWS EBS

| Type | IOPS | Latence | Usage |
|---|---|---|---|
| gp3 | 3000-16000 | ms | Usage général (recommandé) |
| io2 | jusqu'à 64000 | <1ms | BDD haute performance |
| st1 | 500 | ms | Big data, logs séquentiels |
| sc1 | 250 | ms | Archives froides |

---

## Configuration

```bash
# Lancer une instance avec un boot disk gp3 de 50GB
aws ec2 run-instances   --image-id ami-0c55b159cbfafe1f0   --instance-type t3.medium   --block-device-mappings '[{
    "DeviceName": "/dev/sda1",
    "Ebs": {
      "VolumeSize": 50,
      "VolumeType": "gp3",
      "Iops": 3000,
      "Throughput": 125,
      "DeleteOnTermination": true,
      "Encrypted": true
    }
  }]'
```

---

> [!tip]
> Toujours chiffrer les boot disks (`Encrypted: true`) pour les workloads de production. Sur AWS, utiliser gp3 plutôt que gp2 — même prix, meilleures performances de base.
