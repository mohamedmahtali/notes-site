---
title: Inodes
tags:
  - intermediate
---

# Inodes

---

## Définition

Un inode (index [[Node]]) est une structure de données du filesystem qui stocke les métadonnées d'un fichier : [[Permissions]], propriétaire, timestamps, taille, et les pointeurs vers les blocs de données. Chaque fichier a un inode unique ; le nom du fichier est stocké dans le répertoire, pas dans l'inode.

---

## Ce que contient un inode

```
Inode #12345 :
  - Type : fichier régulier
  - Permissions : 644
  - Propriétaire : UID 1001
  - Groupe : GID 1001
  - Taille : 4096 octets
  - Atime : 2024-01-15 10:30 (dernier accès)
  - Mtime : 2024-01-10 08:00 (dernière modification)
  - Ctime : 2024-01-10 08:00 (dernier changement d'inode)
  - Liens : 1
  - Pointeurs vers les blocs de données
```

---

## Commandes

```bash
# Voir le numéro d'inode
ls -i fichier
stat fichier | grep Inode

# Espace inodes disponible
df -i

# Trouver un fichier par son inode
find / -inum 12345

# Utilisation des inodes par répertoire
find /var -xdev -printf '%h
' | sort | uniq -c | sort -rn | head -10
```

---

## Saturation des inodes

```bash
df -i
# Filesystem     Inodes  IUsed  IFree  IUse% Mounted on
# /dev/sda1     655360  655360      0   100% /
# → Plus de fichiers créables même si espace disque disponible !

# Solution : trouver et nettoyer les dossiers avec beaucoup de petits fichiers
find /tmp -type f | wc -l
```
