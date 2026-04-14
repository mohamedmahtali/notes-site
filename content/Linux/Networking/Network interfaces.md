---
title: Network interfaces
tags:
  - intermediate
---

# Network interfaces

## Parent
- [[Networking]]

---

## Définition

Une interface réseau est le point de connexion entre le système Linux et un réseau. Elle peut être physique (eth0, ens3), virtuelle (lo, docker0, virbr0), ou un tunnel (tun0, wg0).

---

## Commandes

```bash
# Lister les interfaces
ip link show
ip addr show

# Interface spécifique
ip addr show eth0
ip link show eth0

# Activer/désactiver
ip link set eth0 up
ip link set eth0 down

# Configurer une IP (temporaire)
ip addr add 192.168.1.10/24 dev eth0
ip addr del 192.168.1.10/24 dev eth0

# Voir les stats
ip -s link show eth0
cat /proc/net/dev

# Nomenclature moderne (systemd)
ip addr
# eth0   → ancienne nomenclature
# ens3   → PCI slot (predictable)
# enp0s3 → bus PCI + slot
# wlan0  → WiFi
# lo     → loopback (127.0.0.1)
```

---

## Configuration permanente

```bash
# Netplan (Ubuntu 18+)
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses: [192.168.1.10/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]

sudo netplan apply
```
