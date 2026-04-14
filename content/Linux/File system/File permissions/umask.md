---
title: umask
tags:
  - intermediate
---

# umask

## Parent
- [[File permissions]]

---

## Définition

`umask` (user file creation mask) définit les permissions par défaut retirées lors de la création de nouveaux fichiers et répertoires. C'est un masque de bits soustrait des permissions maximales.

---

## Fonctionnement

```
Permissions max fichier  : 666 (rw-rw-rw-)
umask par défaut         : 022
Résultat                 : 644 (rw-r--r--)

Permissions max dossier  : 777 (rwxrwxrwx)
umask par défaut         : 022
Résultat                 : 755 (rwxr-xr-x)
```

---

## Commandes

```bash
# Voir l'umask actuel
umask           # 0022
umask -S        # u=rwx,g=rx,o=rx (symbolique)

# Modifier pour la session courante
umask 027       # fichiers → 640, dossiers → 750
umask 077       # fichiers → 600, dossiers → 700 (max sécurité)

# Modifier de manière permanente
echo "umask 027" >> ~/.bashrc
echo "umask 027" >> /etc/profile  # pour tous les utilisateurs
```

---

## Valeurs courantes

| umask | Fichiers | Dossiers | Usage |
|---|---|---|---|
| `022` | 644 | 755 | Standard |
| `027` | 640 | 750 | Sécurisé (pas d'accès others) |
| `077` | 600 | 700 | Très privé |
