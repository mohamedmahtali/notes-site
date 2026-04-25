---
title: Virtual machines
tags:
  - beginner
---
# Virtual machines

---

## Définition

Les machines virtuelles [[Cloud]] ([[EC2]]/[[Compute Engine]]/[[Azure]] VMs) sont des serveurs virtuels provisionnés à la demande. Ils émulent du matériel physique via un hyperviseur et offrent une isolation complète entre tenants.

---

## Cycle de vie

```bash
# AWS EC2
aws ec2 run-instances --image-id ami-... --instance-type t3.micro  # launch
aws ec2 stop-instances --instance-ids i-...                        # stop (données conservées)
aws ec2 start-instances --instance-ids i-...                       # start
aws ec2 reboot-instances --instance-ids i-...                      # reboot
aws ec2 terminate-instances --instance-ids i-...                   # destroy

# GCP Compute Engine
gcloud compute instances create my-vm --machine-type=e2-medium
gcloud compute instances stop my-vm
gcloud compute instances start my-vm
gcloud compute instances delete my-vm
```

---

## Méthodes de connexion

```bash
# SSH direct (subnet public)
ssh -i key.pem ec2-user@54.123.45.67

# AWS SSM Session Manager (sans SSH exposé)
aws ssm start-session --target i-1234567890abcdef0

# GCP IAP (Identity-Aware Proxy)
gcloud compute ssh my-vm --tunnel-through-iap
```
