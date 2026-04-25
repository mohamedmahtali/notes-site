---
title: File system
tags:
  - beginner
---

# File system

---

## Définition

Le filesystem [[Linux]] est une hiérarchie de fichiers et répertoires commençant à la racine `/`. Tout est un fichier : les données, les périphériques, les sockets, les processus (via /proc). C'est la philosophie Unix.

---

## Hiérarchie FHS

```
/
├── bin/      ← binaires essentiels (ls, cp, bash)
├── boot/     ← kernel, initrd
├── dev/      ← fichiers de périphériques
├── etc/      ← configuration système
├── home/     ← homes des utilisateurs
├── lib/      ← bibliothèques partagées
├── media/    ← points de montage amovibles
├── mnt/      ← points de montage temporaires
├── opt/      ← logiciels tiers
├── proc/     ← système de fichiers virtuel (processus)
├── root/     ← home de root
├── run/      ← données runtime (PIDs, sockets)
├── srv/      ← données des services
├── sys/      ← devices, kernel
├── tmp/      ← fichiers temporaires
├── usr/      ← binaires, libs, share (lecture seule)
└── var/      ← données variables (logs, spool, cache)
```

---

## Commandes essentielles

```bash
df -h              # espace disque par partition
du -sh /var/log    # taille d'un dossier
ls -la             # lister avec permissions et liens
stat fichier       # métadonnées complètes
file fichier       # type de fichier
find / -name "*.log" -size +100M  # chercher des gros fichiers
```
