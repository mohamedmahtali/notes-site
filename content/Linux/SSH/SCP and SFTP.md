---
title: SCP and SFTP
tags:
  - beginner
---

# SCP and SFTP

---

## Définition

SCP (Secure [[COPY]]) et SFTP ([[SSH]] File Transfer Protocol) permettent le transfert de fichiers chiffré via SSH. SCP est simple et scriptable ; SFTP est plus interactif et supporte les opérations de navigation/gestion de fichiers.

---

## SCP

```bash
# Copier vers un serveur
scp fichier.txt user@serveur:/opt/app/

# Copier depuis un serveur
scp user@serveur:/var/log/app.log ./

# Copier un dossier (récursif)
scp -r ./dist/ user@serveur:/var/www/html/

# Avec un port non-standard
scp -P 2222 fichier.txt user@serveur:/tmp/

# Avec une clé SSH spécifique
scp -i ~/.ssh/prod_key fichier.txt user@serveur:/opt/
```

---

## rsync (meilleure alternative à SCP)

```bash
# Synchronisation incrémentale (copie seulement les différences)
rsync -avz ./dist/ user@serveur:/var/www/html/

# Avec suppression des fichiers supprimés localement
rsync -avz --delete ./dist/ user@serveur:/var/www/html/

# Via SSH non-standard
rsync -avz -e "ssh -p 2222" ./dist/ user@serveur:/var/www/
```

---

## SFTP

```bash
# Session SFTP interactive
sftp user@serveur

# Commandes SFTP
sftp> ls
sftp> cd /var/log
sftp> get app.log ./
sftp> put config.yaml /etc/app/
sftp> mkdir /opt/backup
sftp> exit
```
