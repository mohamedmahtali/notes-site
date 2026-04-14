---
title: Hard links
tags:
  - intermediate
---

# Hard links

## Parent
- [[Links]]

---

## Définition

Un hard link est une entrée de répertoire qui pointe directement vers le même inode qu'un autre fichier. Les deux noms sont équivalents — modifier ou supprimer l'un n'affecte pas l'autre tant qu'au moins un lien existe.

---

## Commandes

```bash
# Créer un hard link
ln fichier.txt lien-dur.txt

# Vérifier (même inode)
ls -i fichier.txt lien-dur.txt
# 12345 fichier.txt
# 12345 lien-dur.txt   ← même inode !

# Le compteur de liens augmente
stat fichier.txt | grep "Links"
# Links: 2

# Supprimer le fichier original → les données restent accessibles via lien-dur.txt
rm fichier.txt
cat lien-dur.txt    # toujours accessible
```

---

## Limitations

- Impossible entre filesystems différents
- Impossible sur des répertoires
- Le fichier n'est vraiment supprimé que quand le compteur de liens atteint 0
