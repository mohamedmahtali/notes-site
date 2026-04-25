---
title: Instance types
tags:
  - intermediate
---
# Instance types

---

## Définition

Les [[Types]] d'instances définissent les ressources allouées à une VM : CPU, RAM, réseau, stockage. Chaque provider propose des dizaines de familles optimisées pour différents workloads.

---

## AWS EC2

| Famille | vCPU | RAM | Usage |
|---|---|---|---|
| t3.micro | 2 | 1 GB | Dev, test |
| t3.medium | 2 | 4 GB | Apps légères |
| m5.large | 2 | 8 GB | Usage général |
| m5.xlarge | 4 | 16 GB | Apps moyennes |
| c5.xlarge | 4 | 8 GB | Compute-intensif |
| r5.xlarge | 4 | 32 GB | Mémoire-intensif |

---

## GCP Machine Types

```bash
# Lister les types disponibles
gcloud compute machine-types list --filter="zone=europe-west1-b"

# Familles principales :
# e2-* : économique (partage CPU)
# n2-* : usage général
# c2-* : compute-optimized
# m2-* : memory-optimized
```

---

## Choisir le bon type

```
Règle pratique :
- Dev/test → t3.micro / e2-micro (économique)
- Web app standard → t3.medium / e2-medium
- API backend → m5.large
- DB in-memory → r5.xlarge
- ML training → p3.2xlarge (GPU)
- Big data → c5.4xlarge (compute)
```

---

> [!tip]
> Commencer petit et monitorer CPU/RAM. Il est plus facile de scaler up que de scaler down sans interruption de service.
