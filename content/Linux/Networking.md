---
title: Networking
tags:
  - intermediate
---

# Networking

---

## Définition

Le réseau [[Linux]] couvre la configuration des interfaces réseau, l'adressage IP, le routage, et les outils de diagnostic. C'est une compétence fondamentale pour l'administration serveur et le [[DevOps]].

---

## Commandes essentielles

```bash
# Interfaces réseau
ip addr show           # voir les IPs (remplace ifconfig)
ip link show           # état des interfaces
ip addr add 192.168.1.10/24 dev eth0   # ajouter une IP

# Routage
ip route show          # table de routage
ip route add default via 192.168.1.1   # ajouter une route

# Connexions actives
ss -tlnp               # ports en écoute (remplace netstat)
ss -s                  # statistiques réseau

# DNS
dig google.com         # résolution DNS détaillée
nslookup google.com    # résolution DNS simple
host google.com        # résolution rapide

# Diagnostic
ping 8.8.8.8           # test de connectivité
traceroute 8.8.8.8     # chemin réseau
mtr 8.8.8.8            # traceroute + ping continu
curl -v https://api.example.com   # test HTTP
```
