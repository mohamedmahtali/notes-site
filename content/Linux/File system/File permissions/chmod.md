---
title: chmod
tags:
  - beginner
---

# chmod

## Parent
- [[File permissions]]

---

## Définition

`chmod` (change mode) modifie les permissions d'un fichier ou répertoire. Deux syntaxes : numérique (octal) ou symbolique (u/g/o + r/w/x).

---

## Syntaxe

```bash
# Numérique
chmod 755 script.sh      # rwxr-xr-x
chmod 644 config.txt     # rw-r--r--
chmod 600 ~/.ssh/key     # rw-------
chmod 700 ~/.ssh/        # rwx------

# Symbolique
chmod +x script.sh       # ajouter exécution à tous
chmod u+x script.sh      # ajouter exécution au propriétaire
chmod g-w fichier        # retirer écriture au groupe
chmod o-rwx fichier      # retirer tout aux autres
chmod a+r fichier        # lecture à tous (a=all)
chmod u=rw,g=r,o= fichier  # définir explicitement

# Récursif
chmod -R 755 /var/www/html/
```

---

## Permissions courantes

| Permissions | Octal | Usage |
|---|---|---|
| `rwxr-xr-x` | 755 | Scripts, binaires, dossiers web |
| `rw-r--r--` | 644 | Fichiers de config, HTML |
| `rw-------` | 600 | Clés SSH, fichiers secrets |
| `rwx------` | 700 | Répertoires privés |
| `rwxrwxr-x` | 775 | Dossiers partagés dans un groupe |
