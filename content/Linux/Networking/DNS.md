---
title: DNS
tags:
  - beginner
---

# DNS

---

## Définition

DNS (Domain Name System) est le système qui traduit les noms de domaine (`google.com`) en adresses IP (`142.250.185.78`). C'est l'annuaire d'internet — sans DNS, il faudrait mémoriser les IPs de tous les sites.

---

## Résolution DNS

```
Client → Résolveur local (/etc/resolv.conf)
       → Serveur récursif (8.8.8.8)
       → Root servers (.)
       → TLD servers (.com)
       → Authoritative server (google.com)
       → Réponse : 142.250.185.78
```

---

## Commandes

```bash
# Résoudre un nom
dig google.com
dig google.com A       # enregistrement A (IPv4)
dig google.com AAAA    # enregistrement AAAA (IPv6)
dig google.com MX      # serveurs mail
dig google.com NS      # serveurs DNS autoritatifs
dig @8.8.8.8 google.com  # utiliser un DNS spécifique

# Simple
nslookup google.com
host google.com

# Résolveurs configurés
cat /etc/resolv.conf
```

---

## /etc/hosts

```bash
# Fichier de résolution locale (priorité sur DNS)
cat /etc/hosts
# 127.0.0.1   localhost
# 192.168.1.10  mon-serveur mon-serveur.local
```
