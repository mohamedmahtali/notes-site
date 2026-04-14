---
title: File types
tags:
  - beginner
---

# File types

## Parent
- [[File system]]

---

## Définition

Linux distingue plusieurs types de fichiers, tous accessibles via le même système de fichiers. Le type est visible dans `ls -la` via le premier caractère.

---

## Types et indicateurs

| Char | Type | Description |
|---|---|---|
| `-` | Fichier régulier | Texte, binaire, données |
| `d` | Répertoire | Contient d'autres fichiers |
| `l` | Lien symbolique | Pointeur vers un autre fichier |
| `c` | Fichier caractère | Périphériques (tty, console) |
| `b` | Fichier bloc | Périphériques de stockage (sda) |
| `p` | Named pipe (FIFO) | Communication inter-processus |
| `s` | Socket | Communication réseau/locale |

---

## Identifier le type

```bash
# Via ls
ls -la /dev/sda1
# brw-rw---- 1 root disk 8, 1 /dev/sda1   ← b = bloc

ls -la /dev/tty
# crw-rw-rw- 1 root tty 5, 0 /dev/tty     ← c = char

ls -la /tmp
# drwxrwxrwt 20 root root /tmp            ← d = dossier

# Via file (plus explicite)
file /bin/bash
# /bin/bash: ELF 64-bit LSB pie executable

file /etc/passwd
# /etc/passwd: ASCII text

# Via stat
stat /etc/hosts
```
