---
title: Virtual Machines
tags:
  - intermediate
---
# Virtual Machines

## Parent
- [[Azure]]

---

## Définition

Les Azure Virtual Machines sont l'équivalent Azure d'EC2. Elles s'intègrent nativement avec Azure AD, Azure Disk Encryption, et les services réseau Azure.

---

## Commandes essentielles

```bash
# Créer un resource group
az group create --name myapp-rg --location westeurope

# Créer une VM
az vm create   --resource-group myapp-rg   --name myapp-vm   --image Ubuntu2204   --size Standard_B2s   --admin-username azureuser   --ssh-key-values ~/.ssh/id_rsa.pub

# Lister les VMs
az vm list --output table

# Démarrer/arrêter
az vm stop --resource-group myapp-rg --name myapp-vm
az vm start --resource-group myapp-rg --name myapp-vm

# Connexion SSH
az vm show --resource-group myapp-rg --name myapp-vm   --show-details --query publicIps -o tsv
# → ssh azureuser@<IP>
```

---

## Sizes communes

```
B2s   : 2 vCPU, 4 GB RAM (burstable, dev)
D2s_v3: 2 vCPU, 8 GB RAM (usage général)
F4s_v2: 4 vCPU, 8 GB RAM (compute)
E4s_v3: 4 vCPU, 32 GB RAM (mémoire)
```
