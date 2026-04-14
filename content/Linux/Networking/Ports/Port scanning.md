---
title: Port scanning
tags:
  - intermediate
---

# Port scanning

## Parent
- [[Ports]]

---

## Définition

Le port scanning consiste à sonder une machine pour déterminer quels ports sont ouverts (services en écoute). Indispensable pour l'audit de sécurité, le diagnostic réseau, et l'administration système.

---

## nmap

```bash
# Scan basique
nmap 192.168.1.10

# Scan de ports spécifiques
nmap -p 22,80,443 192.168.1.10

# Scan de tous les ports
nmap -p- 192.168.1.10

# Détection de service et version
nmap -sV 192.168.1.10

# Scan d'un sous-réseau
nmap 192.168.1.0/24

# Scan rapide (top 100 ports)
nmap -F 192.168.1.10

# Sans ping (si ICMP bloqué)
nmap -Pn 192.168.1.10
```

---

## nc (netcat) — test rapide

```bash
# Tester un port TCP
nc -zv 192.168.1.10 80

# Tester une plage de ports
nc -zv 192.168.1.10 20-25

# Test UDP
nc -zuv 192.168.1.10 53
```

---

> [!warning]
> Le port scanning sur des systèmes sans autorisation est illégal. Utiliser uniquement sur vos propres systèmes ou avec autorisation explicite.
