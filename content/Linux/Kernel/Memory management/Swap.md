---
title: Swap
tags:
  - intermediate
---

# Swap

## Parent
- [[Memory management]]

---

## Définition

Le swap est un espace disque utilisé comme extension de la RAM. Quand la RAM est pleine, le kernel déplace des pages mémoire rarement utilisées vers le swap. C'est une sécurité — pas un remplacement de la RAM.

---

## Commandes

```bash
# Voir l'utilisation du swap
free -h
swapon --show

# Créer un fichier de swap
dd if=/dev/zero of=/swapfile bs=1M count=2048   # 2 GB
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile

# Désactiver le swap
swapoff -a

# Désactiver un swap spécifique
swapoff /swapfile

# Rendre permanent (/etc/fstab)
/swapfile none swap sw 0 0
```

---

## Swappiness

```bash
# Contrôle le seuil à partir duquel le kernel utilise le swap
cat /proc/sys/vm/swappiness
# 60 = défaut (swap quand 40% RAM libre)

# Réduire pour les serveurs (swap seulement en dernier recours)
sysctl -w vm.swappiness=10

# Pour les conteneurs/Kubernetes
sysctl -w vm.swappiness=1

# Permanent
echo "vm.swappiness=10" >> /etc/sysctl.conf
```

---

> [!warning]
> Pour les bases de données (PostgreSQL, MySQL, Redis) et Kubernetes, désactiver le swap ou le réduire au minimum. Le swap cause des latences imprévisibles incompatibles avec les SLA de ces systèmes.
