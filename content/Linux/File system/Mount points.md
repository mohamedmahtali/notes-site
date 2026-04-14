---
title: Mount points
tags:
  - intermediate
---

# Mount points

## Parent
- [[File system]]

---

## Définition

Un point de montage est un répertoire sur lequel un filesystem est "monté" — rendu accessible dans l'arborescence Linux. Tout le stockage supplémentaire (disques, partitions, NFS, tmpfs) est monté sur des répertoires existants.

---

## Commandes

```bash
# Voir les filesystems montés
mount
df -h

# Monter un disque
mount /dev/sdb1 /mnt/data

# Monter une image ISO
mount -o loop fichier.iso /mnt/iso

# Monter en lecture seule
mount -o ro /dev/sdb1 /mnt/data

# Démonter
umount /mnt/data
umount -l /mnt/data    # lazy umount (attend que les processus terminent)

# Montages temporaires en RAM
mount -t tmpfs -o size=1G tmpfs /tmp/cache
```

---

## /etc/fstab (montages permanents)

```bash
# /etc/fstab
# Device          Mount    Type    Options         Dump  Pass
/dev/sda1         /        ext4    defaults         0     1
/dev/sda2         /boot    ext4    defaults         0     2
/dev/sdb1         /data    ext4    defaults,noatime 0     2
tmpfs             /tmp     tmpfs   size=2G,nosuid   0     0
192.168.1.100:/nfs /mnt/nfs nfs   defaults         0     0

# Appliquer les montages fstab sans reboot
mount -a
```
