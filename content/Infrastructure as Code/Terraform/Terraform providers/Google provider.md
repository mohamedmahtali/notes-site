---
title: Google provider
tags:
  - intermediate
---
# Google provider

## Parent
- [[Terraform providers]]

---

## Définition

Le provider Google (hashicorp/google) gère les ressources GCP. Il supporte l'authentification via Service Account, Application Default Credentials, ou Workload Identity.

---

## Configuration

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = "europe-west1"
  # Authentification :
  # 1. GOOGLE_APPLICATION_CREDENTIALS env var (chemin vers la clé JSON)
  # 2. gcloud auth application-default login
  # 3. Workload Identity (dans GKE/Cloud Run)
}

# Exemple de ressource GCP
resource "google_compute_instance" "web" {
  name         = "web-server"
  machine_type = "e2-medium"
  zone         = "europe-west1-b"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}  # IP publique
  }
}
```
