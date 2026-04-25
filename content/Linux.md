---
title: Linux
tags:
  - beginner
---

# Linux

---

## Définition

Linux est un système d'exploitation open source basé sur le [[Kernel]] Linux, créé par Linus Torvalds en 1991. C'est le système de référence pour les serveurs, le [[Cloud]], et les conteneurs — plus de 90% des serveurs web et la totalité des clouds publics tournent sur Linux.

---

## Pourquoi c'est important

> [!tip] La fondation du [[DevOps]]
> [[Docker]], [[Kubernetes]], les VMs cloud, les [[Pipeline]] CI/CD — tout tourne sur Linux. Sans bases solides en Linux, on travaille à l'aveugle sur l'infrastructure.

- **Omniprésent** : serveurs, conteneurs, cloud, IoT, Android
- **Open source** : code source modifiable et auditable
- **Stable** : des serveurs tournent des années sans reboot
- **Puissant** : [[Shell]] scripting, automatisation, outils en ligne de commande

---

## Distributions principales

| Distribution | Usage | [[Package]] manager |
|---|---|---|
| Ubuntu / Debian | Serveurs, développement | `apt` |
| RHEL / CentOS / Rocky | Enterprise | `yum` / `dnf` |
| Alpine | Conteneurs Docker | `apk` |
| Amazon Linux 2 | [[AWS]] | `yum` |
| Arch Linux | Desktop avancé | `pacman` |

---

## Commandes de base

```bash
# Navigation
pwd          # répertoire courant
ls -la       # lister avec détails
cd /opt/app  # changer de répertoire
find . -name "*.log"  # chercher des fichiers

# Fichiers
cat fichier.txt          # afficher
tail -f /var/log/app.log # suivre en temps réel
grep "ERROR" app.log     # chercher dans un fichier
cp, mv, rm, mkdir        # opérations de base

# Système
uname -a      # version kernel
df -h         # espace disque
free -h       # mémoire
uptime        # charge système
whoami        # utilisateur courant
```
