---
title: Compute Engine
tags:
  - intermediate
---
# Compute Engine

---

## Définition

Google Compute Engine est le service de VMs de GCP, équivalent [[EC2]]. Il propose des machine [[Types]] variés, des instances Spot (preemptible), et une intégration native avec les autres [[Services]] GCP.

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
# Instances Spot — 60-91% moins chères, peuvent être stoppées par GCP
gcloud compute instances create my-spot-vm \
  --provisioning-model=SPOT \
  --instance-termination-action=STOP \
  --machine-type=n2-standard-4
```

## Startup script — configurer au démarrage

```bash
# Passer un script exécuté au premier démarrage
gcloud compute instances create my-vm \
  --machine-type=e2-medium \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --zone=europe-west1-b \
  --metadata-from-file startup-script=./startup.sh

# startup.sh
#!/bin/bash
apt-get update -y
apt-get install -y nginx
systemctl enable --now nginx
```

## Managed Instance Groups (MIG) — autoscaling

```bash
# Créer un instance template
gcloud compute instance-templates create myapp-template \
  --machine-type=e2-standard-2 \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --tags=http-server \
  --metadata-from-file startup-script=./startup.sh

# Créer un MIG avec autoscaling
gcloud compute instance-groups managed create myapp-mig \
  --template=myapp-template \
  --size=2 \
  --zone=europe-west1-b

# Activer l'autoscaling (2-10 instances selon CPU)
gcloud compute instance-groups managed set-autoscaling myapp-mig \
  --zone=europe-west1-b \
  --min-num-replicas=2 \
  --max-num-replicas=10 \
  --target-cpu-utilization=0.7
```

## Connexion sans SSH exposé (Identity-Aware Proxy)

```bash
# Connexion via IAP — pas besoin d'IP publique ni de port 22 ouvert
gcloud compute ssh my-vm \
  --tunnel-through-iap \
  --zone=europe-west1-b

# Transférer un fichier via IAP
gcloud compute scp ./app.tar.gz my-vm:~ \
  --tunnel-through-iap \
  --zone=europe-west1-b
```

> [!tip] IAP + [[VPC]] privé = zéro surface d'attaque
> Avec IAP, les VMs n'ont pas besoin d'IP publique. Tout accès [[SSH]] est authentifié via Google Identity et audité dans [[Cloud]] [[Audit logs]].
