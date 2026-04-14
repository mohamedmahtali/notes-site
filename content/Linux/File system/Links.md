---
title: Links
tags:
  - intermediate
---

# Links

## Parent
- [[File system]]

## Enfants
- [[Hard links]]
- [[Symbolic links]]

---

## Définition

Linux supporte deux types de liens : les **liens durs** (hard links) et les **liens symboliques** (symlinks). Les deux permettent d'accéder au même contenu via plusieurs noms/chemins.

---

## Hard link vs Symbolic link

| Critère | Hard link | Symbolic link |
|---|---|---|
| Pointe vers | Inode | Chemin |
| Cross-filesystem | ❌ Non | ✅ Oui |
| Sur dossiers | ❌ Non | ✅ Oui |
| Si fichier source supprimé | ✅ Données préservées | ❌ Lien cassé |
| Vu comme | Fichier normal | `lrwxrwxrwx` dans ls |

---

## Commandes

```bash
# Créer un hard link
ln fichier-source lien-dur

# Créer un lien symbolique
ln -s cible nom-du-lien
ln -s /opt/app/current/bin/app /usr/local/bin/app

# Voir les liens
ls -la    # les symlinks montrent → cible
ls -i     # hard links partagent le même inode

# Trouver les hard links d'un inode
find / -inum $(stat -c %i fichier)

# Vérifier si un symlink est valide
file /usr/local/bin/app
ls -la /usr/local/bin/app
```
