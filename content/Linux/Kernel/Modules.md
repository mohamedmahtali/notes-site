---
title: Modules
tags:
  - advanced
---

# Modules

## Parent
- [[Kernel]]

---

## Définition

Les modules kernel sont des morceaux de code qui peuvent être chargés et déchargés du kernel sans redémarrage. Ils ajoutent des fonctionnalités : drivers de périphériques, filesystems, protocoles réseau.

---

## Commandes

```bash
# Lister les modules chargés
lsmod

# Informations sur un module
modinfo ext4
modinfo overlay   # utilisé par Docker

# Charger un module
modprobe overlay
modprobe br_netfilter

# Décharger un module
modprobe -r overlay
rmmod overlay

# Modules chargés au démarrage
cat /etc/modules               # Debian/Ubuntu
ls /etc/modules-load.d/        # systemd-modules-load
```

---

## Modules courants DevOps

```bash
# Pour Docker/Kubernetes
modprobe overlay       # filesystem overlay
modprobe br_netfilter  # bridge netfilter

# Vérifier si chargé
lsmod | grep overlay
lsmod | grep br_netfilter

# Persistant
cat > /etc/modules-load.d/k8s.conf << EOF
overlay
br_netfilter
EOF
```
