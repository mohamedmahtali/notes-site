---
title: Device drivers
tags:
  - advanced
---

# Device drivers

---

## Définition

Les drivers de périphériques (device drivers) sont des [[Modules]] [[Kernel]] qui permettent au système de communiquer avec le matériel : disques, cartes réseau, GPU, cartes son. Sans driver approprié, le matériel est inaccessible.

---

## Types de périphériques

```
Character devices (c) : flux de données séquentiel
  /dev/tty, /dev/null, /dev/random, /dev/input/mice

Block devices (b) : accès aléatoire par blocs
  /dev/sda, /dev/nvme0, /dev/loop0

Network devices : pas de fichier /dev/
  eth0, wlan0, lo (gérés via iproute2)
```

---

## Commandes

```bash
# Voir les périphériques détectés
lspci           # périphériques PCI
lsusb           # périphériques USB
lsblk           # périphériques de stockage

# Messages du kernel pour les drivers
dmesg | grep -i "eth0"
dmesg | grep -i "error"
dmesg | grep -i "firmware"

# Drivers chargés
lsmod
lsmod | grep -i "e1000"   # driver Intel Gigabit

# Quel driver gère un périphérique ?
ls -la /sys/class/net/eth0/device/driver

# Informations détaillées
udevadm info /dev/sda
```

---

> [!note]
> En [[DevOps]] [[Cloud]], les drivers sont rarement un problème — les AMIs/images cloud incluent les drivers appropriés. La gestion des drivers est plus pertinente pour du bare metal ou des hyperviseurs.
