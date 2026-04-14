---
title: File permissions
tags:
  - beginner
---

# File permissions

## Parent
- [[File system]]

## Enfants
- [[chmod]]
- [[chown]]
- [[chgrp]]
- [[umask]]

---

## Définition

Chaque fichier Linux a des permissions pour trois entités : le propriétaire (user), le groupe (group), et les autres (others). Ces permissions (read/write/execute) contrôlent qui peut lire, modifier, ou exécuter un fichier.

---

## Lire les permissions

```bash
ls -la
# drwxr-xr-x  2 mohamed www-data 4096 Jan 15 10:00 /var/www
# -rw-r--r--  1 root    root      644 Jan 10 08:00 /etc/passwd

# Format : type + user + group + others
# d rwx r-x r-x
# │ │   │   └─ others : r-x = lecture + exécution
# │ │   └───── group  : r-x = lecture + exécution
# │ └───────── user   : rwx = lecture + écriture + exécution
# └─────────── type   : d=dossier, -=fichier, l=lien, c=char, b=block
```

---

## Valeurs numériques

| Valeur | Permissions |
|---|---|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |
| 0 | --- |

```
chmod 755 script.sh  →  rwxr-xr-x
chmod 644 fichier    →  rw-r--r--
chmod 600 ~/.ssh/id_ed25519  →  rw-------
```

---

## Permissions spéciales

```bash
chmod +s fichier    # setuid/setgid
chmod +t /tmp       # sticky bit
```
