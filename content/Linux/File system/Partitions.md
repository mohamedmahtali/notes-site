---
title: Partitions
tags:
  - intermediate
---

# Partitions

## Parent
- [[File system]]

---

## Définition

Une partition est une division logique d'un disque physique. Chaque partition peut contenir un filesystem différent. Linux voit les disques comme `/dev/sda`, `/dev/sdb`, et les partitions comme `/dev/sda1`, `/dev/sda2`.

---

## Outils

```bash
# Voir les disques et partitions
lsblk
fdisk -l
parted -l

# Voir l'espace disque
df -h

# Partitionner un disque
fdisk /dev/sdb      # MBR (disques < 2TB)
gdisk /dev/sdb      # GPT (disques > 2TB)
parted /dev/sdb     # outil moderne

# Formater une partition
mkfs.ext4 /dev/sdb1
mkfs.xfs /dev/sdb1
mkfs.btrfs /dev/sdb1

# Vérifier/réparer
fsck /dev/sdb1       # arrêter de monter avant !
```

---

## Filesystems Linux courants

| FS | Usage | Avantages |
|---|---|---|
| ext4 | Usage général | Stable, mature |
| xfs | Gros volumes | Performance, scalabilité |
| btrfs | Stockage avancé | Snapshots, compression |
| tmpfs | RAM | Ultra-rapide, temporaire |
| nfs | Réseau | Partage de fichiers |

---

## LVM (Logical Volume Manager)

```bash
# LVM permet de redimensionner les volumes sans redémarrer
pvcreate /dev/sdb1              # créer un physical volume
vgcreate data-vg /dev/sdb1      # créer un volume group
lvcreate -L 50G -n data data-vg # créer un logical volume
mkfs.ext4 /dev/data-vg/data
mount /dev/data-vg/data /data
```
