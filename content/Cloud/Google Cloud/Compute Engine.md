---
title: Compute Engine
tags:
  - intermediate
---
# Compute Engine

## Parent
- [[Google Cloud]]

---

## Définition

Google Compute Engine est le service de VMs de GCP, équivalent EC2. Il propose des machine types variés, des instances Spot (preemptible), et une intégration native avec les autres services GCP.

---

## Commandes essentielles

```bash
# Créer une VM
gcloud compute instances create my-vm   --machine-type=e2-medium   --image-family=ubuntu-2204-lts   --image-project=ubuntu-os-cloud   --zone=europe-west1-b   --tags=http-server,https-server   --boot-disk-size=50GB   --boot-disk-type=pd-ssd

# Lister les instances
gcloud compute instances list

# Se connecter (sans SSH exposé via IAP)
gcloud compute ssh my-vm --tunnel-through-iap --zone=europe-west1-b

# Démarrer/arrêter
gcloud compute instances stop my-vm --zone=europe-west1-b
gcloud compute instances start my-vm --zone=europe-west1-b

# Supprimer
gcloud compute instances delete my-vm --zone=europe-west1-b
```

---

## Spot VMs (Preemptible)

```bash
# Instances Spot — 60-91% moins chères
gcloud compute instances create my-spot-vm   --provisioning-model=SPOT   --instance-termination-action=STOP   --machine-type=n2-standard-4
```
