---
title: Symbolic links
tags:
  - beginner
---

# Symbolic links

---

## Définition

Un lien symbolique (symlink) est un fichier spécial qui contient le chemin vers une cible. C'est l'équivalent d'un raccourci. Si la cible est supprimée, le symlink devient un "lien cassé" (dangling symlink).

---

## Commandes

```bash
# Créer un symlink
ln -s /opt/app/v2.1.0 /opt/app/current

# Pointer un binaire vers /usr/local/bin
ln -s /opt/app/current/bin/mon-app /usr/local/bin/mon-app

# Voir les symlinks
ls -la /opt/app/
# lrwxrwxrwx 1 root root 14 Jan 15 10:00 current -> /opt/app/v2.1.0

# Résoudre un symlink (chemin réel)
readlink -f /usr/local/bin/mon-app
realpath /usr/local/bin/mon-app

# Supprimer un symlink (sans trailing slash)
rm /opt/app/current        # ✅ supprime le lien
rm -rf /opt/app/current/   # ❌ supprime la cible !

# Mettre à jour (atomique)
ln -sfn /opt/app/v2.2.0 /opt/app/current
```

---

## Pattern de déploiement

```bash
# Déploiement sans downtime
/opt/app/
├── v2.0.0/
├── v2.1.0/
├── v2.2.0/     ← nouvelle version
└── current -> v2.2.0   ← mise à jour atomique du symlink
```
