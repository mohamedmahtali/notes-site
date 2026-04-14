---
title: Audit logs
tags:
  - advanced
---

# Audit logs

## Parent
- [[Logs]]

---

## Définition

Les audit logs (via `auditd`) enregistrent les événements de sécurité au niveau kernel : accès aux fichiers, exécutions de commandes, modifications de permissions, appels système. Requis pour les certifications de sécurité (PCI-DSS, SOC2, ISO 27001).

---

## Installation et configuration

```bash
# Installer auditd
apt-get install auditd

# Démarrer
systemctl enable auditd
systemctl start auditd

# Ajouter des règles d'audit
# Surveiller les accès à /etc/passwd
auditctl -w /etc/passwd -p rwa -k passwd-access

# Surveiller les commandes sudo
auditctl -a always,exit -F arch=b64 -S execve -F euid=0 -k root-commands

# Voir les règles actives
auditctl -l
```

---

## Consulter les logs

```bash
# Tous les événements
ausearch -ts today

# Événements d'un fichier
ausearch -f /etc/passwd

# Événements par clé
ausearch -k passwd-access

# Rapport résumé
aureport
aureport --login    # rapport des connexions
aureport --failed   # échecs
```

---

## Configuration permanente

```bash
# /etc/audit/rules.d/audit.rules
-w /etc/passwd -p rwa -k auth
-w /etc/shadow -p rwa -k auth
-w /etc/sudoers -p rwa -k sudoers
-a always,exit -F arch=b64 -S execve -F euid=0 -k privileged
```
